# lesson_11_Sieve_of_Eratosthenes
# task_CountNonDivisible_Medium -- O(N**2) -- 55% w/time-out (*TO BE REVISED)

A = [3, 2, 3, 1, 6]
def solution(A):
    res = list()
    sorted_A = sorted(A)

    for a in A:
        div_lst = count_div(a)
        cnt, j = 0, 0
        while (j < len(A)) and (sorted_A[j] <= a):
            if (sorted_A[j] in div_lst):
                cnt += 1
            else:
                pass
            j += 1
            
        cnt = len(A) - cnt
        res.append(cnt)

    return res

def count_div(N):
    i = 2
    div_lst = [1, N]
    while (i * i) < N:
        if (N % i) == 0:
            div_lst.append(i)
            div_lst.append(N//i)
        i += 1
    if (i * i) == N:
        div_lst.append(i)

    return set(div_lst)