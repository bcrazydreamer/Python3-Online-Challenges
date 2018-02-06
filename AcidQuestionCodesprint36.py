#!/bin/python3

import sys

def acidNaming(x):
    l=len(x)
    last=x[l-2]+x[l-1]
    if l>5:
       first=x[0]+x[1]+x[2]+x[3]+x[4]
       
    if "ic" in last:
        if l>5:
            if "hydro" in first:
                return "non-metal acid"
            else:
                return "polyatomic acid"
        else:
            return "polyatomic acid"
        
    else:
        return "not an acid"
            
    
if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)
