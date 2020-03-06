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
