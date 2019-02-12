# n friends that can be single or paired up. In how many ways?

def friends_pair(n):
    if n == 0:
        return 0            #zero ways of pairing zero people
    if n == 1:
        return 1            #one way to pair a pesron, with himself
    if n == 2:
        return 2            #two friends can either be together or not, so there are 2 ways
    #if person is single, call the function friends_pair(n-1)
    #if the person is paired with n-1 ways, call the function with friends_pair(n-2) n-1 times
    
    return friends_pair(n-1) + (n-1)*friends_pair(n-2)
n = 10
print(friends_pair(n))

#dynamic programming
#bottom - up solution
pairs = [0 for i in range(n+1)]

def dp_friends_pair(n, pairs):
    for i in range(n+1):
        if i<=2:
            pairs[i]=i      #for i = 0, i = 1
        else:
            pairs[i]=pairs[i-1]+(i-1)*pairs[i-2]
    return pairs[n]

print(dp_friends_pair(n,pairs))
