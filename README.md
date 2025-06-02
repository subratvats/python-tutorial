# python-tutorial
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