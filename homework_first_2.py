import paramiko
import pytest

'''
Реализовать класс транспорта SSH
    Методы:
    - exec(command) - выполняет команду на целевом хосте в виде юникод строки результат выполнения;
    - get_file(path) - скачивать файлы с целевого хоста, возвращает содержимое файла.
    Выбрасывает исключения:
    TransportError - в случае отсутствия команды или файла;
    TransportConnectionError - в случае ошибок подключения.
'''


class TransportSSH:

    def __init__(self, host, port, login, password):
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        # attributes
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.port, self.login, self.password)

    def exec(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            if stderr.readlines():
                raise paramiko.ssh_exception.SSHException
            else:
                print(stdout.read())
                return paramiko.AUTH_SUCCESSFUL
        except paramiko.ssh_exception.SSHException:
            raise NameError('TransportError')
        finally:
            self.client.close()

    def get_file(self, remote_file_path, local_file_path):
        try:
            sftp_load_file = self.client.open_sftp()
            sftp_load_file.get(remote_file_path, local_file_path)
        except IOError:
            raise print('TransportError')

        sftp_load_file.close()

    def read_file(self, read_file):
        self.client.connect(self.host, self.port, self.login, self.password)
        stdin, stdout, stderr = self.client.exec_command(read_file)
        for line in stdout:
            print(line.strip('\n'))
        self.client.close()


# s = TransportSSH('localhost', 22022, 'root', 'pwd')                                      # create exemplar
# s.exec('cd /home/alexandr/ && ls')                                                       # run command
# s.get_file('/home/alexandr/documents/game1.txt', '/home/alexandr/Documents/game3.txt')    # download the file
# s.read_file('cat /home/alexandr/documents/game.txt')                                     # read the file content


def test_get_transport():
    s = TransportSSH('localhost', 22022, 'root', 'pwd')
    assert s.exec('cd /home/alexandr/ && ls') == paramiko.AUTH_SUCCESSFUL

