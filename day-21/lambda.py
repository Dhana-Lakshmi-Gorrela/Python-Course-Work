'''
greater = lambda a,b: a if a>b else b

print(greater(12,12))
print(greater(13,14))
print(greater(1,2))
print(greater(3,4))

wish = lambda name: f'welcome to the course {name}'

print(wish("Teju"))
print(wish("sathvika"))
print(wish("kavya"))
print(wish("pavani"))

iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(45))
print(iseven(18))
print(iseven(17))

avg = lambda a,b,c: (a+b+c/3)

print(avg(4,5,6))
print(avg(30,26,15))
'''
domain = lambda mail:(mail.split('@')[-1]).split('.')[0]

'''
print(domain('dhana@codegnan.com'))
print(domain('dhana@gmail.com'))
print(domain('dhana@outlook.com'))
print(domain('dhana@yahoo.com'))                       
'''
'''
gst = lambda price : price + price*0.18

print(gst(1000))
print(gst(5000))
print(gst(8000))
'''
'''
prices = [5678,8765,5432,123,1234,1500,3000]

res = list(map(lambda price: price + price*0.18, prices))

print(res)
'''
'''
names = {'dhana','teju','sathvik','kavya','pavani'}

res = list(map(lambda name: name.title(),names))

print(res)
'''
'''
prices = [5678,8765,5432,123,1234,1500,3000]

res = list(map(lambda price: price - price*0.3, prices))
print(res)
'''
'''
prices = [5678,8765,5432,123,1234,1500,3000]

res = list(filter(lambda price: price>5000, prices))
print(res)
'''
'''
prices = [5678,8765,5432,123,1234,1500,3000]

res = list(filter(lambda price: price%2!=0, prices))
print(res)
'''
'''
names = {'dhana','teju','sathvika','pavani','kavya'}
res = list(filter(lambda name: len(name)>5, names))
print(res)
'''

from functools import reduce
l=[3,34,23,234,24,124,462]
res=reduce(lambda res,i:res+i,names)
print(res)

names =['dhana','teju','sathvika','pavani','kavya']
res=reduce(lambda res,i: res+' '+i, names)
print(res)

'''
product = {'sugar':60,
           'salt':20,
           'eggs':90,
           'cooking oil':120,
           'bread':45
           }

print(dict(sorted(product.items())))
print(dict(sorted(product.items(),reverse=True)))
print(dict(sorted(product.items(),key = lambda i:i[1])))
print(dict(sorted(product.items(),key = lambda i:i[1],reverse=True)))
'''

