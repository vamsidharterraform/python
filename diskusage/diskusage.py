import subprocess

usage = subprocess.run( ['df', '-h' , '/'], capture_output=True, text=True)
print(usage.stdout)
print("after splitting")

lines = usage.stdout.splitlines()
print(lines)

linessplit1 = lines[1].split()

print(linessplit1)

# lines = output.splitlines()

# data = lines[1].split()

# print(data)