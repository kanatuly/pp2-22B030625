def spy_game(nums):
    for i in range(2, len(nums)):
        if nums[i-2] == 0 and nums[i-1] == 0 and nums[i] == 7:
            return True
    return False


print(spy_game(list(map(int, input().split()))))