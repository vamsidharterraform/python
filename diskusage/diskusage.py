import subprocess

usage = subprocess.run( ['df', '-h' , '/'], capture_output=True, text=True)
print(usage.stdout)

print("after splitting")

lines = usage.stdout.splitlines()
print(lines)

print("after splitting by line wise")

linessplit1 = lines[1].split()

print(linessplit1)

# lines = output.splitlines()

# data = lines[1].split()

# print(data)
usage = linessplit1[4]
print(usage)

if usage >= 85:
    print("disk usage is greater than 85% that is :", usage)
else:
    print("disk usage is less than 85% that is :", usage)