class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        dp = points[0]

        for r in range(1, ROWS):
            left = [0] * COLS
            left[0] = dp[0]
            for c in range(1, COLS):
                left[c] = max(dp[c], left[c - 1] - 1)

            right = [0] * COLS
            right[COLS - 1] = dp[COLS - 1]
            for c in range(COLS - 2, -1, -1):
                right[c] = max(dp[c], right[c + 1] - 1)

            nextDp = points[r][:]
            for c in range(COLS):
                nextDp[c] += max(left[c], right[c])

            dp = nextDp

        return max(dp)