
Experiment 9:

AIM: To implement all the function of a dictionary using hashing PROCEDURE: Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized.a Dictionary can be created by placing sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.

creating and inserting a key in a dictionary: Key value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’. Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples, but the key-values can be repeated and be of any type.

Deleting a key from dictionary: del keyword can be used to inplace delete the key that is present in the dictionary. One drawback that can be thought of using this is that is raises an exception if the key is not found and hence non-existence of key has to be handled.

Searching a keys by value in a dictionary: The dictionary object has an items() method which returns a list of all the items with their values, i.e., in the form of key-pairs. So, we’ll call this function and then traverse the sequence to search our desired value. If the target value matches with some of the items in the dict object, then we’ll add the key to a temp list.
