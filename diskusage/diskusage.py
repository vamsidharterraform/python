import subprocess

usage = subprocess.run( ['df', '-h' , '/'], capture_output=True, text=True)
print(usage.stdout)
print("after splitting")
print(usage.stdout.splitlines())

# lines = output.splitlines()

# data = lines[1].split()

# print(data)