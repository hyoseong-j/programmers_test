def solution(dartResult):  
    answer = 0
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    post = ['S', 'D', 'T']
    option = ['*', '#']
    

    S = 1
    D = 2
    T = 3
    b = []
    for i in dartResult:
        if i in a:
            b.append(int(i))
        elif i in post:
            b.append(int(i))
        elif i in option:
            b.append(srt(i))
        
    for i in range(0, len(b) - 1, 2):
        answer += b[i] ** b[i + 1]
        if b[i] == '*':
            answer *= 2
        elif b[i] == '#':
            answer += (b[i - 2] + b[i - 1]) * -1
        
            
    return answer
pritn(solution(1S))
    

    
