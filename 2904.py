# class Solution:
#     def shortestBeautifulSubstring(self, s: str, k: int) -> str:

#         res = []
#         sta = 0
#         end = 0
#         count = 0

#         while end < len(s):

#             if s[end] == '1':
#                 count += 1

#             end += 1

#             if count == k:
#                 while sta < end:
#                     if s[sta] == '1':
#                         break
#                     sta += 1

#                 res.append(s[sta:end])

#                 count -= 1
#                 sta += 1

#         if not res:
#             return ""

#         res.sort()
#         return res[0]

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones >= k:
                if ones == k:
                    current = s[left:right + 1]

                    if best == "" or len(current) < len(best) or (
                        len(current) == len(best) and current < best
                    ):
                        best = current

                if s[left] == '1':
                    ones -= 1
                left += 1

        return best