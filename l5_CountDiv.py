# lesson_5_PrefixSums
# task_CountDiv_Medium -- O(1) 
A, B, K = 6, 11, 2
A, B, K = 10, 10, 7

def solution(A, B, K):
    a, a_l = divmod(A, K)
    b, b_l = divmod(B, K)
    
    res = b - a
    if a_l == 0:
        res += 1
        
    return res