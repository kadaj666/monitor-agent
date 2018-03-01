import connexion
import six
from zencow_agent import util
from zencow_agent import config
import os
import json
import shutil
import platform
import socket






def agent_hwid_iron_device_get(hwid, device):  # noqa: E501
    if hwid == config.hwid and device == 'ram':
        result = memory()
    elif hwid == config.hwid and device == 'disk':
        result = disk_usage()
    elif hwid == config.hwid and device == 'la':
        result = load_av()
    elif hwid == config.hwid and device == 'fqdn':
        result = fqdn()
    elif hwid == config.hwid and device == 'distr':
        result = distribution()
    elif hwid == config.hwid and device == 'cpu':
        result = cpu()
    else:
        result = "Fuck off"
    return result



def memory():
    # Get node total memory and memory usage
    with open('/proc/meminfo', 'r') as mem:
        ret = {}
        tmp = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) == 'MemTotal:':
                ret['total'] = int(sline[1])
            elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                tmp += int(sline[1])
        ret['free'] = tmp
        ret['used'] = int(ret['total']) - int(ret['free'])
    return ret




def disk_usage():
    # Getting / partition usage
    total, used, free = shutil.disk_usage(__file__)
    total = str(total/1073741824)[:4]
    free = str(free/1073741824)[:4]
    used = str(used/1073741824)[:4]
    result = json.dumps({'total': total, 'free': free, 'used': used}, indent=4, separators=(',', ': '))
    result = json.loads(result)
    return result

def load_av():
    load = json.dumps(os.getloadavg())
    load = json.loads(load)
    return load

def fqdn():
    # Getting FQDN
    fqdn = socket.getfqdn()
    return fqdn

def distribution():
    # Getting distribution
    dist = platform.linux_distribution()
    distname = dist[0]
    version = dist[1]
    distid = dist[2]
    distinfo = {'distname': distname, 'version': version, 'id': distid}
    return distinfo

def cpu():
    # Getting CPU info
    cpucount=0
    cpuinfo = dict()
    with open('/proc/cpuinfo') as f:
        for line in f:
            if 'model name' in line:
                model = line.split(':')[1].strip()
                cpuinfo['model'] = model
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
    cpuinfo['virtualization'] = virtualization
    cpuinfo['hyperthreading'] = hyperthreading
    cpuinfo['cpucores'] = cpucores
    cpuinfo['processorcount'] = cpucount
    return cpuinfo


