import subprocess
import shlex
import os
# setting environment variables
print("Setting env variables")
os.environ['USER1'] = 'Rohan'
os.environ['USER2'] = 'Rahul'
os.environ['USER3'] = 'Rakhi'

# calling shellscript
print("Calling script.sh!!!!!")
subprocess.call(shlex.split("./script.sh -a Rohan  -b Rahul  -c Rakhi"))




# print(os.environ['HOME'])
# print("Hello world")


