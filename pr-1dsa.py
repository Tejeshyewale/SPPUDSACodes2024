n=int(input("Enter the size of bucket"))
bucket=[-1]*n
comple=[-1]*n

def hash(telephone):
    return int(telephone)%n

def accept():
    while True:
      num=int(input("enter number of telephone number"))
      if num <= n:
        break
      print("number ofkeys must not exceed")

    keys =[]
    for i in range(num):
       tel=input(f"enter telephone number{i+1}:")
       keys.append(tel)
    return keys

keys =accept()
bucket=[-1]*n
complexity=[-1]*n
collisions=[]

for key in keys:
   ind=hash(key)
   if bucket[ind]==-1:
      bucket[ind]=key


