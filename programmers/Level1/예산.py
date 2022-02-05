def solution(d,budget):
    d=sorted(d)
    for i in range(len(d)):
        budget=budget-d[i]
        if budget<0:
            return i
    return len(d)
