def solve(li):
    list=li
    list.sort()
    x=int(input("how many?"))
    z=len(list)
    if(0<=x<=z):
        y=int(input("enter 1 fortop 2 forlast?"))
        if(y==1):
            max=len(list)
            y=list[max-x:max]
            y.reverse()
            print(y)
        elif(y==2):
	        print(list[:x])
        else:
    	    print("wrong option")
    else:
       c=str(len(list))
       print("wrong number!!!enter element in the range o to "+c)	    

while(True):
    d=[[1,2,3,7,4],[4,5,6,7],[5,4,8,7,6]]
    a=int(input("1 for list1,2 for list2,3 for list3"))
    if 1<=a<=3:
    	c=d[a+1]
    	print("the list is"+str(c))
    	solve(c)
        
    else:
    	print("wrong option")