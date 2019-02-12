# given a list, find the number of pairs that sum up to a given number

def pair_sum(l, N):
    if len(l)<2:            #the list needs to have at least 2 elements to make the sum
        return 0            #no solution
    #we can find the differences between the given N and each of the
    #elements of the list. If the difference exists, then we have a solution
    dif = []                #here, we store the differences
    res = []                #here, we keep the resulting pairs
    for i in l:
        d = N - i           #difference
        if d not in dif:    #this number has not be examined
            dif.append(i)   #so we add the complement
        else:               #complement found, so d+i = N
            res.append((min(i,d),max(i,d)))     #store the valid pair
            
    return res, len(res)

def pair_sum_2(i,N):
    if len(l)<2:            
        return 0
    l.sort()                #the list should be sorted, so that we know in which range
                            #our solution is
    id1 = 0                 #one index at the start
    id2 = len(l)-1          #one at the end
    cnt = 0                 #pair counter
    pair_list = []
    while id1<id2:          #id1+id2 = len(l), all the pairs would have been calculated
        s = l[id1]+l[id2]   #sum the 2 elements
        print(s)
        if s==N:            #pair found from the elements at positions id1,id2
            cnt+=1
            pair_list.append((l[id1],l[id2]))
            id1+=1          #as the list is sorted, we need to proceed
            id2-=1          #by both sides
        if s<N:             #sum too small
            id1+=1          #so increase the low bound
        if s>N:             #sum too large
            id2-=1          #decrease the upper bound
    return pair_list,cnt


#run
l = [1,1,2,2,3]
N = 4
print(pair_sum_2(l, N))
