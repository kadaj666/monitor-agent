import connexion
import six
from zencow_agent import util
from zencow_agent import config
import json
import subprocess


def agent_hwid_version_service_user_get(hwid, service, user):  # noqa: E501
    if hwid == config.hwid and service == 'zendinfo':
        result = zendinfo(user)
    elif hwid == config.hwid and service == 'zendblocks':
        result = zendblocks(user)
    else:
        result = "Fuck off"
    return result


def zendinfo(user):
    output = subprocess.run("su -c 'zen-cli getnetworkinfo' %s" %(user,), shell=True, stdout=subprocess.PIPE, 
                            universal_newlines=True)
    zenver = json.loads(output.stdout)
    return zenver

def zendblocks(user):
    output = subprocess.run("su -c 'zen-cli getinfo' %s" %(user,), shell=True, stdout=subprocess.PIPE, 
                            universal_newlines=True)
    zenver = json.loads(output.stdout)
    return zenver