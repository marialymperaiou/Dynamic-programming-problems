# Having a coin of N cents, in how many ways we can obtain the same value
# if we add coins from a set S repetitions allowed

#recursive
def rec_coin_change(S, l, N):
    
    #we cannot create negative sum, so there is no solution
    if N < 0:
        return 0
    #if we have no change goal N, the only solution contains no coin
    if N == 0:
        return 1

    #if the set of coins is empty, while the sum is positive
    #then again there is no solution
    if l <= 0 and N>=1:
        return 0
    #you can either take the coin or not take it
    #if you take it, check the rest of the coins in the set
    #if you don't take it, check the result without it
    return (rec_coin_change(S, l-1, N) + rec_coin_change(S, l, N - S[l-1]))
S = [1,50,100]
l = len(S)
N = 1000
print(rec_coin_change(S, l, N))

#dynamic programming solution
coin = [[[0 for x in range(l)] for x in range(N+1)] ]
#N+1 because we need to include the default case
def dp_coin_change(S, l, N):
    #n==0 return 1
    for k in range(l):
        coin[0][k] = 1
        
    for i in range(1,N+1):  #take the subproblems of N
        for j in range(l):
            #if you take the j coin of S
            if S[j-1]<=i:
                take = coin[i - S[j-1]][j]
            else:
                take = 0
            #if you don't take the j coin
            if j-1>=0:
                not_take = coin[i][j-1]
            else:
                not_take = 0
            #either the one or the other
            S[i][j] = take + not_take
    return S[N][l-1]
    