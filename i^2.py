'''from collections import OrderedDict
my_order = OrderedDict()
for i in range(int(input())):
    name,space,price = input().rpartition(' ')
    if name not in my_order:
        my_order[name] = int(price)
    else:
        my_order[name] += int(price)
for item_name, net_price in my_order.items():
    print(item_name,net_price)
'''
from collections import OrderedDict
n=int(input("N"))
i=1
arry=list()
while(i<=n):
    abc=input("Enter word:")
    if abc not in arry:
        arry.append(abc)
        
    else:
        
