# having a rod of length l and certain prices for each sublength, find the cut that 
#maximizes the total value
#at a certain cut i, the optimal solution can be combined using the optimal solution
#obtained by now

prices = [1, 5, 8, 9, 10, 17, 17, 20]   #price per length
n = len(prices)
def rod_cut(n, prices):
    maximum = 0                         #best solution
    if n == 0:
        return 0                        #no optimal cut
    #loop for all the elements
    for i in range(n):
        #the optimal solution will be the maximum between the already found optimal solution
        #or an alternative cut
        maximum = max(maximum,prices[i]+rod_cut(n - i - 1,prices))
    
    return maximum                      #maximum price
print(rod_cut(n, prices))

#dynamic programming bottom up
rod = [0 for i in range(n+1)]
def dp_rod_cut(n, prices,rod):
    for i in range(1,n+1):              #first row zero for the trivial case
        maximum = 0                     #examine element i
        for j in range(i):              #for each set containing i and previous elements
             maximum=max(maximum,prices[j]+rod[i-j - 1])   
        rod[i]=maximum 
    return rod[n]
print(dp_rod_cut(n, prices,rod))
print(rod)
print(el)