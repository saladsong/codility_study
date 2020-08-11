# lesson_4_CountingElements
# task_MaxCounters_Medium -- O(N+M) 
## score 88% w/Time-out_Error
A = [3,4,4,6,1,4,4]
N = 5

def solution(N, A):
    counter = [0]*N
    max_cnt = 0
    
    for idx in range(len(A)):
        if A[idx] <= N:
            counter[A[idx]-1] += 1
            
            if counter[A[idx]-1] > max_cnt:
                max_cnt += 1
        else:
            counter = [max_cnt]*N
    
    return counter