# When the number of steps in an algorithm grows at the same rate as its input size, it's classified as O(n)
# For example, our find_max algorithm from is O(n)
def find_max(nums):
    max  = float("-inf")
    for num in nums:
        if max < num:
            max = num
    return max

nums01 = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
nums02 = [12, 12, 12]
nums03 = [-1, -2, -3]

print(find_max(nums01))
print(find_max(nums02))
print(find_max(nums03))