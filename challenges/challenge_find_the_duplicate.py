def find_duplicate(nums):
    index = 0

    nums.sort()

    for num in nums[:-1]:
        index += 1
        if not isinstance(num, int) or num < 0:
            return False
        if num == nums[index]:
            return num
    return False
