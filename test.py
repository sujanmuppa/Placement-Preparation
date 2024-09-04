# def question1(X, A):
#     ans = A*1
#     count = 0
#     while ans <= X:
#         ans = A*count
#         req = X - ans
#         if req == 0:
#             break
#         if count % req == 0 and ans < X:
#             return (count, req)
#         count += 1
#     return (-1, -1)

# print(question1(10, 3))

def question3(str):
    variables = []
    operation = []
    for i in str:
        if not i.isalpha() and len(variables) < 2:
            variables.append(i)
        elif i.isalpha() and len(operation) < 1:
            operation.append(i)
        if len(variables) == 2 and len(operation) == 1:
            if operation[0] == 'A':
                temp = int(variables[0]) & int(variables[1])
                variables = [temp]
                operation = []
                print(temp)
            elif operation[0] == 'B':
                temp = int(variables[0]) | int(variables[1])
                variables = [temp]
                operation = []
                print(temp)
            elif operation[0] == 'C':
                temp = int(variables[0]) ^ int(variables[1])
                variables = [temp]
                operation = []
                print(temp)
    return variables[0]


print(question3("1A0B1C1"))