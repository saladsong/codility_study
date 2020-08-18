# lesson_7_Stacks_and_Queues
# task_StoneWall_Easy -- O(N)
H = [8,8,5,7,9,8,7,4,8]

def solution(H):
    stack = list()
    stack_idx = list()
    cnt = 0
    
    for idx, item in enumerate(H):
        if len(stack) == 0:
            stack.append(item)
            stack_idx.append(idx)
        else:
            if item < stack[-1]:
                while (len(stack) > 0) and (item < stack[-1]):
                    stack.pop()
                    stack_idx.pop()
                    cnt += 1
                    
                if (len(stack) > 0) and (item == stack[-1]):
                    pass
                else:
                    stack.append(item)
                    stack_idx.append(idx)
                    
            elif item > stack[-1]:
                stack.append(item)
                stack_idx.append(idx)
                
            else:
                pass
        
    if len(stack) > 0:
        cnt += len(stack)
    
    return cnt