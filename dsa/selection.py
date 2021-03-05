

def sort (num):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            print("1st",num)
            if num[j]<num[minpos]:
                minpos=j
        temp =num[i]
        num[i]=num[minpos]
        num[minpos]=temp
        print(num)


num=[5,3,8,6,7,2]
sort(num)
# print(num)