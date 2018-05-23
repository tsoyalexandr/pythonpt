import paramiko
import get_config as att


def get_connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(att.get_config()['host'],
                   att.get_config()['transports']['SSH']['port'],
                   att.get_config()['transports']['SSH']['login'],
                   att.get_config()['transports']['SSH']['password'])
    return client
