#bell triangle method:
#1
#1 2
#2 3 5
#5 7 10 15

N = 5

#the rightmost element of the series for the N-1-th bell number
#becomes the leftmost element of the series for the N-th bell numberB
Bell = [[0 for i in range(N+1)] for j in range(N+1)]    #NxN matrix
def triangle_bell(N, Bell):
    Bell[0][0] = 1
    for i in range(1, N+1):
        #first column
        Bell[i][0] = Bell[i-1][i-1]     #the diagonal element (last of the previous row)
        for j in range(1, i+1):
        #sum of the previous element the previous row in this row 
        #plus the previous  element in the current row
            Bell[i][j] = Bell[i-1][j-1] + Bell[i][j-1]
    return Bell[N][0]           #return the 1st column of the N-th row, which is the N-th bell number
print(triangle_bell(N, Bell))