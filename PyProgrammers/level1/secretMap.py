
'''
 1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
 2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
 3. "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
 4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
 
 
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    
    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    
    
    
    1. 각 배열을 2진수로 만들어 재배열
    2. 이진수를 0이면 " ", 1이면 "#" 으로 바꿔서 재배열
    3. 두 배열을 그대로 합쳐
 
'''

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        arr1[i] = f'{arr1[i]:b}'
        arr2[i] = f'{arr2[i]:b}'
        
        lenArr1 = len(arr1[i])
        lenArr2 = len(arr2[i])
        
        if lenArr1 < n :
            j = n - lenArr1
            arr1[i] = "0" * j + arr1[i]
        arr1[i] = arr1[i].replace("0", " ")
        arr1[i] = arr1[i].replace("1", "#")
        
        if lenArr2 < n :
            j = n - lenArr2
            arr2[i] = "0" * j + arr2[i]
        arr2[i] = arr2[i].replace("0", " ")
        arr2[i] = arr2[i].replace("1", "#")
        
        result = ""
        for j in range(n) :
            if arr1[i][j] == ' ' and arr2[i][j] == ' ' :
                result += " "
            else :
                result += "#"
        answer.append(result)
    return answer

    
def solution1(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
    

if __name__ == '__main__':
    
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    
    print(solution1(n, arr1, arr2))