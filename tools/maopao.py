#python3X print变为函数需加（），python2x去掉
def randompop():
    import random
    li=[random.randint(1,300) for i in range(20)]
    print(li)
    for i in range(len(li)):
        for j in range(len(li)):
            if i>j and li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    print(li)
    return li

def reverseG(lst):
    for i in range(len(lst)):
        if i>len(lst)/2:
            break
        lst[i],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[i]
    print(lst)
    return lst

lst=randompop()
reverseG(lst)

