# lesson_12_Euclidean_algorithm
# task_CommonPrimeDivisors_Medium -- 69% w/wrong_answers 
# Correctness_85%_Performance_50%

A = [15, 10, 3]
B = [75, 30, 5]
def solution(A, B):
    res = list()
    for i in range(len(A)):
        gcd = get_gcd(A[i], B[i])
        #print(gcd)
        m_A, m_B = A[i]//gcd, B[i]//gcd
        if (gcd % m_A == 0) and (gcd % m_B == 0):
            res.append(gcd)
            #print(res)
        else:
            pass
        
    return len(res)

def get_gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return get_gcd(b, a%b)