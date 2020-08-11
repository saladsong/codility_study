# lesson_3_TimeComplexity
# task_TapeEquilibrium_Easy -- O(N)
A = [3,1,2,4,3]
A = [-1000, 1000]

def solution(A):
    pre, post = 0, sum(A)
    res = {}
    
    for idx in range(len(A)-1):
        pre = pre + A[idx]
        post = post - A[idx]
        
        diff = abs(pre - post)
        if diff not in res:
            res[diff] = 1
        
    return min(res)