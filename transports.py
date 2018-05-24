import ssh


class TransportSSH:
    @staticmethod
    def exec(command):
        stdin, stdout, stderr = ssh.get_connect().exec_command(command)
        return stdout.read().decode('ascii')

    @staticmethod
    def get_file(remote, local):
        stdin, stdout, stderr = ssh.get_connect().exec_command('cat %s' % remote)
        sftp_client = ssh.get_connect().open_sftp()
        if not stderr.readlines():
            sftp_client.get(remote, local)
            content = []
            for line in stdout:
                content.append(line)
            return content
        else:
            stdin, stdout, stderr = ssh.get_connect().exec_command('cat %s' % remote)
            return stderr.readlines()
