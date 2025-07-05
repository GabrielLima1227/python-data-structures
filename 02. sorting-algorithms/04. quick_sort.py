def quick_sort_in_place(data_list, start_index, end_index):
    if start_index < end_index:
        pivot_final_position = partition_list(data_list, start_index, end_index)
        quick_sort_in_place(data_list, start_index, pivot_final_position - 1)
        quick_sort_in_place(data_list, pivot_final_position + 1, end_index)


def partition_list(data_list, start_index, end_index):
    pivot_value = data_list[end_index]
    store_index = start_index
    for current_element_index in range(start_index, end_index):
        if data_list[current_element_index] < pivot_value:
            data_list[store_index], data_list[current_element_index] = data_list[current_element_index], data_list[store_index]
            store_index += 1
    data_list[store_index], data_list[end_index] = data_list[end_index], data_list[store_index]
    return store_index

print("--- Starting Manual Tests for Quick Sort (In-Place) ---")

def sort_and_return_copy(input_list):
    temp_list = input_list.copy() 
    if temp_list: 
        quick_sort_in_place(temp_list, 0, len(temp_list) - 1)
    return temp_list

# Test 1: Empty List
test_list_qs01 = []
expected_qs01 = []
result_qs01 = sort_and_return_copy(test_list_qs01)
print(f"\nTest 1 (Empty List):")
print(f"  Original: {test_list_qs01}")
print(f"  Expected: {expected_qs01}")
print(f"  Actual:   {result_qs01}")
print(f"  PASSED: {result_qs01 == expected_qs01}")

# Test 2: Single Element List
test_list_qs02 = [7]
expected_qs02 = [7]
result_qs02 = sort_and_return_copy(test_list_qs02)
print(f"\nTest 2 (Single Element List):")
print(f"  Original: {test_list_qs02}")
print(f"  Expected: {expected_qs02}")
print(f"  Actual:   {result_qs02}")
print(f"  PASSED: {result_qs02 == expected_qs02}")

# Test 3: Already Sorted List
test_list_qs03 = [1, 2, 3, 4, 5]
expected_qs03 = [1, 2, 3, 4, 5]
result_qs03 = sort_and_return_copy(test_list_qs03)
print(f"\nTest 3 (Already Sorted List):")
print(f"  Original: {test_list_qs03}")
print(f"  Expected: {expected_qs03}")
print(f"  Actual:   {result_qs03}")
print(f"  PASSED: {result_qs03 == expected_qs03}")

# Test 4: Reverse Sorted List
test_list_qs04 = [5, 4, 3, 2, 1]
expected_qs04 = [1, 2, 3, 4, 5]
result_qs04 = sort_and_return_copy(test_list_qs04)
print(f"\nTest 4 (Reverse Sorted List):")
print(f"  Original: {test_list_qs04}")
print(f"  Expected: {expected_qs04}")
print(f"  Actual:   {result_qs04}")
print(f"  PASSED: {result_qs04 == expected_qs04}")

# Test 5: List with Duplicate Elements
test_list_qs05 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
expected_qs05 = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
result_qs05 = sort_and_return_copy(test_list_qs05)
print(f"\nTest 5 (With Duplicates):")
print(f"  Original: {test_list_qs05}")
print(f"  Expected: {expected_qs05}")
print(f"  Actual:   {result_qs05}")
print(f"  PASSED: {result_qs05 == expected_qs05}")

# Test 6: List with Negative Numbers
test_list_qs06 = [-5, -1, -10, 0, 3]
expected_qs06 = [-10, -5, -1, 0, 3]
result_qs06 = sort_and_return_copy(test_list_qs06)
print(f"\nTest 6 (With Negative Numbers):")
print(f"  Original: {test_list_qs06}")
print(f"  Expected: {expected_qs06}")
print(f"  Actual:   {result_qs06}")
print(f"  PASSED: {result_qs06 == expected_qs06}")

# Test 7: Mixed List (Positive, Negative, Zero)
test_list_qs07 = [0, -3, 5, -1, 2]
expected_qs07 = [-3, -1, 0, 2, 5]
result_qs07 = sort_and_return_copy(test_list_qs07)
print(f"\nTest 7 (Mixed Numbers):")
print(f"  Original: {test_list_qs07}")
print(f"  Expected: {expected_qs07}")
print(f"  Actual:   {result_qs07}")
print(f"  PASSED: {result_qs07 == expected_qs07}")

# Test 8: Large List (to check robustness)
test_list_qs08 = [i for i in range(100, 0, -1)] 
expected_qs08 = list(range(1, 101))
result_qs08 = sort_and_return_copy(test_list_qs08)
print(f"\nTest 8 (Large List):")
print(f"  Original: [100, 99, ..., 1] (Omitted for brevity)")
print(f"  Expected: [1, 2, ..., 100] (Omitted for brevity)")
print(f"  Actual:   {result_qs08[:5]}...{result_qs08[-5:]}")
print(f"  PASSED: {result_qs08 == expected_qs08}")

print("\n--- Manual Tests Completed ---")