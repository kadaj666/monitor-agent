import connexion
import six
from zencow_agent import config
from zencow_agent import util
import subprocess


def agent_hwid_services_service_get(hwid, service):  # noqa: E501
    if hwid == config.hwid:
        service = service.encode()
        output = subprocess.check_output(['ps', '-A'])
        if service in output:
            result = 1
        else:
            result = 0
    else:
        result = "Fuck off"
    return result
