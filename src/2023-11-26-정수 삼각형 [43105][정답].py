def solution(triangle):
    """
    - 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43105
    - 정답 : O
    - 해설
    
    기존에 주어진 triangle 자료구조를 그대로 활용하여 문제 풀이
    """

    for rowIdx, rowVal in enumerate(triangle):
        isFirstRow = rowIdx == 0
        if isFirstRow: continue
        
        for colIdx, colVal in enumerate(rowVal):
            isFirstColumn = colIdx == 0
            isLastColumn = colIdx == rowIdx
            if isFirstColumn:
                parentTraingleItem = triangle[rowIdx - 1][colIdx]
                
            elif isLastColumn:
                parentTraingleItem = triangle[rowIdx - 1][colIdx - 1]
                
            else:
                parentTraingleItem = max(triangle[rowIdx - 1][colIdx], triangle[rowIdx - 1][colIdx - 1])
                
            triangle[rowIdx][colIdx] += parentTraingleItem    
        
    lastRow = triangle[len(triangle) - 1]
    maxColum = max(lastRow)
    return maxColum