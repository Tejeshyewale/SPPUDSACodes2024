def createSet():
    s=set()
    return(s)
a=createSet()
b=createSet()
print(type(a),type(b))
print(a)
# i. Add (newElement) -Place a value into the set
def add(myset,element):
    myset.update((element,))  #   {element}
    return
ele=int(input("enter element to add in set:"))
add(a,1)
add(b,ele)
print(a,b)
#iii. Contains (element) Return true if element is in collection
def isMember(myset,element):
    if element in myset:
        return(True)
    else:
        return(False)
#ii. Remove (element) Remove the value
def remove(myset,element):
    if isMember(myset,element):
        myset.remove(element)
        print("Element removed from set:",element)
        #return
    else:
        print("Element not in set:",element)
remove(b,12)
print(b)
#iv. Size () Return number of values in collection Iterator () Return an iterator used to loop over collection
def getSize(myset):
    size=0
    for i in myset:   # iterator
        print(i)
        size+=1
    return(size)
print("Set size:",getSize(b))
#Menu
def menu():
    print("0. Exit\n1. Create Set\n2.Add elements to set \n3.Remove Element\n4.IS Member")
    ch=int(input(""))
    return(ch)
a=set()
b=set()
c=set()
while(1):
    ch=menu()
    if(ch==0):
        break
    elif(ch==1):
        c=createSet()
        #c=a.copy()
    elif(ch==2): 
        ele=int(input("enter element to add in set:"))
        add(c,ele)
    elif(ch==3):
        ele=int(input("enter element to remove in set:"))
        remove(c,ele)
    elif(ch==4):
        ele=int(input("enter element to search in set:"))
        print(isMember(c,ele))
    else:
        break
    getSize(c)
a=c.copy()      
print(a)    
class myset:
    def __init__(self):
        self.s=createSet()
    def add(self,ele):
        add(self.s,ele)
        return
    def remove(self,ele):
        remove(self.s,ele)
        return
    def display(self,label):
        print("Elements in set",label,self.s)
        return
    def intersect(self,s1):
        return(self.s & s1)
    def union(self,s1):
        return(self.s.union(s1))
    def diff(self,s1):
        return(self.s.difference(s1))
    def isSubset(self,s1): 
        return(self.s.issubset(s1))        
a=myset()
a.add(10)
a.add(100)
a.display("A")
b=myset()
b.add(100)
b.display("B")
print('Intersection:',a.intersect(b.s))
print('Union:',a.union(b.s))
print('Diff:',a.diff(b.s))
print('Subset:',b.isSubset(a.s))
