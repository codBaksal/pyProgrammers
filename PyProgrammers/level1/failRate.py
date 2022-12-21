'''
Created on 2022. 5. 18.

@author: shywj

전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

N            stages                      result
5    [2, 1, 2, 6, 2, 4, 3, 3]        [3,4,2,1,5]
4    [4,4,4,4,4]                     [4,1,2,3]
7    [1,3,3,4,2,3]

딕셔너리 사용
스테이지 : 실패율 순위 > 스테이지로 정렬

1. 딕셔너리 만들기
2. 실패율 계산해서 딕셔너리에 넣어주기
3. 소팅한 결과를 결과 리스트에 넣어주기

'''
from collections import OrderedDict 

# mySolution
def mySolution(N, stages):
    result = {}
    stag_layer = {}
    for i in range(N):
        stag_layer.setdefault(i+1, 0)
        
    for i in range(len(stag_layer)) :
        dict_key = list(stag_layer.keys())[i]
    
        if dict_key in stages :
            sate_count = stages.count(dict_key)
            stag_layer[dict_key] = sate_count
        else :
            stag_layer[dict_key] = 0

    stages_len = len(stages)
    # change_stages = stages
    stage_list = list(stag_layer.keys())
    
    for stages_num in stag_layer.keys() :
        getCount = stag_layer.get(stages_num) 
        if stages_len > 0:
            result.append(getCount / stages_len)
            stages_len -= getCount
        else :
            stag_layer[stages_num] = 0
        
    result = sorted(result, key=lambda x : result[x], reverse=True)
    
    print(result)
    
    
    
# 간결한 풀이
def betterSolution(N, stages): 
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
        
    
    


if __name__ == '__main__':
    N = 7
    stages = [1,3,3,4,2,3]
     
    print(mySolution(N, stages))