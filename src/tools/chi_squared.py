class ChiSquaredTest:

    @staticmethod
    def expected(matrix, i, j):
        return (matrix[i][2]) * (matrix[2][j]) / matrix[2][2]

    @staticmethod
    def step(matrix, i, j):
        exp = ChiSquaredTest.expected(matrix, i, j)
        case = matrix[i][j]
        # print(f"step {i},{j}: case={case}, exp={exp}")
        return (case - exp) * (case - exp) / exp

    @staticmethod
    def statistic_test(matrix):
        result = 0
        for i in range(0, 2):
            for j in range(0, 2):
                result += ChiSquaredTest.step(matrix, i, j)
        return result
