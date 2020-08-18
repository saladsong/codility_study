# lesson_8_Leader
# task_Dominator_Easy -- O(N)
A = [3,4,3,2,3,-1,3,3]

def solution(A):
    cnt = 0
    for idx in range(len(A)):
        if cnt == 0:
            cnt += 1
            value = A[idx]
        else:
            if value != A[idx]:
                cnt -= 1
            else:
                cnt += 1
    
    cand = -1
    if cnt > 0:
        cand = value
    
    res = list()
    for idx in range(len(A)):
        if A[idx] == cand:
            res.append(idx)
    
    if len(res) > (len(A)//2):
        return res[0]
    else:
        return -1