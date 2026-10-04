import sys

with open('app.log' , 'r') as inputfile:
    for line in inputfile:
        if "ERROR" in line:
            print("ERROR found:", line.strip())
            sys.exit(1)

            
print("No errors found")
sys.exit(0)