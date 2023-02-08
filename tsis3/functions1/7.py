def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    return False


print(has_33(list(map(int, input().split()))))