# lesson_10_Prime_and_Composite_numbers
# task_Flags_Medium -- 80% w/wrong_answer (*TO BE REVISED)

A = [1,5,3,4,3,4,1,2,3,4,6,2]
def solution(A):
    n = len(A)
    if n < 3:
        return 0
    
    peaks = list()
    for i in range(1, n-1):
        if (A[i] > A[i-1]) and (A[i] > A[i+1]):
            peaks.append(i)
    #print(peaks)
    
    max_ = len(peaks)
    if max_ < 3:
        return max_
    
    res = 0
    for k in range(2,max_+1):
        f = 1
        start_f = peaks[0]
        for p in range(1, max_):
            next_f = peaks[p]
            if (next_f - start_f) >= k:
                f += 1
                start_f = next_f
            if f == k:
                break
            
        #print(k, f, start_f, next_f)
        #print('res', res)
        
        if k == f:
            res = max(res, k)
        if res < k:
            return res
            
    return 0