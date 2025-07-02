# O(n^2) grows in complexity much more rapidly. That said, for small and medium input sizes, these algorithms can still be very useful.
# A common reason an algorithm falls into O(n^2) is by using a nested loop, where the number of iterations of each loop is equal to the number of items in the input:
def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if f"{first_name} {last_name}" == full_name:
                return True
    return False

first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Brown"]

print(does_name_exist(first_names, last_names, "Alice Smith")) 

print(does_name_exist(first_names, last_names, "Charlie Brown"))

print(does_name_exist(first_names, last_names, "Bob Davis")) 

print(does_name_exist(first_names, last_names, "David Johnson")) 

print(does_name_exist(first_names, last_names, "Alice  Smith")) 