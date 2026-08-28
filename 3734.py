class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = [i for i in range(26) if cnt[i] % 2]

        if len(odd) > 1:
            return ""

        middle = chr(ord('a') + odd[0]) if odd else ""

        half_cnt = [x // 2 for x in cnt]

        target_left = target[:half_len]


        remaining = half_cnt[:]

        possible = True
        for ch in target_left:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            left = target_left

            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate


        prefix = [[0] * 26 for _ in range(half_len + 1)]

        for i, ch in enumerate(target_left):
            prefix[i + 1] = prefix[i][:]
            prefix[i + 1][ord(ch) - ord('a')] += 1

        for i in range(half_len - 1, -1, -1):
            used = prefix[i]

            remaining = half_cnt[:]

            valid_prefix = True

            for c in range(26):
                remaining[c] -= used[c]

                if remaining[c] < 0:
                    valid_prefix = False
                    break

            if not valid_prefix:
                continue

            target_char = ord(target_left[i]) - ord('a')

            for c in range(target_char + 1, 26):
                if remaining[c] == 0:
                    continue

                remaining[c] -= 1


                suffix = []

                for x in range(26):
                    if remaining[x]:
                        suffix.append(chr(ord('a') + x) * remaining[x])

                left = target_left[:i] + chr(ord('a') + c) + "".join(suffix)

                answer = left + middle + left[::-1]

                return answer



        return ""
