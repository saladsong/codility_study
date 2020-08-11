# lesson_5_PrefixSums
# task_MinAvgTwoSlice_Medium -- O(N**2)
## score = 60% w/Time-out_Error  
A = [4,2,2,5,1,5,8]

def solution(A):
    res = 0
    base = (A[0]+A[1])/2
    pref = prefix_sums(A)
    
    for idx in range(len(A)):
        end = len(A)-1
        while idx < end:
            cand = count_avg(pref, idx, end)
            if cand < base:
                res = idx
                base = cand
            end -= 1
    return res