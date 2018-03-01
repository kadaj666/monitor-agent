import connexion
import six
from zencow_agent import config
from zencow_agent import util


def agent_get():  # noqa: E501
    return 'ok'


def agent_hwid_get(hwid):  # noqa: E501
    if hwid == config.hwid:
        result = "ok"
    else:
        result = "Fuck off"
    return (result)
