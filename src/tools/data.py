from ab_test.user import User
from ab_test.experiment import Experiment
from ab_test.hasher import Hasher


class DataHelper:

    @staticmethod
    def generate(hasher: Hasher, population, exp_a_id: int = None):
        if exp_a_id is not None:
            exp_a = Experiment(hasher, f'{2*exp_a_id:06d}')
            exp_b = Experiment(hasher, f'{2*exp_a_id + 1:06d}')
        else:
            exp_a = Experiment(hasher)
            exp_b = Experiment(hasher)

        var_a1_b1 = 0
        var_a1_b2 = 0
        var_a2_b1 = 0
        var_a2_b2 = 0

        for i in range(1, population+1):
            user = User(i)
            var_a = exp_a.assign(user)
            var_b = exp_b.assign(user)

            if var_a.name == "variation1":
                if var_b.name == "variation1":
                    var_a1_b1 += 1
                else:
                    var_a1_b2 += 1
            else:
                if var_b.name == "variation1":
                    var_a2_b1 += 1
                else:
                    var_a2_b2 += 1

        matrix = [[var_a1_b1,         var_a2_b1,         var_a1_b1+var_a2_b1],
                  [var_a1_b2,         var_a2_b2,         var_a1_b2+var_a2_b2],
                  [var_a1_b1+var_a1_b2, var_a2_b1+var_a2_b2, var_a1_b1+var_a2_b1+var_a1_b2+var_a2_b2]]

        return matrix

    @staticmethod
    def display(matrix):
        header = ["/", "ExpA:Var1", "ExpA:Var2", "Sum"]
        array = [header]
        header_row = ["ExpB:Var1", "ExpB:Var2", "Sum"]
        for index, row in enumerate(matrix, start=0):
            new_row = row.copy()
            new_row.insert(0, header_row[index])
            array.append(new_row)

        print('\n'.join([''.join(['{:10}'.format(item) for item in row])
                         for row in array]))
