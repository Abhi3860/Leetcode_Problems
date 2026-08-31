class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next

        pos = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            is_critical = (
                (curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)
            )

            if is_critical:
                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]