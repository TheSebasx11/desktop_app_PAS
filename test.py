import sys 
import os
import subprocess
import tempfile


cmd = "echo pere"
output = ""
with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen(cmd, stdout=tempf,shell=True)
    proc.wait()
    tempf.seek(0)
    output = tempf.read()    
    print(output)
output = str(output.decode('utf-8', errors='replace'))
print(f"{output.strip()}")


