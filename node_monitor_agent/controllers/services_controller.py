import connexion
import six
import subprocess
from node_monitor_agent import util


def service_service_call_get(service, call):  # noqa: E501
    """check service status

    Check service status # noqa: E501

    :param service: service name
    :type service: str
    :param call: send remote command to service
    :type call: str

    :rtype: None
    """
    return 'do some magic!'


def service_service_get(service):  # noqa: E501
    key = util.key()
    if key == 401:
        return 'Invalid key', 401
    
    service = service.encode()
    output = subprocess.check_output(['ps', '-A'])
    if service in output:
        result = 1
    else:
        result = 0

    return result
