# lesson_7_Stacks_and_Queues
# task_Fish_Easy -- O(N)
A = [4,3,2,1,5]
B = [0,1,0,0,0]

def solution(A, B):
    stack = list()
    idx_stack = list()
    
    for idx, item in enumerate(B):
        br = False
        if item == 0:
            if (len(stack) > 0) and (stack[-1] == 1):
                while (len(stack) > 0) and (stack[-1] == 1):
                    if A[idx_stack[-1]] < A[idx]:
                        stack.pop()
                        idx_stack.pop()
                    else:
                        br = True
                        break
                if br is not True:
                    stack.append(item)
                    idx_stack.append(idx)
            else:
                stack.append(item)
                idx_stack.append(idx)
                
        else:
            stack.append(item)
            idx_stack.append(idx)

    return len(stack)