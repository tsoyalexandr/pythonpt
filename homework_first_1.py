import paramiko
import pytest

'''
Реализовать функцию get_transport(transport_name, host, port, login, password), которая возвращает instance транспорта
Выбрасывает исключение:
UnknownTransport - в случае если транспорта не существует.
'''


def get_transport(transport_name, host, port, login, password):
    try:
        if transport_name == 'SSH':
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port, login, password)
            client.close()
            return paramiko.AUTH_SUCCESSFUL
        else:
            raise NameError('UnknownTransport')
    except paramiko.AuthenticationException:
        raise paramiko.AuthenticationException('Authentication failed, please verify your data')
    except paramiko.ssh_exception.NoValidConnectionsError:
        print('Connection failed')


def test_get_transport():
    check_transport_name = get_transport('SSH', 'localhost', 22022, 'root', 'pwd')
    assert check_transport_name == paramiko.AUTH_SUCCESSFUL


def test_some_exception():
    with pytest.raises(paramiko.AuthenticationException):
        get_transport('SSH', 'localhost', 22022, 'admin', 'pwd')


