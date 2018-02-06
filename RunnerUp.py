if __name__ == '__main__':
    n = int(input())
    arr = (input().split())
    for i in range(0,len(arr)):
           arr[i] = int(arr[i])
    winner=max(arr)
    temp=winner
    arr.remove(winner)
    for i in range(n):
        winner=max(arr)
        if winner==temp:
            arr.remove(winner)
            
    runnerup=max(arr)
    print(runnerup)
