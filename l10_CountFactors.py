# lesson_10_Prime_and_Composite_numbers
# task_CountFactors_Easy -- O(sqrt(N))

N = 24
def solution(N):
    i = 1
    res = 0
    
    while (i * i) < N:
        if (N % i) == 0:
            res += 2
        i += 1
    
    if (i * i) == N:
        res += 1
        
    return res
