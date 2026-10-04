import time

with open("app.log", "r") as file:

    file.seek(0, 2)

    while True:

        line = file.readline()

        if line:

            if "ERROR" in line:
                print("ERROR:", line.strip())

            elif "WARNING" in line:
                print("WARNING:", line.strip())

        else:
            time.sleep(1)