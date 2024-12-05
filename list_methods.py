from functools import reduce

myList= [4,6,8,1.5,10,7,5]
newlist=["", 'Argentina', '', 'Brazil', 'Chile', '','Columbia', '', 'Ecuador', '', '', 'Venezula']

def increase(num):
    return num+1

def multiple(num):
    if num%3==0:
        return num
    


multipler = lambda x, y:x*y

print(reduce(multipler, myList))
#print(list(filter(None, newlist)))
#print(list(filter(lambda num: num %3==0, myList)))

# print(map(increase, myList))
    
#for num in myList:
#     newlist.append(num+1)

# print(myList)
# print(newlist)

