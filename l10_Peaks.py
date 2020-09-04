# lesson_10_Prime_and_Composite_numbers
# task_Peaks_Medium -- O(N * log(log(N))

A= [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
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
    if max_ < 2:
        return max_
        
    for m in reversed(range(1, max_+1)):
        if (n % m) == 0:
            k = n // m
            cnt_dict = dict()
            for idx in range(max_):
                gr = peaks[idx] // k
                if gr not in cnt_dict:
                    cnt_dict[gr] = 1
                else:
                    cnt_dict[gr] += 1
                #print(peaks[idx], cnt_dict)
            
            if len(cnt_dict) == m:
                return m
    return 0
