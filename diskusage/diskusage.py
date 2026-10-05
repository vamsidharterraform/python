import subprocess

usage = subprocess.run( ['df', '-h' , '/'], capture_output=True, text=True)
print(usage.stdout)