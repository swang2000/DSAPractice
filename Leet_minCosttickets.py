def mincostTickets(days, costs):
    dp = [1000 * 365] * 366
    dp[0] = 0
    travelday = [False] * 366
    for i in days:
        travelday[i] = True
    for i in range(1, 366):
        if not travelday[i]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + costs[0]
            if i - 7 < 0:
                dp[i] = min(dp[i], costs[1])
            else:
                dp[i] = min(dp[i], dp[i - 7] + costs[1])
            if i - 30 < 0:
                dp[i] = min(dp[i], costs[2])
            else:
                dp[i] = min(dp[i], dp[i - 30] + costs[2])
    return dp[365]

days = [1,4,6,7,8,20]
costs = [2,7,15]
mincostTickets(days, costs)
