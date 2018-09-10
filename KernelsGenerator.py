<<<<<<< HEAD
import numpy as np

class KernelsGenerator:
    Iteration=20001
    q=127773
    a=16807
    r=2836
    # def __init__(self):
    #     pass
    def Generate(self):
        # data = np.genfromtxt("./Kernels.txt",delimiter=",")

        f = open("./Kernels.txt", 'r')
        data = f.readlines()
        f.close()

        # print(data)
        x =int(data[self.Iteration])
        # print(x)
        self.h = x / self.q
        result = self.a * (x - (self.q * self.h)) - self.r * self.h
        if (result < 0):
            result = result + 2147483647
        self.Iteration+=1
=======
import numpy as np

class KernelsGenerator:
    Iteration=20001
    q=127773
    a=16807
    r=2836
    def __init__(self):
        pass
    def Generate(self):
        data = np.genfromtxt("./Kernels.txt",delimiter=",")
        # print(data)
        x =int(data[self.Iteration])
        self.h = x / self.q
        result = self.a * (x - (self.q * self.h)) - self.r * self.h
        if (result < 0):
            result = result + 2147483647
        self.Iteration+=1
>>>>>>> 4f4fc14c96e7c6c9d79354c4f43045ef07401993
        return result