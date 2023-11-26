# 오답
def calcMaxSumInTreeDFS(
    triangle,
    
    depth: int = 0,
    maxTriangle: int = 0,
    
    befPointer: int = 0,
    accPointer: list = [],
) -> list:
    
    if depth > len(triangle) - 1:
        return max(maxTriangle, sum(accPointer))
    
    copiedAccPointer = accPointer.copy()
    copiedAccPointer.append(triangle[depth][befPointer])
    
    
    leftTreeSum = calcMaxSumInTreeDFS(triangle=triangle,
                                depth=depth+1,
                                maxTriangle=maxTriangle,
                                befPointer=befPointer,
                                accPointer=copiedAccPointer)
    rightTreeSum = calcMaxSumInTreeDFS(triangle=triangle,
                                depth=depth+1,
                                maxTriangle=maxTriangle,
                                befPointer=befPointer + 1,
                                accPointer=copiedAccPointer)
    
    return max(leftTreeSum, rightTreeSum)

def solution(triangle):
    """
    - 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43105
    - 정답 : X
    - 해설
    
    성능 및 효율성 문제에서 실패함
    아래와 같이 생긴 triangle의 깊이는 500까지 될 수 있습니다. 
    이 경우 DFS 방식으로 코드를 연산하면 성능 이슈가 발생할 수 있습니다.
    따라서 **반복문을 사용한 동적 프로그래밍 기법** 이용해서 풀어야 합니다.
    
    triangle	result
    [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
    """
    return calcMaxSumInTreeDFS(triangle=triangle)