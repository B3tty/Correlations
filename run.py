from user import User
from experiment import *
from md5 import Md5Hasher


expA = Experiment()
expA.hasher = Md5Hasher()

for i in range(1, 10):
    user = User(i)
    expA.assign(user)

