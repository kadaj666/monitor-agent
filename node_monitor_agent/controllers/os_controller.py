import connexion
import six
import psutil, datetime, platform, socket, os, json
from node_monitor_agent import util


def boot_time_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    boot_time = (datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    return boot_time


def distr_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    dist = platform.linux_distribution()
    distinfo = {'distname': dist[0], 'version': dist[1], 'id': dist[2]}
    return distinfo    



def hostname_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    fqdn = socket.getfqdn()
    return fqdn



def la_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    load = json.dumps(os.getloadavg())
    return load


def python_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    return platform.python_version()


def top5cpu_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    top_cpu = ([(p.pid, p.info['name'], sum(p.info['cpu_times'])) for p in sorted(psutil.process_iter(attrs=['name', 'cpu_times']), key=lambda p: sum(p.info['cpu_times'][:2]))][-5:])
    return top_cpu

def top5mem_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    top_mem = ([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent']), key=lambda p: p.info['memory_percent'])][-5:])
    return top_mem
