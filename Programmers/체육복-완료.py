def solution(n, lost, reserve):
    reserveset = set(reserve) - set(lost)
    lostset = set(lost) - set(reserve)
    
    for i in reserveset:
        if i-1 in lostset:
            lostset.remove(i-1)
        elif i+1 in lostset:
            lostset.remove(i+1)
    return n-len(lostset)