#같은 숫자는 싫어
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        elif i == 0:
            answer.append(arr[i])
    
    
    return answer
    
#올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i =='(':
            stack.append(i)
        else:
            if i == ')':
                if stack == []:
                    return False
                else :
                    stack.pop()
                    
    return stack == []
    
#기능개발
def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    
    while len(progresses) > 0:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else :
            if count != 0:
                answer.append(count)
                count = 0
            day += 1
                
    answer.append(count)
    
    return answer
