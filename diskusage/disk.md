# AWS DevOps Python Practice — Task 1: Disk Usage Monitor

## Objective

Create a Python script that checks the disk usage of the Linux root filesystem and generates a warning when disk usage is high.

## File

Create:

```text
/root/scripts/disk_check.py
```

## Requirements

Write a Python script that:

1. Imports the `subprocess` module.
2. Executes the following Linux command using `subprocess`:

   ```bash
   df -h /
   ```

3. Reads the output of the command.
4. Extracts the disk usage percentage from the output.

   For example, if the command returns:

   ```text
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/nvme0n1p1   20G   13G    7G  65% /
   ```

   Extract:

   ```text
   65%
   ```

5. Prints the disk usage:

   ```text
   Disk Usage: 65%
   ```

6. Checks whether the disk usage is greater than or equal to 80%.

   If disk usage is 80% or higher, print:

   ```text
   WARNING: Disk usage is high: 85%
   ```

   If disk usage is below 80%, print:

   ```text
   OK: Disk usage is normal: 65%
   ```

7. Uses `try/except` to handle errors when executing the `df` command.

## Expected Output

### Scenario 1 — Normal Disk Usage

If the disk usage is 65%:

```text
Disk Usage: 65%
OK: Disk usage is normal: 65%
```

### Scenario 2 — High Disk Usage

If the disk usage is 85%:

```text
Disk Usage: 85%
WARNING: Disk usage is high: 85%
```

## Restrictions

For this exercise, use only:

- `subprocess`
- Variables
- `if/else`
- `try/except`
- Basic string/list operations

Do **not** use:

- `psutil`

## Starting Hint

You can start with:

```python
import subprocess

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

## Your Goal

Complete the entire script yourself.

Do not worry about making it perfect on the first attempt. Focus on this flow:

```text
Run command
    ↓
Get output
    ↓
Extract Use%
    ↓
Convert percentage to integer
    ↓
Check >= 80
    ↓
Print WARNING or OK
    ↓
Handle errors
```