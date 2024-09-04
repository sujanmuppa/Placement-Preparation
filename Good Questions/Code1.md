```py
def question1(X, A):
    ans = A*1
    count = 0
    while ans <= X:
        ans = A*count
        req = X - ans
        if req == 0:
            break
        if count % req == 0 and ans < X:
            return (count, req)
        count += 1
    return (-1, -1)
```

```py
def question2(N, a, b, c, d):
    start = a 
    end = c 
    req = []
    limita = a+(N-1)*b
    limitc = c+(N-1)*d
    while start <= limita and end <= limitc:
        if start == end:
            req.append(start)
            start += b
            end += d
        elif start < end:
            start += b
        else:
            end += d
    return req
```

```py
def question2-alternate(N,a,b,c,d):
    req = []
    for i in range(N):
        t1 = a + i*b
        t2 = (t1-c)//d
        if (t1-c)%d == 0 and t2 < N:
            req.append(t1)
    return req
```
