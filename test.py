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

print(question1(10, 3))