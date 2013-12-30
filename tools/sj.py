import random

def genrand(small, big) :
    return small + (big-small) * random.random()

def display(small, big) :
    return r'请输入上下限(默认%.2f~%.2f):' % (small, big)

big = 100
small = 0

while True :
    try :
        s = input(display(small, big)).strip()
        if s.lower() == 'exit' :
            break
        a = s.split()
        if a != [] :
            big = float(a[1])
            small = float(a[0])
        rand = genrand(small, big)
        print('(%.2f~%.2f): %.3f\n' % (small, big, rand))
    except :
        print('--Error--\n')
