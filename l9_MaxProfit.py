# lesson_9_Maximum_slice_problem
# task_MaxProfit_Easy -- O(N)

A = [23171, 21011, 21123, 21366, 21013, 21367]
def solution(A):
    if len(A) < 2:
        return 0
        
    min_prc = A[0]
    max_prc = A[1]
    max_prof = max(0, max_prc - min_prc)
    
    for idx, cand in enumerate(A[1:]):
        max_prc = A[idx+1]
        if cand < min_prc:
            min_prc = cand
        
        max_prof_cand = max_prc - min_prc
        max_prof = max(max_prof, max_prof_cand)
    
    return max(max_prof, 0)