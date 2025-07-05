def insertion_sort_list(unsorted_list):
    for current_index in range(1, len(unsorted_list)):
        pointer_to_element_to_insert = current_index
        while pointer_to_element_to_insert > 0 and unsorted_list[pointer_to_element_to_insert - 1] > unsorted_list[pointer_to_element_to_insert]:
            unsorted_list[pointer_to_element_to_insert], unsorted_list[pointer_to_element_to_insert - 1] = unsorted_list[pointer_to_element_to_insert - 1], unsorted_list[pointer_to_element_to_insert]
            pointer_to_element_to_insert -= 1

    return unsorted_list

print("--- Starting Manual Tests for Insertion Sort ---")

# Test 1: Empty List
list_test_is01 = []
expected_is01 = []
result_is01 = insertion_sort_list(list_test_is01.copy())
print(f"\nTest 1 (Empty List):")
print(f"  Original: {list_test_is01}")
print(f"  Expected: {expected_is01}")
print(f"  Actual:   {result_is01}")
print(f"  PASSED: {result_is01 == expected_is01}")

# Test 2: Single Element List
list_test_is02 = [7]
expected_is02 = [7]
result_is02 = insertion_sort_list(list_test_is02.copy())
print(f"\nTest 2 (Single Element List):")
print(f"  Original: {list_test_is02}")
print(f"  Expected: {expected_is02}")
print(f"  Actual:   {result_is02}")
print(f"  PASSED: {result_is02 == expected_is02}")

# Test 3: Already Sorted List
list_test_is03 = [1, 2, 3, 4, 5]
expected_is03 = [1, 2, 3, 4, 5]
result_is03 = insertion_sort_list(list_test_is03.copy())
print(f"\nTest 3 (Already Sorted List):")
print(f"  Original: {list_test_is03}")
print(f"  Expected: {expected_is03}")
print(f"  Actual:   {result_is03}")
print(f"  PASSED: {result_is03 == expected_is03}")

# Test 4: Reverse Sorted List
list_test_is04 = [5, 4, 3, 2, 1]
expected_is04 = [1, 2, 3, 4, 5]
result_is04 = insertion_sort_list(list_test_is04.copy())
print(f"\nTest 4 (Reverse Sorted List):")
print(f"  Original: {list_test_is04}")
print(f"  Expected: {expected_is04}")
print(f"  Actual:   {result_is04}")
print(f"  PASSED: {result_is04 == expected_is04}")

# Test 5: List with Duplicate Elements
list_test_is05 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
expected_is05 = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
result_is05 = insertion_sort_list(list_test_is05.copy())
print(f"\nTest 5 (With Duplicates):")
print(f"  Original: {list_test_is05}")
print(f"  Expected: {expected_is05}")
print(f"  Actual:   {result_is05}")
print(f"  PASSED: {result_is05 == expected_is05}")

# Test 6: List with Negative Numbers
list_test_is06 = [-5, -1, -10, 0, 3]
expected_is06 = [-10, -5, -1, 0, 3]
result_is06 = insertion_sort_list(list_test_is06.copy())
print(f"\nTest 6 (With Negative Numbers):")
print(f"  Original: {list_test_is06}")
print(f"  Expected: {expected_is06}")
print(f"  Actual:   {result_is06}")
print(f"  PASSED: {result_is06 == expected_is06}")

# Test 7: Mixed List (Positive, Negative, Zero)
list_test_is07 = [0, -3, 5, -1, 2]
expected_is07 = [-3, -1, 0, 2, 5]
result_is07 = insertion_sort_list(list_test_is07.copy())
print(f"\nTest 7 (Mixed Numbers):")
print(f"  Original: {list_test_is07}")
print(f"  Expected: {expected_is07}")
print(f"  Actual:   {result_is07}")
print(f"  PASSED: {result_is07 == expected_is07}")

# Test 8: Large List (to check robustness)
list_test_is08 = [i for i in range(100, 0, -1)]
expected_is08 = list(range(1, 101))
result_is08 = insertion_sort_list(list_test_is08.copy())
print(f"\nTest 8 (Large List):")
print(f"  Original: [100, 99, ..., 1] (Omitted for brevity)")
print(f"  Expected: [1, 2, ..., 100] (Omitted for brevity)")
print(f"  Actual:   {result_is08[:5]}...{result_is08[-5:]}")
print(f"  PASSED: {result_is08 == expected_is08}")