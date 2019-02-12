#Having 3 numbers x, y, z, return the number of all the ways that they 
#can form a number N, if repetitions are allowed:
#*x + *y + *z = N

N = 6
x = 1
y = 3
z = 5

#in a random state i, where sum[i] < N, all possible combinations have been formed as:
#sum[i-1] + x, or sum[i-1]+y, or sum[i-1]+z
#so: state[N] = state[N-x]+state[N-y]+state[N-z]

#recursive
def sum_counter(N,x,y,z):
     if (N < 0):  
         return 0 
     if (N == 0):   
         return 1 
     return sum_counter(N - x,x,y,z) + sum_counter(N - y,x,y,z) + sum_counter(N - z,x,y,z)
 
print(sum_counter(N,x,y,z))

#top down
mem = [None for i in range(N+1)]
def td_sum_counter(N,x,y,z):
     if (N < 0):  
         return 0 
     if (N == 0):   
         return 1 
     if mem[N]==None:            #not calculated yet
        mem[N] = td_sum_counter(N - x,x,y,z) + td_sum_counter(N - y,x,y,z) + td_sum_counter(N - z,x,y,z)   
     return mem[N]
 
print(td_sum_counter(N,x,y,z))




