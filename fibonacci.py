#Calculation of fibonacci numbers: 0,1,1,2,3,5,8,13...
#each number in the sequence is the addition of the two previous elements
#Different implementations will be tested

#here, the performance will be calculated
from timer_function import timer_function

n = 8   #fibonacci number that we want to calculate

#First, the simple recursive one. The function calls itself with different parameters
#in the way that computes each value bu computing the 2 previous ones
@timer_function
def rec_fib(n):
    if n<=1:
        return n
    return rec_fib(n-1) + rec_fib(n-2)  
    
#Top down technique. We store the calculated values recursively, so that 
#they are not recomputed. Initialize by 0.
    
#store None value, as it is a value that for sure you are not going to find later
mem = [None for i in range(n+1)]
@timer_function
def mem_fib(n, mem):
    mem[0],mem[1] = 0,1         #fib(0)=0, fib(1)=1
    if mem[n]==None:            #not calculated yet, so calculate the values (fib(2), fib(3)...)
        mem[n] = mem_fib(n-1,mem)+mem_fib(n-2,mem)
    #the value of the n position is the fibonnaci number    
    return mem[n] 
    
#Bottom up technique. Calculate each value, store it, and then calculate
#the next numbers. Instead of recursion use repetition
tab = [0 for i in range(n+1)]
def tab_fib(n,tab):
    tab[0],tab[1] = 0,1

    for i in range(2 , n+1): 
        tab[i] = tab[i-1] + tab[i-2] 
    return tab[n]
    
#call the functions here
print(mem_fib(n, mem))

