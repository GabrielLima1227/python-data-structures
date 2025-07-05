def merge_sort_list(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    middle_index = len(unsorted_list) // 2
    left_half = merge_sort_list(unsorted_list[:middle_index])
    right_half = merge_sort_list(unsorted_list[middle_index:])
    return merge_two_sorted_lists(left_half, right_half)

def merge_two_sorted_lists(list1, list2):
    merged_result = []
    index_list1 = 0
    index_list2 = 0

    while index_list1 < len(list1) and index_list2 < len(list2):
        if list1[index_list1] <= list2[index_list2]:
            merged_result.append(list1[index_list1])
            index_list1 += 1
        else:
            merged_result.append(list2[index_list2])
            index_list2 += 1

    while index_list1 < len(list1):
        merged_result.append(list1[index_list1])
        index_list1 += 1

    while index_list2 < len(list2):
        merged_result.append(list2[index_list2])
        index_list2 += 1

    return merged_result

print("--- Starting Manual Tests ---")

list_test01 = []
expected_01 = []
result_01 = merge_sort_list(list_test01)
print(f"\nTest 1 (Empty List):")
print(f"  Original: {list_test01}")
print(f"  Expected: {expected_01}")
print(f"  Actual:   {result_01}")
print(f"  PASSED: {result_01 == expected_01}")

list_test02 = [7]
expected_02 = [7]
result_02 = merge_sort_list(list_test02)
print(f"\nTest 2 (Single Element List):")
print(f"  Original: {list_test02}")
print(f"  Expected: {expected_02}")
print(f"  Actual:   {result_02}")
print(f"  PASSED: {result_02 == expected_02}")

list_test03 = [1, 2, 3, 4, 5]
expected_03 = [1, 2, 3, 4, 5]
result_03 = merge_sort_list(list_test03)
print(f"\nTest 3 (Already Sorted List):")
print(f"  Original: {list_test03}")
print(f"  Expected: {expected_03}")
print(f"  Actual:   {result_03}")
print(f"  PASSED: {result_03 == expected_03}")

list_test04 = [5, 4, 3, 2, 1]
expected_04 = [1, 2, 3, 4, 5]
result_04 = merge_sort_list(list_test04)
print(f"\nTest 4 (Reverse Sorted List):")
print(f"  Original: {list_test04}")
print(f"  Expected: {expected_04}")
print(f"  Actual:   {result_04}")
print(f"  PASSED: {result_04 == expected_04}")