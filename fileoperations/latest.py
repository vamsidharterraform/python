latest_error = None

with open("app.log", "r") as inputfile:
    for line in inputfile:
        if "ERROR" in line:
            # print(line)
            latest_error = line.strip()

if latest_error:
    print("Latest ERROR:")
    print(latest_error)
else:
    print("No ERROR found")

# print(latest_error)

# ddddddddddddddddddddddddddddddddddddddddddddd
from datetime import datetime

latest_error = None
latest_time = None

with open("app.log", "r") as inputfile:

    for line in inputfile:

        if "ERROR" in line:

            timestamp = line[:19]

            log_time = datetime.strptime(
                timestamp,
                "%Y-%m-%d %H:%M:%S"
            )

            if latest_time is None or log_time > latest_time:
                latest_time = log_time
                latest_error = line.strip()

if latest_error:
    print("Latest ERROR:")
    print(latest_error)
else:
    print("No ERROR found")


# =-====================================

error_count = 0

with open("app.log", "r") as inputfile:

    for line in inputfile:

        if "ERROR" in line:
            error_count += 1

print("Total errors:", error_count)