# lesson_3_TimeComplexity
# task_FrogJmp_Easy -- O(1)
(X, Y, D) = (10, 85, 30)

def solution(X, Y, D):
    dist = Y - X
    jmp_cnt, mod = divmod(dist, D)
    
    if mod > 0:
        jmp_cnt += 1
        
    return jmp_cnt