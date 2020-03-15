#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def decimalToVector(i,l):
    vector=[]
    num=i
    for x in range (l-1,-1,-1):
        bit=num//(2**x)
        num=num%(2**x)
        vector.append(bit)
    return vector
        
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G

def repetitionEncoder(m,n):
    c=m*n
    return c

def repetitionDecoder(v):
    count0=v.count(0)
    count1=v.count(1)
    if count0==count1:
        return []
    elif count0>count1:
        return [0]
    elif count0<count1:
        return [1]

def message(a):
    m=[]
    l=len(a)
    r=2
    while ((2**r)-(2*r)-1)<l:
        r+=1
    k=(2**r)-r-1
    print(l,r,k)
    m.extend(decimalToVector(l,r))
    m.extend(a)
    x=k-l-r
    for i in range (0,x):
        m.append(0)
    return m

def hammingEncoder(m):
    r=2
    while (2**r)-r-1<len(m):
        r+=1
    if (2**r)-r-1 == len(m):
        c=[]
        matrix=hammingGeneratorMatrix(r)
        for i in range (0,len(matrix[0])):
            total=0
            for j in range (0,len(matrix)):
                total+=(matrix[j][i]*m[j])
            total=total%2
            c.append(total)
        return c                
    else:
        return []

def hammingDecoder(v):
    r=2
    while (2**r)-1<len(v):
        r+=1
    if (2**r)-1==len(v):
        # generate H
        H = [[] for i in range(r)]
        for i in range(1,(2**r)):
            u=decimalToVector(i,r)
            for x in range (0,len(u)):
                H[x].append(u[x])
        # generate H transpose
        HT=[[] for i in range((2**r)-1)]
        for x in range (0,len(HT)):
            for j in range (0,len(H)):
                HT[x].append(H[j][x])
        #multiply v by H transpose
        c=[]
        for i in range (0,len(HT[0])):
            vH=0
            for j in range (0,len(HT)):
                vH+=(HT[j][i]*v[j])
            vH=vH%2
            c.append(vH)
        print (c)
        total=0
        x=1
        for t in range(0,len(c)):
            y=c[t]*(2**(len(c)-x))
            total+=y
            x+=1
        x=v[total-1]
        if x==0:
            x=1
        else:
            x=0
        v[total-1]=x
        return (v)
            
    else:
        return []

def messageFromCodeword(c):
    r=2
    while (2**r)-1<len(c):
        r+=1
    if (2**r)-1==len(c):
        x=[]
        powers=[]
        for i in range (0,r):
            powers.append(2**i)
        print (powers)
        for i in range (0,len(c)):
            if i not in powers:
                x.append(c[i])
        return x          
    else:
        return []


def dataFromMessage(m):
    r=2
    while (2**r)-r-1<len(m):
        r+=1
    if (2**r)-r-1 == len(m):
        length=m[:r]
        total=0
        x=1
        for t in range(0,len(length)):
            y=length[t]*(2**(len(length)-x))
            total+=y
            x+=1
        if r+total>len(m):
            return []
        else:
            message=m[r:r+total]
            return message
    else:
        return []




    
