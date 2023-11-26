def solution(arr):
    """
    - 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/68936
    - 정답 : O
    - 해설

    분할 정복으로 풀이
    """

    global zeroCount, oneCount

    zeroCount = 0
    oneCount = 0

    def devideAndConquer(rowStartIdx: int,
                         colStartIdx: int,
                         length: int):
        global zeroCount, oneCount

        # 조건 충족 시, 합산해서 +1
        # 조건 미충족 시, 다시 deviceAndConquer

        firstValue = arr[rowStartIdx][colStartIdx]

        for rowIdx in range(rowStartIdx, rowStartIdx + length):
            for colIdx in range(colStartIdx, colStartIdx + length):
                if arr[rowIdx][colIdx] != firstValue:
                    length = length // 2

                    devideAndConquer(rowStartIdx=rowStartIdx,
                                     colStartIdx=colStartIdx,
                                     length=length)
                    devideAndConquer(rowStartIdx=rowStartIdx,
                                     colStartIdx=colStartIdx+length,
                                     length=length)
                    devideAndConquer(rowStartIdx=rowStartIdx+length,
                                     colStartIdx=colStartIdx,
                                     length=length)
                    devideAndConquer(rowStartIdx=rowStartIdx+length,
                                     colStartIdx=colStartIdx+length,
                                     length=length)
                    return

        if firstValue == 0:
            zeroCount = zeroCount + 1
        if firstValue == 1:
            oneCount = oneCount + 1

    devideAndConquer(rowStartIdx=0,
                     colStartIdx=0,
                     length=len(arr))

    return (zeroCount, oneCount)
