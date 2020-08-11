# lesson_5_PrefixSums
# task_GenomicRangeQuery_Medium -- O(N*M)
## score = 62% w/Time-out_Error  
S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]

def solution(S, P, Q):
    res = []
    nucle = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    S_str = []
    for s in S:
        S_str.append(nucle[s])
    
    for idx in range(len(P)):
        res_min = min(S_str[ P[idx] : Q[idx]+1 ])
        res.append(res_min)
    
    return res