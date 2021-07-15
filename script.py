import subprocess

import os
# setting environment variables
print("Setting env variables")
os.environ['USER1'] = 'Rohan'
os.environ['USER2'] = 'Rahul'
os.environ['USER3'] = 'Rakhi'

# calling shellscript
print("Calling script.sh")
subprocess.call(['bash','./script.sh'])




print(os.environ['HOME'])

print("Hello world")


