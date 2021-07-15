import subprocess
import shlex
import os
os.environ['USER1'] = 'Rohan'
os.environ['USER2'] = 'Rahul'
os.environ['USER3'] = 'Rakhi'
subprocess.call(shlex.split('./script.sh USER1 USER2 USER3'))



print(os.environ['HOME'])

print("Hello world")


