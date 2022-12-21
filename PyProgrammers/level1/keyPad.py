#######################################################
# 키패드 누르기#
# 예시
'''
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 
   더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 
완성해주세요.

입출력 예 
numbers                                hand           result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]    "right"       "LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]    "left"        "LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]       "right"       "LLRLLRLLRL"

'''

def solution(numbers, hand):
    
    if hand == 'right':
        hand = "R"
    else :
        hand = "L"
        
    answer = ''
    last_Left_key = 10
    last_right_key = 12
    
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
        
    for i in numbers:
        if i in left_key:
            answer += "L"
            last_Left_key = i
        elif i in right_key:
            answer += "R"
            last_right_key = i
        else :
            i = 11 if i == 0 else i
            absLeft = sum(divmod(abs(i - last_Left_key), 3))
            absRight = sum(divmod(abs(i - last_right_key), 3))
            if absLeft < absRight:
                answer += "L"
                last_Left_key = i
            elif absLeft > absRight:
                answer += "R"
                last_right_key = i
            elif absLeft == absRight and hand == "R":
                answer += hand
                last_right_key = i
            elif absLeft == absRight and hand == "L":
                answer += hand
                last_Left_key = i
                
    return answer



if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    solution(numbers, hand)