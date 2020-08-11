# lesson_1_Iterations
# task_BinaryGap_Easy
N = 1041

def solution(N):
    bin = []
    while N > 0:
        N, mod = divmod(N, 2)
        bin.append(mod)

    cnt = 0
    res = []
    for c in reversed(bin):
        if c == 1:
            res.append(cnt)
            cnt = 0
        elif c == 0:
            cnt += 1
    
    return max(res)