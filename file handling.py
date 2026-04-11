#write()
'''a=open('emmanuel.txt',"w")
a.write("Codegnan it solutions")
a.close()'''

''' a=open('emmanuel.txt',"w")
a.write('\tpython course')
a.close()'''

#append()
'''a=open('emmanuel.txt',"a")
a.write('\temmanuel raju')
a.close()'''

'''a=open('emmanuel.txt',"w")
b=input("data")
a.write(b)
a.close()'''


#readline()
'''a=open('emmanuel.txt')
#print(a.read())    #it will display entire content
#print(a.readline()) #it will display first line
#print(a.readlines())  #it will display with \n
#print(a.read(10)) '''      #it will display no. of characters


#writelines() it makes every object side by side
'''a=open('data.txt',"w")
b=["Python","Dsa","Java","Html","Css"]
a.writelines('\n'.join(b))
a.close()'''

'''a=open("functions.py") 
print(a.read())'''

'''a=open("C:\\Users\\EMMANUEL\\OneDrive\\Desktop\\python codegnan\\loops.py")
print(a.read())'''


#error handling
#syntax error
'''for i in range(10)
print(i)'''

#run time error
'''a=int(input('enter a value'))
b=int(input('enter b value'))
print(a//b)'''  #b value is 0 it gets error

#logical error
'''a=10
b=20
print(a-b)'''

'''a=2 
b=5
if a>b:
    print('true')'''


#exception handeling
'''while True:
    a=int(input('a value'))
    b=int(input('b value'))
    try:
        c=a//b
        print(c)
    except:
        print('exception is raised')
    else:
        print('no exception')
    finally:
        print('program end.......')'''






























