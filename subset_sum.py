# given a set of int S and a number n, return if there is a subset of S that adds up to n
# a number of S can either be included in the solution or not

n = 2                       #given sum
S = [3, 34, 4, 12, 5, 2]    #the set
m = len(S)                  #size of set
def sub_sum(S,m,n):
    if m == 0 and n!=0:     #if set is empty, but the number is non-zero
        return False        #there is no solution
    if n == 0:              #given number==0
        return True         #empty set always exists
    #element not included, recur for the rest
    #or included, recur for the rest by updating the sum
    if n-S[m-1]>=0:
        return sub_sum(S,m-1,n) or sub_sum(S,m-1,n-S[m-1])
    else:
        return sub_sum(S,m-1,n) 

print(sub_sum(S,m,n))

#Dynamic programming
#bottom up way
sub = [[False for j in range(n+1)] for i in range(m+1)]
def dp_sub_sum(S,m,n,sub):
    for i in range(1,m+1):
        sub[i][0]=True          #empty set
        for j in range(1,n+1):
            if j>=S[i-1]:
                sub[i][j]=sub[i-1][j] or sub[i-1][j-S[i-1]]
            else:
                sub[i][j]=sub[i-1][j] 
    return sub[m][n]
print(dp_sub_sum(S,m,n,sub))