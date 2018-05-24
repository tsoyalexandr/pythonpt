import transports


class UnknownTransport(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def get_transport(transport_name):
    try:
        if transport_name == 'SSH':
            return transports.TransportSSH()
        else:
            raise UnknownTransport('UnknownTransport')
    except UnknownTransport as error:
        return error.value


# print(get_transport('SSH').exec('cd /home/alexandr/ && ls'))
# print(get_transport('SSH').get_file('/home/alexandr/file.txt', r'C:\Users\tavav\PycharmProjects\local.txt'))
