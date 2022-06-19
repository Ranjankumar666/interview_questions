def _permute(curr, arr, results):
    if len(curr) == len(arr):
        results.append(curr)
        return results

    for i in arr:
        if i not in curr:
            _permute(curr+[i], arr, results)
    
    return results
    
    
def permute(arr):
    return _permute([], arr, [])

print(permute([1, 2, 3]))