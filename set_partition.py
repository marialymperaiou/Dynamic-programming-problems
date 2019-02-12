# Number of ways to partition a set
# if N is the number of elements, and k the sets, then S(n,k) is the total number of partitions
# and the sum of those from k = 1 to N is a Bell number (Bell(N))

N = 10          #number of elements
k = 5           #number of sets

#S(n+1, k) = k*S(n, k) + S(n, k-1)
#recursive solution based on the recursion above
def rec_bell(N, k):
    if (N == 0)or(k == 0)or(k > N):
        return 0
    if (N == k)or(k == 1):
        return 1
    return rec_bell(N - 1,k)*k + rec_bell(N - 1, k - 1)
print(rec_bell(N, k))    



    

