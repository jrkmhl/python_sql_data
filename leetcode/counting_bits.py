def count_bits(n):
    dp = []
    dp[0] = 0
    dp[1] = 1
    k = 1

    dp[2] = 1 + dp[0] [2-2]
    dp[3] = 1 + dp[1] [3-2]

    dp[4] = 1 + dp[0] [4-4]
    dp[5] = 1 + dp[1] [5-4]
    dp[6] = 1 + dp[2] [6-4]
    dp[7] = 1 + dp[3] [7-4]

    dp[8] = 1 + dp[0]  [8-8]
    dp[9] = 1 + dp[1]  [9-8]
    dp[10] = 1 + dp[2] [10-8]
    dp[11] = 1 + dp[3] [11-8]
    dp[12] = 1 + dp[4] [12-8]
    dp[13] = 1 + dp[5] [12-8]
    dp[14] = 1 + dp[6] [14-8]
    dp[15] = 1 + dp[7] [16-8]

    dp[16] = 1 + dp[0]



