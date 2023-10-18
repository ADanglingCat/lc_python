# 螺旋矩阵
class Resolution:
    def generateMatrix(self, n):
        ret = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        index, tar = 1, n * n
        while index <= tar:
            # left to right
            for i in range(l, r + 1):
                ret[t][i] = index
                index += 1
            t += 1
            # top to bottom
            for i in range(t, b + 1):
                ret[i][r] = index
                index += 1
            r -= 1
            # right to left
            for i in range(r, l - 1, -1):
                ret[b][i] = index
                index += 1
            b -= 1
            for i in range(b, t - 1, -1):
                ret[i][l] = index
                index += 1
            l += 1
        return ret