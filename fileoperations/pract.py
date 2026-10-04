# 1. Read the entire file
# 2. Read line by line
# 3. Find ERROR lines
# 4. Find WARNING lines
# 5. Count ERRORs
# 6. Count WARNINGs
# 7. Extract ERROR lines into errors.log
# 8. Find database-related errors
# 9. Find HTTP 500 errors
# 10. Find authentication failures
# 11. Find entries from a particular date
# 12. Find the latest ERROR
# 13. Generate an error summary
# 14. Monitor the log continuously
# 15. Exit with code 1 if ERROR is found

# with open('app.log' , 'r')as infile:
#     content = infile.read()
#     print(content)

# with open('app.log' , 'r')as infile:
#     for line in infile:
#         print(line.strip())

# with open('app.log' , 'r') as infile:
#     for line in infile:
#         if "ERROR" in line or "WARNING" in line:
#             print(line.strip())

# with open('app.log' , 'r') as infile , open('errors.log' , 'w') as writefile:
#     for line in infile:
#         if "ERROR" in line:
#             writefile.write(line)

# print('errors.log')

# with open('app.log' , 'r') as infile:
#     for line in infile:
#         if "ERROR" in line and "database" in line.lower():
#             print(line)


# with open('app.log' , 'r') as infile:
#     for line in infile:
#         if "500" in line:
#             print(line)

# with open('app.log' , 'r') as infile:
#     for line in infile:
#         if "authentication failures" in line:
#             print(line)

date = "2026-09-28"
with open('app.log' , 'r') as infile:
    for line in infile:
        if date in line:
            print(line)