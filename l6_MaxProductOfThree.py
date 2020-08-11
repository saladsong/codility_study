# lesson_6_Sorting
# task_MaxProductOfThree_Easy -- O(N*logN)
A = [-3, 1, 2, -2, 5, 6]

def solution(A):
    sorted_a = sorted(A)
    res = 0
    
    if sorted_a[1] < 0:
        if sorted_a[-1] > 0:
            p, q, r = sorted_a[0], sorted_a[1], sorted_a[-1]
            res = p*q*r
        else:
            p, q, r = sorted_a[-3], sorted_a[-2], sorted_a[-1]
            res = p*q*r
            
    pp, qq, rr = sorted_a[-3], sorted_a[-2], sorted_a[-1]
    resres = pp*qq*rr
    
    if res > resres:
        return res
    else:
        return resres

    sorted_a = merge_sort(A)
    res = 0

### past_trial below
## failed with time-out_error of O(N**3) <- why?
def solution(A):
    sorted_a = merge_sort(A)
    res = 0    

    if sorted_a[1] < 0:
        if sorted_a[-1] > 0:
            p, q, r = sorted_a[0], sorted_a[1], sorted_a[-1]
            res = p*q*r
        else:
            p, q, r = sorted_a[-3], sorted_a[-2], sorted_a[-1]
            res = p*q*r
            
    pp, qq, rr = sorted_a[-3], sorted_a[-2], sorted_a[-1]
    resres = pp*qq*rr
    
    if res > resres:
        return res
    else:
        return resres
    
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left_A = A[:mid]
    right_A = A[mid:]
    left_A = merge_sort(left_A)
    right_A = merge_sort(right_A)
    return merge(left_A, right_A)
    
def merge(L, R):
    res = list()
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                res.append(L[0])
                L = L[1:]
            else:
                res.append(R[0])
                R = R[1:]
        elif len(L) > 0:
            res.append(L[0])
            L = L[1:]
        elif len(R) > 0:
            res.append(R[0])
            R = R[1:]
    return res