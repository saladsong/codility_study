# lesson_4_CountingElements
# task_MissingInteger_Medium -- O(N) or O(N*logN) 
A = [1,3,6,4,1,2]
A = [1,2,3]
A = [-1,-3]

def solution(A):
    pos = dict()
    cand = set(range(1, len(A)+1))
    
    for item in A:
        if (item in cand) and (item not in pos):
            pos[item] = 1
            cand.remove(item)
            
    if len(cand) == len(A):
        return 1
    elif len(cand) == 0:
        return len(A)+1
    else:
        return min(cand)