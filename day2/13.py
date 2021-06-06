mydict={}
for totnum in range(0,int(input('Input the total number:'))):
a, b =input('Enter the key value pair:').split()
if a in mydict:
    mydict[a].append(b)
    else:
        mydict [a] = [b]
        print(mydict)
