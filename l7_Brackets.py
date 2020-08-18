# lesson_7_Stacks_and_Queues
# task_Brackets_Easy -- O(N)
S = "{[()()]}"
S = "([)()]"

def solution(S):
    stack = list()
    closed = { ')': '(', '}': '{', ']': '[' }
               
    if len(S) == 0:
        return 1
        
    for s in S:
        if s not in closed:
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            elif stack[-1] == closed[s]:
                stack.pop()
            else:
                return 0
                
    if len(stack) == 0:
        return 1
    else:
        return 0