
def search(lis,n):
    global i
    i=1
    for i in range(len(lis)):
        if lis[i]==n:
            return lis[i]

lis=[3,4,6,7,9,3,]
n=9

if search(lis,n):
    print("value found",i+1)
else:
    print("value not found")