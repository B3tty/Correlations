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


def check_correlation(experimentA: Experiment, experimentB: Experiment, population: int):
    usersA1 = []
    usersA2 = []

    varB1 = 0
    varB2 = 0

    for i in range(1, population):
        user = User(i)
        var = experimentA.assign(user)
        if var.name == "variation1":
            usersA1.append(user)
        else:
            usersA2.append(user)

    for user in usersA1:
        var = experimentB.assign(user)
        if var.name == "variation1":
            varB1 += 1
        else:
            varB2 += 1

    print(f"Users in variation B1 in A1: {varB1} or {varB1 / len(usersA1) * 100}% of people in var A1")

    for user in usersA2:
        var = experimentB.assign(user)
        if var.name == "variation1":
            varB1 += 1
        else:
            varB2 += 1

    print(f"Users in variation B1 in total: {varB1} or {varB1 / population * 100}% ot total population")


# MD5
print("--------- MD5 ---------")
expA_md5 = init_experiment(Md5Hasher())
expB_md5 = init_experiment(Md5Hasher())
check_repartition(expA_md5, 10000)
check_correlation(expA_md5, expB_md5, 100000)

# Built In Hash
print("--------- Built In Hash Function ---------")
expA_bi = init_experiment(BuiltInHasher())
expB_bi = init_experiment(BuiltInHasher())
check_repartition(expA_bi, 10000)
check_correlation(expA_bi, expB_bi, 100000)

# # SHA256
# print("--------- SHA256 ---------")
# expA_sha256 = init_experiment(Sha256Hasher())
# expB_sha256 = init_experiment(Sha256Hasher())
# check_repartition(expA_sha256, 10000)
# check_correlation(expA_sha256, expB_sha256, 1000000)

