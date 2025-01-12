def permutasi(arr):
    result = []
    def backtrack(path, used):
        if len(path) == len(arr):
            result.append(path)
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            backtrack(path + [arr[i]], used)
            used[i] = False
    backtrack([], [False] * len(arr))
    return result

arr = [1, 2, 3, 4]
print(permutasi(arr))
