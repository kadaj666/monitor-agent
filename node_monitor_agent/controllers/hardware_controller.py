import connexion
import six
import psutil, os, socket
from node_monitor_agent import util

af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}


def cpu_detail_get(detail):  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    
    if detail == 'info':
        result = cpuinfo()
    elif detail == 'cpu_times':
        result = psutil.cpu_times()
    elif detail == 'cpu_percent':
        result = psutil.cpu_percent(interval=1, percpu=True)
    elif detail == 'cpu_percent_total':
        result = psutil.cpu_percent(interval=1)
    elif detail == 'cpu_stats':
        result = psutil.cpu_stats()
    elif detail == 'cpu_freq':
        result = psutil.cpu_freq(percpu=True)
    
    return result


def disk_detail_get(detail):  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    if detail == 'partitions':
        result = disk_detail()
    elif detail == 'disk_io_counters':
        result = psutil.disk_io_counters(perdisk=True)
    elif detail == 'disk_rw':
        result = disk_rw()
    return result


def mem_detail_get(detail):  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    
    if detail == 'virtual':
        result = psutil.virtual_memory()
    elif detail == 'swap':
        result = psutil.swap_memory()
    return result


def net_detail_get(detail):  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401

    if detail == 'addr':
        result = address_info()
    
    if detail == 'counters':
        result = net_counters()

    return result


def cpuinfo():
    cpucount=0
    cpu = dict()
    with open('/proc/cpuinfo') as f:
        for line in f:
            if 'model name' in line:
                model = line.split(':')[1].strip()
                cpu['model'] = model
                cpucount = cpucount + 1
            if 'flags' in line:
                if 'vmx' in line or 'svm' in line:
                    virtualization = True
                else:
                    virtualization = False
                if 'ht' in line:
                    hyperthreading = True
                else:
                    hyperthreading = False
            if 'cpu cores' in line:
                cpucores = line.split(':')[1].strip()
    cpu['virtualization'] = virtualization
    cpu['hyperthreading'] = hyperthreading
    cpu['cpucores'] = cpucores
    cpu['processorcount'] = cpucount
    return cpu

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def disk_detail():
    data=[]
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        
        data.append({'Device': part.device, 'Total': bytes2human(usage.total), 'Used': bytes2human(usage.used),'Free': bytes2human(usage.free),'Use_perc': int(usage.percent),'Type': part.fstype,'Mount': part.mountpoint })
    return data

def disk_rw():
    """
    Get the disk reads and writes
    """
    try:
        pipe = os.popen("cat /proc/partitions | grep -v 'major' | awk '{print $4}'")
        data = pipe.read().strip().split('\n')
        pipe.close()

        rws = []
        for i in data:
            if i.isalpha():
                pipe = os.popen("cat /proc/diskstats | grep -w '" + i + "'|awk '{print $4, $8}'")
                rw = pipe.read().strip().split()
                pipe.close()

                rws.append([i, rw[0], rw[1]])

        if not rws:
            pipe = os.popen("cat /proc/diskstats | grep -w '" + data[0] + "'|awk '{print $4, $8}'")
            rw = pipe.read().strip().split()
            pipe.close()

            rws.append([data[0], rw[0], rw[1]])

        data = rws

    except Exception as err:
        data = str(err)

    return data


def address_info():
    data = []
    io_counters = psutil.net_io_counters(pernic=True)
    for nic, addrs in psutil.net_if_addrs().items():
        def addr_inf():
            addr_info = []
            for addr in addrs:
                addr_type = (af_map.get(addr.family, addr.family))
                addr_info.append({addr_type:{"address":addr.address,"netmask":addr.netmask,"broadcast":addr.broadcast}})
            return addr_info
        data.append({nic:addr_inf()})
    return data

def net_counters():
    data = []
    io_counters = psutil.net_io_counters(pernic=True)
    for nic, addrs in psutil.net_if_addrs().items():
        def inco():
            if nic in io_counters:
                incout = []
                io = io_counters[nic]
                incout.append({"incoming":{"bytes":bytes2human(io.bytes_recv),"pkts":io.packets_recv,"errs":io.errin,"drops":io.dropin},"outgoing":{"bytes":bytes2human(io.bytes_sent),"pkts":io.packets_sent,"errs":io.errout,"drops":io.dropout}})
            return incout
        data.append({nic:inco()})
    return data