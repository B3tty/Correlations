from user import User
from experiment import *
from hasher_implems import *



def init_experiment(hasher: Hasher):
    exp = Experiment()
    exp.hasher = hasher
    return exp

def check_repartition(experiment: Experiment, population: int):
    var1 = 0
    var2 = 0

    for i in range(1, population):
        user = User(i)
        var = experiment.assign(user)
        if var.name == "variation1":
            var1 += 1
        else:
            var2 += 1
    print(f"Users in variation 1: {var1} or {var1 / population * 100}%")
    print(f"Users in variation 2: {var2} or {var2 / population * 100}%")


expA = init_experiment(Md5Hasher())
check_repartition(expA, 10000)

expB = init_experiment(Sha256Hasher())
check_repartition(expB, 10000)

