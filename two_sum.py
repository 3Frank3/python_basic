# Find two numbers in a list that add up to a specific target


nums = [3,2,4]
target = input("Enter target: ")
target = int(target)

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

d = two_sum(nums, target)
print(d) # [0,1]