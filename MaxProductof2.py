def maxProduct(dums):
    l1=l2= 0
    for i in dums:
        if i>l1:
            l1,l2 = i, l1
        elif i>l2:
            l2=i
    return (l1-1) * (l2-1)