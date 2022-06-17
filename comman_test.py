import os
import subprocess
import re 
p = subprocess.Popen('whoami',shell=True,stdout=subprocess.PIPE)  

out,err = p.communicate()  
print(out)
res=re.search('.*\'(.*)\\n.*', "b'gitpod\\n'")
out_=str(out, encoding = "utf-8")
out_=bytes.decode(out.splitlines()[0])
print(out_)
print("res:",res)

for line in out.splitlines():   
    print(line)  
