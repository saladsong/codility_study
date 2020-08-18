# lesson_7_Stacks_and_Queues
# task_Nesting_Easy -- O(N)
S = "(()(())())"
S = "())"

def solution(S):
    brac = { ')' : '(' }
    stack = list()
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if (len(stack) == 0) or (brac[s] != stack[-1]):
                return 0
            else:
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0