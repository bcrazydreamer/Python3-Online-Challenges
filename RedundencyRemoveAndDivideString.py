from collections import OrderedDict
def merge_the_tools(string, div):
    k=int(len(string)/div)
    i=0
    for j in range(k):
        li2=string[i:k]
        result="".join(OrderedDict.fromkeys(li2))
        print(result)
        i=k
        k=k+k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
