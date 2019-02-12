# Knapsack version, with item repetition allowed

def rep_knapsack(W, N, wt, val, matrix):
    item_list = []
    for i in range(W+1):        #for every subweight
        for j in range(N):      #for each item
            if wt[j]<=i:        #the item can fit in this subweight
                # you can either take it or not
                matrix[i] = max(matrix[i-wt[j]]+val[j], matrix[i])
                #if you take the item, add it in the list
                if matrix[i-wt[j]]+val[j] >= matrix[i]:
                    item_list.append(j)
    return matrix[W], item_list, len(item_list)

W = 8
val = [10, 40, 50, 70] 
wt = [1, 3, 4, 5] 
N = len(val) 
matrix = [0 for i in range(W+1)]
print(rep_knapsack(W, N, wt, val, matrix))

