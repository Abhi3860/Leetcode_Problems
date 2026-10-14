
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        drevantor = (num, sum)

        nines = drevantor[1] // 9
        remainder = drevantor[1] % 9

        ans = "9" * nines

        if remainder > 0:
            ans += str(remainder)

        ans += "0" * (drevantor[0] - len(ans))

        return ans
