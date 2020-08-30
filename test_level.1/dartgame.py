def solution(dartResult):
    answer = 0
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    post = ['S', 'D', 'T']
    option = ['*', '#']
    c = []
    for i in dartResult:
        c.append(i)
    bcount = len(c) - 1

    for k in range(bcount):
        if c[k] == '1' and c[k + 1] == '0':
            c[k] = '10'
            del c[k + 1]
    b = []
    for i in c:
        if i in a:
            b.append(int(i))
        elif i in post:
            for j in range(len(post)):
                if i == post[j]:
                    b.append(j + 1)
        elif i in option:
            b.append(str(i))
    count = 0
    group = []
    for i in range(0, len(b)):
        if count >= len(b):
            return answer

        if b[count] == '*':
            group[-1] = group[-1] * 2
            group[-2] = group[-2] * 2
            count += 1
        elif b[count] == '#':
            count -= 2
            group[count] = -group[count]
            print(group)
            count += 3
        else:
            group.append(b[count] ** b[count + 1])
            count += 2
        answer = sum(group)

print(solution(input()))
