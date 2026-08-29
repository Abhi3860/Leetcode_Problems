def lexicographicallySmallestArray(nums, limit):
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        
        result = [0] * n
        
        group_indices = [order[0]]
        group_values = [nums[order[0]]]
        
        for k in range(1, n):
            i = order[k]
            prev_i = order[k - 1]
            
            if nums[i] - nums[prev_i] <= limit:
                group_indices.append(i)
                group_values.append(nums[i])
            else:
                group_indices.sort()
                for idx, val in zip(group_indices, group_values):
                    result[idx] = val
                group_indices = [i]
                group_values = [nums[i]]

        group_indices.sort()
        for idx, val in zip(group_indices, group_values):
            result[idx] = val
        
        return result