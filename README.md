# pythonpt
1. Download files in one directory:
  - env.json
  - get_config.py
  - get_transport.py
  - ssh.py
  - transports.py
  
 2. Docker
  - create docker container cont-ubuntu-ssh
  - mkdir /home/alexandr
  - create file.txt with content
  
 3. Run
  - open get_transport.py
  - add lines:
  print(get_transport('SSH').exec('cd /home/alexandr/ && ls'))
  print(get_transport('SSH').get_file('/home/alexandr/file.txt', r'C:\Users\tavav\PycharmProjects\local.txt'))
