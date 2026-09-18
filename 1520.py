class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        def get_interval(start):
            ch = ord(s[start]) - ord('a')
            end = last[ch]

            i = start

            while i <= end:
                idx = ord(s[i]) - ord('a')

                if first[idx] < start:
                    return -1, -1

                end = max(end, last[idx])

                i += 1

            return start, end

        intervals = []

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if i == first[idx]:
                left, right = get_interval(i)

                if left != -1:
                    intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result