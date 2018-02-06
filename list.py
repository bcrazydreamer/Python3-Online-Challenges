if __name__ == '__main__':
    n=int(input())
    array=[]
    for i in range(n):
        val=input().split()
        for i in range(1,len(val)):
           val[i] = int(val[i])
    
        if val[0]=='insert':
            val[1]=int(val[1])
            array.insert(val[1],val[2])
            
        elif val[0]=='append':
            array.append(val[1])

        elif val[0]=='remove':
            array.remove(val[1])
            
        elif val[0]=='sort':
            array.sort()
            
        elif val[0]=='pop':
            array.pop()

        elif val[0]=='reverse':
            array.reverse()

        elif val[0]=='print':
            print(array)
