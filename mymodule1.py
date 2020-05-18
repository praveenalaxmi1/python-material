def mylist():
    l1=[1,2,3,4,5,6,7,8,9,10]
    ec=0
    oc=0
    for i in l1:
        if(i%2==0):
            ec=ec+1
        else:
            oc=oc+1

    print("Even {} odd {}".format(ec,oc))
