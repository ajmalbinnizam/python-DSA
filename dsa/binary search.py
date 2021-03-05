pos=-1
def search(lis,n):
  l=0
  u=len(lis)-1
  while l<=u:
      mid=(l+u)//2
      if lis[mid]==n:

          globals()['pos']=mid
          return True

      else:
          if lis[mid]<n:
              l=mid+1
          else:
              u=mid-1
  return False
lis=[1,4,3,4,5,6,]
n=4

if search(lis,n):
    print("value found",pos+1)
else:
    print("value not found")