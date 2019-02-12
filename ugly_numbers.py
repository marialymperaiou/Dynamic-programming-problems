#Ugly numbers have factors 2,3 or 5
#find the n-th ugly number

N = 150
ugly_list = [0 for i in range(N+1)]

#produce ugly numbers
def ugly_numbers(N,ugly_list):
    ugly_list[0]=1      #as a conention, 1 is the 1st ugly number
    c2 = c3 = c5 = 0    #ugly pointers
    #initialy, the multiples are set to 2, 3 and 5, as they are the first uglys
    mul2 = ugly_list[c2]*2      #multiples of 2 have 2 as a factor
    mul3 = ugly_list[c3]*3
    mul5 = ugly_list[c5]*5
    
    for i in range(1,N):
        next_ugly = min(mul2,mul3,mul5)
        ugly_list[i] = next_ugly
        #if we found a multiple of 2
        if next_ugly == mul2:
            #find the next multiple of 2
            c2 += 1
            mul2 = ugly_list[c2]*2
            
        if next_ugly == mul3:
            #find the next multiple of 3
            c3 += 1
            mul3 = ugly_list[c3]*3
            
        if next_ugly == mul5:
            #find the next multiple of 3
            c5 += 1
            mul5 = ugly_list[c5]*5
        
    return next_ugly

print(ugly_numbers(N,ugly_list))