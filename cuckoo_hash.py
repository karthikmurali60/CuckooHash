# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List

class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[int]]:
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	# insert() inserts a given key in the CuckooHash.
	# 
	# inputs --> key (type : int) - the key to be inserted in the hash.
	# 
	# output --> boolean - if the key is inserted successfully, the function
	# 			 returns True. If there is a cycle, then the key will not be
	# 			 inserted and the function returns False.
	def insert(self, key: int) -> bool:
		# Start the insert operation in the first table i.e table[0].
		table_id = 0

		for _ in range(self.CYCLE_THRESHOLD + 1):
			position = self.hash_func(key, table_id)

			# If there is no element present at the hash position for
			# the input key, store the key in that position and return.
			if self.tables[table_id][position] == None:
				self.tables[table_id][position] = key
				return True

			# If there is already an element at the hash position for
			# the input key, insert the input key in the current position
			# and deal with the displaced element in the next iteration. 
			self.tables[table_id][position], key = key, self.tables[table_id][position]
			table_id = 1 if table_id == 0 else 0

		# If this point is reached, then there is a cycle during insert.
		return False

	# lookup() is used to find a given key in the CuckooHash.
	# 
	# inputs --> key (type: int) - the key to be searched in the hash.
	# 
	# output --> boolean - True if the key is present in the hash else False.
	def lookup(self, key: int) -> bool:
		position1 = self.hash_func(key, 0)
		if self.tables[0][position1] and self.tables[0][position1] == key:
			return True

		position2 = self.hash_func(key, 1)
		if self.tables[1][position2] and self.tables[1][position2] == key:
			return True
		
		return False

	# delete() deletes a given key from the CuckooHash.
	# 
	# inputs --> key (type: int) - the key to be deleted from the hash.
	# 
	# output --> None - if the key is present in the hash, it is deleted and
	# 			 the None is placed in its position, else nothing is done.
	def delete(self, key: int) -> None:
		position1 = self.hash_func(key, 0)
		if self.tables[0][position1] != None and self.tables[0][position1] == key:
			self.tables[0][position1] = None
		
		position2 = self.hash_func(key, 1)
		if self.tables[1][position2] != None and self.tables[1][position2] == key:
			self.tables[1][position2] = None

	# rehash() is used to alter the size of the table and all the keys is 
	# re-inserted into the new table using new hash functions.
	# 
	# inputs --> new_table_size (type : int) - the size of the new table to
	#   		 be created for rehashing
	# 
	# output --> None - the existing elements are inserted into the rehashed table.
	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line

		new_table = CuckooHash(new_table_size)
		new_table.__num_rehashes = self.__num_rehashes

		for i in range(2):
			for j in range(len(self.tables[0])):
				if self.tables[i][j] != None:
					new_table.insert(self.tables[i][j])

		self.tables = new_table.tables

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
