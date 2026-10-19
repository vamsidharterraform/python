# Python String Practice — DevOps Tasks

## 1. String Indexing and Slicing

**Tasks:**
- Print the first character and last character.
- Print `"prod"` using slicing.
- Reverse the entire string.

**Syntax:** `string[start:stop:step]`

```python
server_name = "prod-web-server-01"

print(server_name[0])     # First character
print(server_name[-1])    # Last character
print(server_name[0:4])   # Slicing: prod
print(server_name[::-1])  # Reverse the string
```

## 2. String Methods: `upper()`, `lower()`, `title()`

**Tasks:**
- Convert the string to uppercase.
- Convert it to lowercase.
- Convert the first letter of each word to uppercase.

```python
environment = "production server monitoring"

# Write your code below

print(environment.upper())
print(environment.lower())
print(environment.title())

```

## 3. `split()` and `join()`

**Tasks:**
- Split the string using the comma.
- Print only the error message.
- Join the resulting parts using `" | "` as the separator.

```python
log = "ERROR,2026-10-19,Database connection failed"

# Write your code below

print(log.split(","))
print(log.split(",")[2])
print(" | ".join(log.split(",")))
```

## 4. `strip()`, `lstrip()`, `rstrip()`

**Tasks:**
- Remove spaces from both sides.
- Remove only leading spaces.
- Remove only trailing spaces.

```python
server = "   prod-api-01   "

# Write your code below
print(server.strip())
print(server.lstrip())
print(server.rstrip())

```

## 5. `replace()` and `count()`

**Tasks:**
- Count how many times `"ERROR"` appears.
- Replace `"ERROR"` with `"WARNING"`.
- Count how many times `"failed"` appears.

```python
log = "ERROR: API failed. ERROR: Database failed. ERROR: Timeout."

# Write your code below

print(log.count("ERROR"))
print(log.replace("ERROR" , "WARNING"))
print(log.count("failed"))

```

## 6. `startswith()` and `endswith()`

**Tasks:**
- Print only filenames starting with `"prod"`.
- Print only filenames ending with `".tf"`.
- Count how many files start with `"prod"`.

```python
files = [
    "prod.tf",
    "dev.tf",
    "prod.yaml",
    "test.py",
    "prod.json"
]

# Write your code below
prodfile = []
nonprod = []

for i in files:
    if i.startswith("prod"):
        prodfile.append(i)
        
    if i.endswith(".tf"):
        nonprod.append(i)
        
        
print(f"filenames startswith prod are {prodfile}") 
print(f"filenames ending with .tf are {nonprod}") 
print(len(prodfile))

```

## 7. `find()`, `index()` and `in`

**Tasks:**
- Check whether `"timeout"` exists in the log.
- Find the position of `"database"`.
- Find the position of `"WARNING"` using `find()` and observe the result.

```python
log = "ERROR: Connection timeout while accessing database"

# Write your code below

print(log.find("database"))   # 41
print(log.index("database"))  # 41
print("timeout" in log)       # True

print(log.find("WARNING"))    # -1
print("WARNING" in log)       # False
# log.index("WARNING")        # Raises ValueError

```

## 8. f-Strings and String Formatting

**Tasks:**
- Print a message containing the server name, CPU usage, and status.
- Print the CPU usage with a `%` symbol.
- Print a message such as `CRITICAL: prod-api-01 is using 92% CPU`.

```python
server = "prod-api-01"
cpu = 92
status = "CRITICAL"

# Write your code below


print(f" {server} {cpu} {status} ")
print(f"{cpu}%")
print(f"{status}: {server} is using {cpu}% CPU ")
```

## Bonus Challenge — Real-World DevOps Log Parsing

**Tasks:**
1. Extract the date.
2. Extract the log level (`ERROR`).
3. Extract the server name (`prod-api-01`).
4. Extract the CPU usage as an integer (`92`).
5. Print a warning if CPU usage is 80 or higher.

```python
log = "2026-10-19 10:30:15 ERROR [prod-api-01] CPU usage reached 92%"

# Write your code below

parts = log.split(" ")

# 1. Extract the date
date = parts[0]

# 2. Extract the log level
level = parts[2]

# 3. Extract the server name
server = parts[3].strip("[]")

# 4. Extract CPU usage as an integer
cpu = int(parts[7].replace("%", ""))

print(f"Date: {date}")
print(f"Log level: {level}")
print(f"Server: {server}")
print(f"CPU usage: {cpu}%")

# 5. Check CPU usage
if cpu >= 80:
    print(f"WARNING: {server} CPU usage is {cpu}%")
else:
    print(f"OK: {server} CPU usage is {cpu}%")

```

## Practice Instructions

Complete Task 1 first and share your code for review. Fix any mistakes before moving to Task 2. Continue until you complete all eight tasks and the bonus challenge.