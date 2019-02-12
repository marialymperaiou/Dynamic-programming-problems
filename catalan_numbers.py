# Counting problem of combinations
# This series is the following: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
# Catalan(n) is the sum of catalan(i)*catalan(n-i-1)

N = 10      #define the N-th catalan number that you want to compute

#recursive edition
def rec_catalan(N):
    s = 0           #sum of the catalan numbers
    if N<=1:        #c[0] = c[1] = 1
        return 1
    for i in range(N):
        s += rec_catalan(i)*rec_catalan(N-i-1)
    return s

print(rec_catalan(N))

#build the solution in the bottom up way
catalan = [0 for i in range(N+1)]
def bu_catalan(N):
    catalan[0] = catalan[1] = 1       #c[0] = c[1] = 1
    for i in range(2,N+1):
        catalan[i] = 0
        for j in range(i): 
            catalan[i] += catalan[j] * catalan[i-j-1] 
    return catalan[N]

print(bu_catalan(N))
    
