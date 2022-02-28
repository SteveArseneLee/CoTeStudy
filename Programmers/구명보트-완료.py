# 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    
    start, end = 0, len(people)-1
    # print(start,end)
    
    while start<=end:
        answer += 1
        # print(people[start], people[end])
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    print(answer)

solution([70, 50, 80, 50], 100)