# lesson_4_CountingElements
# task_PermCheck_Easy -- O(N) or O(N*logN) 
A = [4,1,3,2]

def solution(A):
    n = len(A)
    total = n*(n+1)/2
    
    if sum(A) != total:
        return 0
    elif len(set(A)) < n:
        return 0
    else:
        return 1 