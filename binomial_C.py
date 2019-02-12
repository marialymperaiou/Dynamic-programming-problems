# Finds the binomial coefficient C(n,k). The recursive relation can be:
# C(n, k) = C(n-1, k-1) + C(n-1, k), C(n, 0) = C(n, n) = 1
# This implies that n objects can be chosen in k ways (combinations), when order doesn't matter

n = 10
k = 5

#recursive
def rec_binomial(n,k):
    if (k == 0)or(n == k):
        return 1
    return rec_binomial(n-1, k-1) + rec_binomial(n-1, k)
print(rec_binomial(n,k))

