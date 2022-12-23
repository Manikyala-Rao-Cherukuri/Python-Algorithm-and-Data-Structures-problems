def countDown(i):
    print(i)
    if i<=1:
        return
    else:
        countDown(i-1)

countDown(3)
