# 1. String indexing and slicing

# Tasks:
# - Print the first character and last character.
# - Print "prod" using slicing.
# - Reverse the entire string.

server_name = "prod-web-server-01"

# 2. String methods: upper(), lower(), title()

# Tasks:
# - Convert the string to uppercase.
# - Convert it to lowercase.
# - Convert the first letter of each word to uppercase.

environment = "production server monitoring"






# 3. split() and join()

# Tasks:
# - Split the string using the comma.
# - Print only the error message.
# - Join the resulting parts using " | " as the separator.

log = "ERROR,2026-10-19,Database connection failed"




# 4. strip(), lstrip(), rstrip()

# Tasks:
# - Remove spaces from both sides.
# - Remove only leading spaces.
# - Remove only trailing spaces.


server = "   prod-api-01   "






# 5. replace() and count()

# Tasks:
# - Count how many times "ERROR" appears.
# - Replace "ERROR" with "WARNING".
# - Count how many times "failed" appears.


log = "ERROR: API failed. ERROR: Database failed. ERROR: Timeout."




# 6. startswith() and endswith()

# Tasks:
# - Print only filenames starting with "prod".
# - Print only filenames ending with ".tf".
# - Count how many files start with "prod".


files = [
    "prod.tf",
    "dev.tf",
    "prod.yaml",
    "test.py",
    "prod.json"
]






# 7. find(), index() and in

# Tasks:
# - Check whether "timeout" exists in the log.
# - Find the position of "database".
# - Find the position of "WARNING" using find() and observe the result.

log = "ERROR: Connection timeout while accessing database"




# 8. f-strings and string formatting

# Tasks:
# - Print a message containing the server name, CPU usage, and status.
# - Print the CPU usage with a % symbol.
# - Print a message such as CRITICAL: prod-api-01 is using 92% CPU.


server = "prod-api-01"
cpu = 92
status = "CRITICAL"





# Bonus challenge — Real-world DevOps log parsing

# Using string methods only:
# 1. Extract the date.
# 2. Extract the log level (ERROR).
# 3. Extract the server name (prod-api-01).
# 4. Extract the CPU usage as an integer (92).
# 5. Print a warning if CPU usage is 80 or higher.


log = "2026-10-19 10:30:15 ERROR [prod-api-01] CPU usage reached 92%"






# How we'll practise: Complete Task 1 first and send me your code. I'll review it, explain any mistakes, and then we'll move to Task 2.