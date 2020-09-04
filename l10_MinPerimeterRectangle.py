# lesson_10_Prime_and_Composite_numbers
# task_MinPerimeterRectangle_Easy -- O(sqrt(N))

N = 30
def solution(N):
    i = 1
    res = 2 * (1 + N)
    
    while (i * i) <= N:
        if (N % i) == 0:
            a, b = i, N//i
            res = min(res, 2 * (a + b))
        i += 1
    
    return res