# lesson_9_Maximum_slice_problem
# task_MaxSliceSum_Easy -- O(N)

A = [3,2,-6,4,0]
def solution(A):
    if len(A) == 1:
        return A[0]

    pref = prefix_sum(A)
    p, q = 0, 1
    max_sum = get_sliced_sum(pref, p, q)  ## a_0

    for idx in range(1,len(A)):
        q = idx + 1
        if pref[idx] < pref[p]:
            p = idx
        tmp_max_sum = get_sliced_sum(pref, p, q)
        max_sum = max(tmp_max_sum, max_sum)
    
    return max_sum
          
def prefix_sum(A):
    pref = [0]
    for i in range(len(A)):
        summed = pref[i] + A[i]
        pref.append(summed)
    return pref
        
def get_sliced_sum(pref, p, q):
    return pref[q] - pref[p]