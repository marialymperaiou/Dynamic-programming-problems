# P(n, k): the number of ways to reorder a subset having k elements from a set of n elements
# P(n, k) = P(n-1, k) + k* P(n-1, k-1)

n = 10       #n-set
k = 3       #k-subset

#recursive
def rec_permutations(n,k):
    if (k == 0)or(k == 0):
        return 1
    if (k>n):
        return 0
    return k*rec_permutations(n-1, k-1) + rec_permutations(n-1, k)
print(rec_permutations(n,k))

#dynamic programming solution in the bottom up way
P = [[0 for i in range(k + 1)] for j in range(n + 1)]   #kxn matrix
def dyn_permutations(n,k,P):
    for i in range(n + 1): 
        for j in range(min(i, k) + 1): 

            if (j == 0): 
                P[i][j] = 1
            else: 
                P[i][j] = j * P[i - 1][j - 1] + P[i - 1][j] 
            if (j < k): 
                P[i][j + 1] = 0
    return P[n][k] 
print(dyn_permutations(n,k,P))

#the factorial way
# P(n,k) = n!/(n - k)!
f = [0 for i in range(n+1)]     #the list that stores factorials
def fact_permutations(n,k,f):
    f[0] = 1                    #0! = 1
    for i in range(1,n+1):
        f[i] = f[i-1]*i
    return int(f[n]/f[n-k])
print(fact_permutations(n,k,f))
    
    
    
    
    
    
    
    