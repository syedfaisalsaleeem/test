#python3
input1=int(input())

count=0
m=[]
m.append(input1)
while input1>1:
    if input1%2==0:
        if input1%3==0:
            input1=int(input1/3)
            count=count+1
            m.append(input1)
            #print(input1)
        else:
            if (input1-1)%3==0 :
                input1=int(input1-1)
                count=count+1
                m.append(input1)
                #print(input1)
            else:
                input1=int(input1/2)
                count=count+1
                m.append(input1)
                #print(input1)

    else:
        if input1%3==0:
            input1=int(input1/3)
            count=count+1
            m.append(input1)
            #print(input1)
        elif (input1-1)%2==0:
            input1=int(input1-1)
            count=count+1
            m.append(input1)
        else:
            input1=int(input1-1)
            count=count+1
            m.append(input1)
            #print(input1)
    
print(count)
list.sort(m)
print(' '.join(map(str,m)))
