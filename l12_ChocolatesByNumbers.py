# lesson_12_Euclidean_algorithm
# task_ChocolatesByNumbers_Easy -- O(log(N+M)) 

N, M = 10, 4
def solution(N, M):
    gcd = get_gcd(N, M)
    res = N // gcd
    
    return res

def get_gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return get_gcd (b, a%b)


## Naive_apporach -- O(N+M) -- 62% w/time-out
def solution(N, M):
    res = set()
    ate, i = 0, 0
    while ate not in res:
        res.add(ate)
        i += 1
        ate = (i * M) % N
    #print(res)
        
    return len(res)