def comp(x):
    done=[]
    y=list(x)
    result=''
    for i in range(len(y)):
        p=y[i]
        if p in done:
            pass
        else:
            z=y.count(y[i])
            result=result+"("+str(z)+","+str(p)+")"
        done.append(p)
    return result


if __name__ == '__main__':
    x=input()
    result=comp(x)
    print(result)
