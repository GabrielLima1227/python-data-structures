# The Bubble Sort algorithm works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which means the list is sorted.

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1,end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1], nums[i] = nums[i], temp
                swapping = True
        end -= 1
    return nums

nums = [1,3,5,7,9,2,4,6,8,10]
print(bubble_sort(nums))