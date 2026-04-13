#list comprehension
a=['codegnan','python','course']
#['CODEGNANA','PYTHON','COURSE']
'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]

'''b=[i.upper() for i in a]
print(b)'''

#print([i.upper() for i in a])

'''a=['python','java','ml']
print([i.title() for i in a])'''   

'''a=[1,2,3,5,6,8,12,13]
print([i*i for i in a])'''

'''a=[1,2,3,5,6,8,12,13]
print([i**2 for i in a])'''

'''a=[1,2,3,5,6,8,12,13]
print([pow(i,2) for i in a])'''


#if-usage in list comprehension
#even and odd
'''a=16
print([ i for i in range(a) if i%2==0])'''

'''a=16
print([ i for i in range(a) if i%2!=0])'''

#square of even no.
'''a=16
print([ i**2 for i in range(a) if i%2==0])'''

#task
'''fruits=["apple","grapes","mango","banana","berry","kiwi","dragon"]
print([i for i in fruits if "a" in i])

fruits=["apple","grapes","mango","banana","berry","kiwi","dragon"]
print([i for i in fruits if "a"not in i])'''


#if-else using
'''print([i**2 if i%2==0 else i*5 for i in range(21)])'''


'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
print([a[i]+b[i] for i in range(len(a))])
print([a[i]+b[i] for i in range(5)])'''


'''result = [x**2 for x in range(1, 16) if x % 2 != 0]
print(result)'''


'''nums = [3, -1, 5, -7, 2]
result = [x if x > 0 else 0 for x in nums]
print(result)'''






















