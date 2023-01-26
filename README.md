# CuckooHashing

Python3 Cuckoo Hash Table

This uses 2 separate arrays, each of length **init_size**

## CuckooHash public member functions definitions

### init()
initializes the cuckoo hash tables as a list with dimensions 2 by **init_sizes**, and fills both tables with **None** entries.
					**CYCLE_THRESHOLD** denotes the threshold for the number of evictions for detecting cycles in the **insert()** method.

### get_table_contents()
will be used during testing to check the correctness of the table contents.

### hash_func()
takes as input the key and the table id (0 or 1), and returns the hash value for that key in the specified table.

### insert(key)
insert an item with the specified key to the cuckoo hash. if a cycle is found during the insertion, stop and return False. otherwise return True after inserting the item. if a cycle is found, the function only return False.

### lookup(key)
return True if an item with the specified key exists in the cuckoo hash, and False otherwise.

### delete(key)
delete item with the specified key from the cuckoo hash and replace it with a None entry.

### rehash(new_table_size)
updates tables such that both tables are of size **new_table_size**, and all existing elements in the old tables are rehashed to their new locations.


## CuckooHash Performance
Cuckoo hashing is very efficient for searching. It has a worst case lookup time of O(1)! This is a vast improvement from many hash table implementations with a worst case of O(N).

When inserting into a cuckoo hash table, it's important to consider all of the potential problems that may arise. An infinite loop may be encountered while cuckoo hashing. This occurs if there are 2 or more items that are continuously displacing one another and are never able to find a permanent position. There should be a certain threshold - **CYCLE_THRESHOLD** - in the code to detect these infinite loops and deal with them. Once detected, a new hash function should be used to rehash the entire contents of the table.
