# lesson_5_PrefixSums
# task_PassingCars_Easy -- O(N) 
A = [0,1,0,1,1]

def solution(A):
    east_cnt = list()
    pass_cnt = res = 0
    
    for i in A:
        if i == 0:
            east_cnt.append(0)
        else:
            pass_cnt = len(east_cnt)
            res += pass_cnt
    
    if res > 1000000000:
        res = -1
    
    return res