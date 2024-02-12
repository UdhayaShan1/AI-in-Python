# https://leetcode.com/problems/predict-the-winner/


# Example input
nums = [1, 5, 2]
#nums = [1, 5, 233, 7]
total_sum = sum(nums)

#Iteration #1, passes but too slow, exponential time complexity
def minimax(i, j, current, maximiser):
    if i > j:
        return 1 if current >= total_sum - current else -1
    if maximiser:
        return max(minimax(i + 1, j, current+nums[i], not maximiser), minimax(i, j - 1, current+nums[j], not maximiser))
    else:
        return min(minimax(i + 1, j, current, not maximiser), minimax(i, j - 1, current, not maximiser))


#print(minimax(0, len(nums)-1, 0, True) == 1)
    
#Iteration #2, passes, faster than Iteration #1. Linear time complexity
dp = {}
def minimax2(i, j, current, maximiser):
    if i > j:
        return 1 if current >= total_sum - current else -1
    key = (i, j, current, maximiser)
    if key in dp:
        return dp[key]
    if maximiser:
        dp[key] = max(minimax(i + 1, j, current+nums[i], not maximiser), minimax(i, j - 1, current+nums[j], not maximiser))
    else:
        dp[key] = min(minimax(i + 1, j, current, not maximiser), minimax(i, j - 1, current, not maximiser))
    return dp[key]

#print(minimax2(0, len(nums)-1, 0, True) == 1)