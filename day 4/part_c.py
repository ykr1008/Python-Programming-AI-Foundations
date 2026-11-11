import time

my_list = list(range(100_000))
my_set = set(my_list)

# Time the list lookup
start = time.perf_counter()
99999 in my_list
list_time = time.perf_counter() - start

# Time the set lookup
start = time.perf_counter()
99999 in my_set
set_time = time.perf_counter() - start

print(f"List lookup time: {list_time:.8f} seconds")
print(f"Set lookup time:  {set_time:.8f} seconds")