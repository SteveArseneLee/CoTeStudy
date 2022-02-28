# 큰수 만들기
def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        print("************************")
        print("i :",i,"num  ;",num)
        
        while collected and collected[-1] < num and k > 0:
            print("1. collected", collected)
            collected.pop()
            k -= 1
            print("k :",k)
        
        if k == 0:
            collected += number[i:]
            break

        collected.append(num)
        print("2. collected", collected)
        

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    print("==========================")
    return answer
    

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
