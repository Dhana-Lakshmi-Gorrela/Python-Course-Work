'''
for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
'''
'''
pin = 1234

for _ in range(5):
    epin = int(input("Enter the pin: "))
    if pin == epin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds.")
'''
'''
n = int(input("Enter the number: "))
c=0
print("Factors: ",end=' ')
for i in range(1,n+1):
    if n%i==0:
        c+=1
        
if c==2:
    print("prime number")
else:
    print("not prime number")
    '''

n = int(input("Enter the number: "))

for i in range(1,n+1):
    if n%i==0:
        print("not prime number")
else:
    print("prime number")    

