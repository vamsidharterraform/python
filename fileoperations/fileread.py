# # read the file

with open('app.log', 'r') as file:
    for line in file:
        if "ERROR" in line:
          
          print(line.strip())


# # Count ERRORs
count = 0

with open('app.log' , 'r') as file:
   for line in file:
      if "ERROR" in line:
         count += 1
print("error matching lines count is :" , count)


# # Extract ERROR lines into errors.log
with open('app.log', 'r') as infile, open('errors.log', 'w') as outfile:
    for line in infile:
        if "ERROR" in line:
            outfile.write(line)


with open("app.log" , 'r') as inputfile , open('out.log' , 'w') as outfile:
    for line in inputfile:
        if "ERROR" in line:
          outfile.write(line)