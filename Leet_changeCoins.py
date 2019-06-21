#
def coinChange(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

    return [dp[amount], -1][dp[amount] == MAX]

# def coinChange(coins, amount):
#     Max = float('inf')
#     nums = [Max] * (amount + 1)
#     nums[0] = 0
#     for x in coins:
#         for i in range(amount // x):
#             nums[(i+1)*x] = min(nums[i*x] + 1, nums[(i + 1)*x])
#     return nums[amount] if nums[amount] != Max else -1


coins = [1, 2, 5]
amount = 11
coinChange(coins, 11)