def capitalize(string):
    a=''
    string=list(string.split(' '))
    for i in range(len(string)):
            x=string[i]
            y=x.capitalize()
            a=a+y+" "    
    return a

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
