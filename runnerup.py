n = int(input())
arr = map(int, input().split())
arr=sorted(arr,reverse=True)
for i in range(n):
    if arr[i]==arr[0]:
            continue
    else:
           print(arr[i])  
           break