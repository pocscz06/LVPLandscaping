def is_subsequence(x, y):
    n = len(x)
    m = len(y)
    
    i, j = 0, 0
    
    while i < n and j < m:
        if x[i] == y[j]:
            j += 1
        i += 1
    
    if j == m:
        return "yes"
    else:
        return "no"
    
# Example usage:
x = [1, 12, 4, 8, 10, 6]
y = [12, 10, 6]
print(is_subsequence(x, y))  # Output: yes

x = [-2, 0, 4, 0, 2, 7]
y = [0, 2, 4]
print(is_subsequence(x, y))  # Output: no