def solution(A):
    lA=len(A)
    mA=max(A)
    repeats=[0]*mA
    divisors=[[1]]
    
    for x in range(1,mA): divisors.append([1,x+1])
    for x in A: repeats[x-1] +=1
    
    x=2
    while (x*x<=mA):
        for y in range (x, (mA//x)+1):
            tmp=divisors[(y*x)-1]
            tmp.append(x)
            if (y!=x) : tmp.append(y)
            divisors[(y*x)-1]=tmp
        x += 1
    
    r=[]
    
    for y in A:
        sum=0
        for x in divisors[y-1]: sum+=repeats[x-1]
        r.append(lA-sum)
    
    return(r)