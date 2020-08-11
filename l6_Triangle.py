# lesson_6_Sorting
# task_Triangle_Easy -- O(N**3)
## score = 81% w/Time-out_Error
A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]

def solution(A):
    s_a = sorted(A)
    for a in range(len(A)-2):
        b, c = a+1, len(A)-1
        while b < c:
            if (s_a[a]+s_a[b]>s_a[c]) and (s_a[b]+s_a[c]>s_a[a]) and (s_a[c]+s_a[a]>s_a[b]):
                return 1
            elif (s_a[a]+s_a[b]<=s_a[c]):
                c -= 1
            elif (s_a[c]+s_a[a]>s_a[b]):
                b += 1
            else:
                break
    return 0