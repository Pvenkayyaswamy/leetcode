class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        vertices = [0] * n
        for i in range(0,n):
            for j in range(i,n):
                if i==j:
                    continue
                else:
                    if matrix[i][j] == 1:
                        vertices[i] = vertices[i]+1
                        vertices[j] = vertices[j]+1
        return vertices
