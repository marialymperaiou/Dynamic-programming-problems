# Given 2 assembly lines and n stations, we need to find the minimum time that a product needs
# in order to be manufactured
# every station incurrs a cost, as well as transfering from the one line to the other

# entry times are entry1, entry2 in array entry
# exit times are exit1, exit2 in array exit_t

# transfer time will be a table of 2 arrays, one for each assembly line
# assembly time will be a table of the same size as the transfer
def path(L1,L2, track):
    if L1<L2:
        track.append(('L1',L1))
    else:
        track.append(('L2',L2))
    return track

def assembly_line(entry, exit_t, transfer, assembly, L1, L2):
    track = []      #here, we keep track of the product's path during assembly
    
    # while entering the 1st and 2nd station
    L1[0], L2[0] = entry[0]+assembly[0][0], entry[1]+assembly[1][0]
    path(L1[0], L2[0],track)
    
    for i in range(1,len(L1)):
        # the product in L1 either comes from the same line, or from the L2
        L1[i] = min(L1[i-1]+assembly[0][i], L2[i-1]+transfer[1][i]+assembly[1][i])
        # accordingly, for the L2
        L2[i] = min(L2[i-1]+assembly[1][i], L1[i-1]+transfer[0][i]+assembly[0][i])
        #return the path
        path(L1[i], L2[i],track)
        
    #exit step, add the exit time
    final = min(L1[len(L1)-1] + exit_t[0], L2[len(L2)-1] + exit_t[1])
    path(L1[len(L1)-1] + exit_t[0], L2[len(L2)-1] + exit_t[1], track)

    return final, track

entry = [2,3]
exit_t = [1,4]
transfer = [[1,3,6,2],[3,2,4,1]]    #from the first to the second
assembly = [[1,5,2,4],[3,1,2,1]]

#initialize the arrays for each line
L1 = [0 for x in range(len(assembly[0]))]
L2 = [0 for x in range(len(assembly[1]))]

print(assembly_line(entry, exit_t, transfer, assembly, L1, L2))