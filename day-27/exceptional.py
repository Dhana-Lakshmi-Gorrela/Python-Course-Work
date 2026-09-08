'''
try:
    # a = int(input())
    k={1:12,12:13}
    #print(k[14])
    
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of the program")
    '''
'''
try:
   # a = int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(1[10])
   #print('1'+1)
except ValueError:
    print("Enter the correct datatype")
except keyError:
    print("key is not there")
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("can't divide with zero")
except 
else:
    print("a=",a)
finally:
    print("End of the program")  
'''
'''
try:
    #a = int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
   #print(1[10])
   #print('1'+1)
except (ValueError,keyError,IndexError,
       ZeroDivisionError,TypeError,NameError)
 as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
(ValueError,keyError,IndexError,
       ZeroDivisionError,TypeError,NameError)
'''
'''
try:
    #a = int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
   #print(1[10])
   #print('1'+1)
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
try:
    account = int(input("Enter the ammount: "))
    balance = 5000
    if balance < 0:
        raise Exception("Amount needs to be positive")

except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
