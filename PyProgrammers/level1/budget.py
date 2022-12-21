'''
Created on 2022. 6. 21.

@author: shywj
'''

def solution(d, budget):
    answer = 0
    
    d = sorted(d, key=None, reverse=False)
    
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
    
    return answer
    
    

if __name__ == "__main__" :
    d = {1,3,2,5,4}
    budget = 9
    
    print(solution(d, budget))
    
    