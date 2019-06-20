from user import User
from experiment import *
from md5hasher import Md5Hasher


expA = Experiment()
expA.hasher = Md5Hasher()

for i in range(1, 10):
    user = User(i)
    var = expA.assign(user)
    print(f"user {i} in variation {var.name}")

