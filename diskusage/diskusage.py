import subprocess

try:
    usage = subprocess.run(
        ['df', '-h', '/'],
        capture_output=True,
        text=True,
        check=True
    )

    print(usage.stdout)

    print("After splitting")

    lines = usage.stdout.splitlines()
    print(lines)

    print("After splitting line wise")

    linessplit1 = lines[1].split()
    print(linessplit1)

    usage = int(linessplit1[4].replace("%", ""))

    print("Disk usage:", usage, "%")

    if usage >= 85:
        print("WARNING: Disk usage is greater than 85%:", usage, "%")
    else:
        print("OK: Disk usage is less than 85%:", usage, "%")

except subprocess.CalledProcessError as e:
    print("Failed to execute df command:", e)

except IndexError:
    print("Unable to parse disk usage from df output")

except ValueError:
    print("Unable to convert disk usage to a number")

except Exception as e:
    print("Unexpected error:", e)