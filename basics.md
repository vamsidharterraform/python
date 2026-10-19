


Remember
- Mutable: Can be changed after creation — list, dict, set.
- Immutable: Cannot be changed after creation — int, float, bool, str, tuple, range.
- Sequence: Ordered items accessible by index — str, list, tuple, range.
- Dictionary: Stores key-value pairs and preserves insertion order.
- Set: Stores unique values without a guaranteed positional order.
- Map: Returns an iterator that applies a function to each item; use list(map(...)) to convert its results into a list.# Python Data Types — Quick Reference

| Data Type | Example | Mutable / Immutable | Ordered / Sequence? |
|---|---|---|---|
| `int` | `10` | Immutable | No |
| `float` | `2.5` | Immutable | No |
| `bool` | `True` | Immutable | No |
| `str` | `"hello"` | Immutable | Yes — Sequence |
| `list` | `[10, 20]` | Mutable | Yes — Sequence |
| `tuple` | `(10, 20)` | Immutable | Yes — Sequence |
| `dict` | `{"cpu": 80}` | Mutable | Ordered by insertion; not a sequence |
| `set` | `{10, 20}` | Mutable | Unordered; not a sequence |
| `range` | `range(5)` | Immutable | Yes — Sequence |
| `map` | `map(int, ["1", "2"])` | Iterator | Not a sequence |

## How to Add Values

```python
# List — append an item
my_list.append(30)

# String — create a new string
my_string += " world"

# Tuple — create a new tuple
my_tuple += (30,)

# Dictionary — add or update a key-value pair
my_dict["memory"] = 80

# Set — add a unique item
my_set.add(30)

# Map — convert the iterator results into a list
numbers = list(map(int, ["1", "2"]))
```

## Remember

- **Mutable:** Can be modified after creation — `list`, `dict`, `set`.
- **Immutable:** Cannot be modified after creation — `int`, `float`, `bool`, `str`, `tuple`, `range`.
- **Sequence:** Ordered collection that supports indexing — `str`, `list`, `tuple`, `range`.
- **Dictionary:** Stores key-value pairs and preserves insertion order.
- **Set:** Stores unique values without a guaranteed positional order.
- **Map:** Returns an iterator that applies a function to each item.