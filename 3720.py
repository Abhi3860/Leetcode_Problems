class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for ch in target:
            cnt[ord(ch) - ord('a')] -= 1

        bad = sum(1 for x in cnt if x < 0)

        for i in range(len(target) - 1, -1, -1):
            x = ord(target[i]) - ord('a')

            cnt[x] += 1

            if cnt[x] == 0:
                bad -= 1

            if bad == 0:
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        suffix = []
                        for k in range(26):
                            suffix.append(chr(k + ord('a')) * cnt[k])

                        return target[:i] + chr(c + ord('a')) + ''.join(suffix)

        return ""