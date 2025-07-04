
## Python Formatted String Notes

- **Definition**: Formatted strings allow embedding expressions inside string literals.
- **f-Strings (Python 3.6+)**:
    ```python
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    ```
- **Modifiers/Format Specifiers**:
    - `{value:.2f}`: Format float with 2 decimal places.
    - `{value:>10}`: Right-align in a field of width 10.
    - `{value:<10}`: Left-align in a field of width 10.
    - `{value:^10}`: Center-align in a field of width 10.
    - `{value:,}`: Add thousands separator.
    - `{value:%}`: Percentage format.
- **Other Methods**: `str.format()` and `%` formatting (older styles).

## Python List Notes

- **Definition**: A list is an ordered, mutable collection of items.
- **Syntax**:
    ```python
    my_list = [1, 2, 3, 'a', 'b']
    ```
- **Accessing Elements**:
    ```python
    first = my_list[0]
    last = my_list[-1]
    ```
- **Adding Items**:
    - `append(x)`: Add to end.
    - `insert(i, x)`: Insert at index.
    - `extend(iterable)`: Add multiple items.
- **Removing Items**:
    - `remove(x)`: Remove first occurrence.
    - `pop(i)`: Remove and return item at index.
    - `clear()`: Remove all items.
- **Common Methods**:
    - `sort()`: Sort list in place.
    - `reverse()`: Reverse list in place.
    - `count(x)`: Count occurrences of x.
    - `index(x)`: Find index of x.
- **Iteration**:
    ```python
    for item in my_list:
        print(item)
    ```
- **Key Features**:
    - Supports mixed data types.
    - Allows duplicates.
    - Lists are mutable and dynamic.
## Python Dictionary Notes

- **Definition**: A dictionary is an unordered collection of key-value pairs.
- **Syntax**:  
    ```python
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    ```
- **Accessing Values**:  
    ```python
    value = my_dict['key1']
    ```
- **Adding/Updating Items**:  
    ```python
    my_dict['key3'] = 'value3'
    ```
- **Removing Items**:  
    ```python
    del my_dict['key1']
    my_dict.pop('key2')
    ```
- **Common Methods**:
    - `keys()`: Returns all keys.
    - `values()`: Returns all values.
    - `items()`: Returns all key-value pairs.
- **Iteration**:
    ```python
    for key, value in my_dict.items():
            print(key, value)
    ```
- **Key Features**:
    - Keys must be immutable (e.g., strings, numbers, tuples).
    - Values can be any data type.
    - Dictionaries are mutable and dynamic.