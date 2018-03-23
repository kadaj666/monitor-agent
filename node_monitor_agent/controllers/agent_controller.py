import connexion
import six

from node_monitor_agent import util, config


def agent_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    return config.ver


def key_get():  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    return 'Authorized', 200



def root_get():  # noqa: E501
    return '0'
