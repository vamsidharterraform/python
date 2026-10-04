# Find HTTP 500 errors

with open('app.log' , 'r') as inp:
    for line in inp:
        if "Response status: 500" in line:
            print(line)

# Find authentication failures

with open('app.log' , 'r') as inputfile:
    for line in inputfile:
        if "Failed login attempt" in line or "authentication failures" in line:
            print(line.strip())

# Find entries from a particular date

date = "2026-09-27"

with open("app.log", "r") as inputfile:
    for line in inputfile:
        if date in line:
            print(line.strip())

            