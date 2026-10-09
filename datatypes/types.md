# Python Data Types — Complete Cheat Sheet

## 1. Python Data Types

| Data Type | Example Declaration | Nature |
|---|---|---|
| String (`str`) | `a = "hello"` | Immutable |
| Integer (`int`) | `a = 100` | Immutable |
| Float (`float`) | `a = 10.5` | Immutable |
| Boolean (`bool`) | `a = True` | Immutable |
| List (`list`) | `a = ["apple", "banana"]` | Mutable |
| Tuple (`tuple`) | `a = ("apple", "banana")` | Immutable |
| Set (`set`) | `a = {"apple", "banana"}` | Mutable |
| Dictionary (`dict`) | `a = {"name": "Vamsi", "age": 30}` | Mutable |
| None (`NoneType`) | `a = None` | Immutable |

**Mutable:** An object's contents can be changed after creation.

**Immutable:** An object's contents cannot be changed after creation. Reassigning the variable is still allowed.

---

## 2. String (`str`)

Stores text. Use single or double quotes.

```python
a = "hello"
b = 'python'
c = "12345"

print(type(a))  # <class 'str'>
```

**Nature: Immutable**

```python
a = "hello"

# a[0] = "H"  # TypeError

a = "Hello"    # Valid: assigns a new string
```

---

## 3. Integer (`int`)

Stores whole numbers.

```python
a = 10
b = -25
c = 0

print(type(a))  # <class 'int'>
```

**Nature: Immutable**

```python
a = 10
a = 20  # Reassignment is allowed
```

---

## 4. Float (`float`)

Stores numbers with decimal points.

```python
a = 10.5
b = 3.14
c = -2.5

print(type(a))  # <class 'float'>
```

**Nature: Immutable**

---

## 5. Boolean (`bool`)

Stores either `True` or `False`.

```python
a = True
b = False

print(type(a))  # <class 'bool'>
```

**Nature: Immutable**

Example:

```python
disk_usage = 90

if disk_usage >= 85:
    alert = True
else:
    alert = False
```

---

## 6. List (`list`)

Stores multiple values in an ordered collection. Allows duplicates and different data types.

```python
a = ["apple", "banana", "orange"]
b = [10, 20, 30]
c = ["Vamsi", 30, True, 10.5]
d = []  # Empty list
```

**Nature: Mutable**

```python
a = ["apple", "banana"]

a.append("orange")  # Add an item
a[0] = "mango"      # Update an item

print(a)
# ['mango', 'banana', 'orange']
```

DevOps example:

```python
branches = ["main", "feature1"]
branches.append("feature2")
```

---

## 7. Tuple (`tuple`)

Stores multiple values in an ordered collection. Similar to a list, but cannot be modified in place.

```python
a = ("apple", "banana", "orange")
b = (10, 20, 30)
c = ("Vamsi", 30, True)
d = ()       # Empty tuple
e = (10,)    # One-element tuple
```

**Nature: Immutable**

```python
a = ("apple", "banana")

# a[0] = "mango"  # TypeError
```

**Remember:** `(10,)` is a one-element tuple. `(10)` is an integer.

---

## 8. Set (`set`)

Stores unique values. Sets do not support indexing and do not guarantee a fixed positional order.

```python
a = {"apple", "banana", "orange"}
b = {10, 20, 30}
c = {10, 10, 20, 30}
d = set()  # Empty set
```

**Nature: Mutable**

```python
a = {"apple", "banana"}

a.add("orange")
a.remove("apple")

print(a)
```

The duplicate `10` in `c` is stored only once.

**Remember:** `{}` creates an empty dictionary, not an empty set. Use `set()`.

---

## 9. Dictionary (`dict`)

Stores information as **key-value pairs**.

```python
a = {
    "name": "Vamsi",
    "age": 30,
    "role": "DevOps Engineer"
}

b = {}  # Empty dictionary
```

**Nature: Mutable**

```python
a = {"name": "Vamsi", "age": 30}

a["age"] = 31
a["city"] = "Hyderabad"

print(a)
```

Access values using keys:

```python
print(a["name"])
print(a["age"])
```

DevOps example — parsing an API response:

```python
branch = {
    "name": "feature1",
    "commit": {"id": "abc123"}
}

print(branch["name"])
print(branch["commit"]["id"])
```

---

## 10. None (`NoneType`)

Represents the absence of a value.

```python
a = None

print(type(a))  # <class 'NoneType'>
```

**Nature: Immutable**

Example:

```python
result = None

if result is None:
    print("No result available")
```

---

# 11. Mutable vs. Immutable

## Mutable Example

```python
a = [10, 20, 30]
a.append(40)

print(a)
# [10, 20, 30, 40]
```

The existing list is modified.

## Immutable Example

```python
a = "hello"

# a[0] = "H"  # Error

a = "Hello"  # Reassigns a to a new string
```

The original string cannot be changed in place.

**Important:** Reassigning a variable is not the same as modifying the object it refers to.

---

# 12. Quick Interview Reference

| Type | Ordered? | Allows Duplicates? | Mutable? |
|---|---|---|---|
| String | Yes | Yes | No |
| Integer | N/A | N/A | No |
| Float | N/A | N/A | No |
| Boolean | N/A | N/A | No |
| List | Yes | Yes | Yes |
| Tuple | Yes | Yes | No |
| Set | No fixed positional order | No | Yes |
| Dictionary | Yes (insertion order) | Keys: No; values: Yes | Yes |
| None | N/A | N/A | No |

**Note:** Dictionary keys must be unique. Dictionary values may repeat.

---

# 13. Five Important Types for DevOps

Prioritize these for Python scripting:

1. **String:** Parse log lines, API messages, and command output.
2. **Integer:** Compare disk usage, CPU percentages, and thresholds.
3. **List:** Store branch names, server names, and process results.
4. **Dictionary:** Read JSON responses from GitLab and AWS APIs.
5. **Boolean:** Track whether a check passed or failed.

Example:

```python
disk_usage = 85
server_name = "web-server-01"
alerts = ["High disk usage", "High memory"]
server = {
    "name": "web-server-01",
    "status": "running"
}
is_healthy = False
```

These data types are the foundation for writing practical AWS DevOps automation scripts.
