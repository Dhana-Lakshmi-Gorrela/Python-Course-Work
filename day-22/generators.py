'''
def retrivedata():
    data = ['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i

reels = retrivedata()

while True:
    status = input("[s]croll or [q]uit: ")
    if status == 's':
        print(next(reels))
    else:
        break
'''
'''
def even():
    i = 0
    while True:
        i+=2
        yield i

n = 10
res = even()
for i in range(n):
    print(next(res))
'''

def isprimes(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return Flase
    return True

def primes(n):
    for i in range(2,n+1):
        if isprimes(i):
           yield i

n = 50
res = primes(n)
for i in res:
    print(i)

