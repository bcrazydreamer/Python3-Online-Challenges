from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    name,space,price = input().rpartition(' ')
    if name not in od:
        od[name] = int(price)
    else:
        od[name] += int(price)
for item, price2 in od.items():
    print(item,price2)
