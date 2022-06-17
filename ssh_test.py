import os
a=os.path.isfile(os.path.join('/home/gitpod/.ssh','ka'))
print(a)
os.system('echo '' ''| ssh-keygen -t rsa -f /home/gitpod/.ssh/kaa')