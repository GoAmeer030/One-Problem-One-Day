def max_sum(a, n):
    mx, d = 0, 0
    curr_sum = 0
    
    for i, val in enumerate(a):
        curr_sum += i * val
        if i != 0:
            d += val
    
    l, r = 0, 1
    mx = curr_sum
    
    for i in range(n - 1):
        curr_sum = curr_sum - d + a[i] * (n - 1)
        mx = max(mx, curr_sum)
        d = d - a[r] + a[l]
        l = r
        r += 1
    
    return mx