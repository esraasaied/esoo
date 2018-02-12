def secret(list):
    if len(list)<3:
        return False
    if len(list)>=3:
        if(list[0]+list[1]+list[2]==15):
            return True
    if len(list)>=4:
        if((list[0]+list[1]+list[3]==15)or(list[0]+list[1]+list[3]==15)or(list[1]+list[2]+list[3]==15)):
            return True
    if len(list)>=5:
        if((list[0]+list[1]+list[4]==15)or(list[0]+list[2]+list[4]==15)or(list[1]+list[2]+list[4]==15)or(list[1]+list[3]+list[4]==15)or(list[2]+list[3]+list[4]==15)):
            return True
                                                                        
                                                                        
                                                                        
p1=[]
p2=[]   
count=0
while True: 
    while True:
        x=int(input('player 1:'))
        if ((x in p1)or(x in p2)or(x<=0)or(x>9)):
            print('x is taken')
        else:
            break
       
    p1.append(x)
    if secret(p1):
        print('p1 win')
        break
    count=count+1
    if count==9:
        print('draw')
        break
    while True:        
        y=int(input('player 2:'))
        if((y in p1)or(y in p2)or(y<=0)or(y>9)):
            print('y is taken')
        else:
            break
        
    p2.append(y)
    if secret(p2):
        print('p2 win')
        break
    count=count+1
