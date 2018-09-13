import math

import matplotlib.animation as anim
import matplotlib.pyplot as plt


class Distributions():

    def __init__(self):
        self.Iteration = 20001
        f = open("./Kernels.txt", 'r')
        self.data = f.readlines()
        f.close()

        # o = []
        # for i in range(6000):
        #     o.append(self.get_exponential(1700))
        # # print(o)
        # plt.hist(o, 50, density=True, facecolor='g', alpha=0.2)
        # plt.xlabel('Smarts')
        # plt.ylabel('Probability')
        # plt.title('Histogram')
        # plt.show()

    def Generate(self):
        q = 44488
        a = 48271
        r = 3399
        x = int(self.data[self.Iteration])
        h = int(x / q)
        result = int((a * (x - (q*h))) - (r * h))
        if(result < 0):
            result = result + 2147483647
        self.Iteration += 1
        return result

    def GetBloodType(self):
        Value = self.Generate()
        result = ((float(Value) / 100) % 1)*100
        if(result <= 60):
            result = "A"
        else:
            result = "B"
        return result

    def GetGeometric(self):
        i = int(0)
        flag = False
        GeometricValue = self.Generate()
        while (flag != True):
            flag = self.Bernouli(GeometricValue)
            if (flag != True):
                i += 1
            GeometricValue = self.Generate()
        return i

    def GetUniform(self):
        Value = self.Generate()
        result = (float(Value) / 100) % 1
        return result

    def Bernouli(self, randomVariable):
        BernouliValue = self.GetUniform()
        if (BernouliValue < 0.2):  # W=0.2 wynika ze sredniej potrzebnej do tego zadania
            return True
        else:
            return False

    def GetBLoodReturnTime(self):
        Value = self.Generate()
        result = float((100*((float(Value) / 100) % 1)/1.98))+150
        return result

    def get_exponential(self, average):
        Value = self.GetUniform()
        while(Value == 0):
            Value = self.GetUniform()
        return(-average * math.log(Value))

    def get_normal(self):
        sum_i = 0.0
        for _i in range(10):
            sum_i += (self.Generate()/100) % 1
        return float(((sum_i - 5) / (math.sqrt(100/12))) + 500)


a = Distributions()
