nums = [1, 5, 2]
total_sum = sum(nums)


# We will improve on Iteration #2
# Iteration #2.5, with alpha-beta pruning but turns out to be slightly slower..
dp = {}
def minimax3(i, j, current, maximiser, alpha, beta):
    if i > j:
        #1 to mark maximiser's victory, -1 to mark the L.
        return 1 if current >= total_sum - current else -1
    key = (i, j, current, maximiser)
    if key in dp:
        return dp[key]
    if maximiser:
        dp[key] = max(minimax3(i + 1, j, current+nums[i], not maximiser, alpha, beta),
                      minimax3(i, j - 1, current+nums[j], not maximiser, alpha, beta))
        alpha = max(alpha, dp[key])
        if dp[key] >= beta:
            return dp[key]
    else:
        dp[key] = min(minimax3(i + 1, j, current, not maximiser, alpha, beta),
                      minimax3(i, j - 1, current, not maximiser, alpha, beta))
        beta = min(beta, dp[key])
        if dp[key] <= alpha:
            return dp[key]

    return dp[key]

print(minimax3(0, len(nums)-1, 0, True, -float('inf'), float('inf')) == 1)
