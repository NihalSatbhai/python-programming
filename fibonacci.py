def fibo(n):
    emptyList = [0,1]
    for i in range(2,n):
        emptyList.append(emptyList[i-1] + emptyList[i-2])
    return emptyList

result = fibo(8)
print(result)