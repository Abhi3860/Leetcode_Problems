class Solution:
    def checkValidString(self, s: str) -> bool:
        min_balance = 0
        max_balance = 0

        for ch in s:

            if ch == '(':
                min_balance += 1
                max_balance += 1

            elif ch == ')':
                min_balance -= 1
                max_balance -= 1

            else:  
                min_balance -= 1   
                max_balance += 1 

        
            if min_balance < 0:
                min_balance = 0

            if max_balance < 0:
                return False

        return min_balance == 0