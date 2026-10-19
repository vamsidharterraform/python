
Python Data Types — Quick Reference
Data type	Example	Mutable / Immutable	Ordered / Sequence?
int	10	Immutable	No
float	2.5	Immutable	No
bool	True	Immutable	No
str	"hello"	Immutable	Yes, sequence
list	[10, 20]	Mutable	Yes, sequence
tuple	(10, 20)	Immutable	Yes, sequence
dict	{"cpu": 80}	Mutable	Ordered by insertion; not a sequence
set	{10, 20}	Mutable	Unordered; not a sequence
range	range(5)	Immutable	Yes, sequence
map	map(int, ["1", "2"])	Iterator	Not a sequence





How to add values

my_list.append(30)          # List: adds one item
my_string += " world"       # String: creates a new string
my_tuple += (30,)           # Tuple: creates a new tuple
my_dict["memory"] = 80      # Dictionary: adds or updates a key
my_set.add(30)              # Set: adds a unique item

Remember: Lists, dictionaries, and sets are mutable. Strings and tuples are immutable.
Note: Python's map() is an iterator, not a mutable collection like a list.

Remember
- Mutable: Can be changed after creation — list, dict, set.
- Immutable: Cannot be changed after creation — int, float, bool, str, tuple, range.
- Sequence: Ordered items accessible by index — str, list, tuple, range.
- Dictionary: Stores key-value pairs and preserves insertion order.
- Set: Stores unique values without a guaranteed positional order.
- Map: Returns an iterator that applies a function to each item; use list(map(...)) to convert its results into a list.