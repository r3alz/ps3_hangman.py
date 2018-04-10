def power(n, m):
    for i in range(10):
        if n**i > m:
            if m-n**(i-1) >n**(i) - m:
                return n**(i)
            else:
                return  n**(i-1)


print(power(3, 70))
