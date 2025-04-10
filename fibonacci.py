def fibonacci(n):
    # use the Dynamic Programming
    fiboList = []
    fiboList.append(1)
    fiboList.append(1)
    for i in range(2, n):
        fiboList.append(fiboList[-1] + fiboList[-2])

    #print fibolist
    print(fiboList)
    ratioList = []
    for i in range(1, len(fiboList)):
        ratioList.append(fiboList[i - 1] / fiboList[i])

    #print ratioList
    print(ratioList)


fibonacci(10)