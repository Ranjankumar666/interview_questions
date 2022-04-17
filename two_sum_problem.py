def two_sum_problem(arr, s):
        n = len(arr)
        # map for searching 
        mp = {}
        count = 0

        for i in range(n):
            # Check if the current element exists in the map, if not
            # add the t = s - arr[i] to map with its value i
            if mp.get(arr[i]) is None:
                mp[s - arr[i]] = i
            # Return found arr[i] value and current element
            else:
                count += 1
                mp[s - arr[i]] = i
        
        return count


print(two_sum_problem([1, 1, 1, 1], 2))




