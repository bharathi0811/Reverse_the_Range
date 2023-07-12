def reverse_range(arr,b,c):
    org = arr[b]
    arr[b] = arr[c]
    arr[c]=org
    return arr
arr= list(map(int,input("Enter the list: ").split()))
b= int(input("Enter the first range:"))
c= int(input("Enter the second range: "))
print(reverse_range(arr,b,c))
