# from KernelsGenerator import KernelsGenerator
import math
import matplotlib.pyplot as plt
import matplotlib.animation as anim


class Distributions():

    def __init__(self):
        self.Iteration = 20001
        self.q = 127773
        self.a = 16807
        self.r = 2836
        f = open("./Kernels.txt", 'r')
        self.data = f.readlines()
        f.close()

        # o=[]
        # for i in range(500000):
        # o.append(self.GetBLoodReturnTime())
        # print(o)
        # plt.hist(o, 100, density=False, facecolor='g', alpha=0.2)
        # plt.xlabel('Smarts')
        # plt.ylabel('Probability')
        # plt.title('Histogram')
        # plt.show()

    def Generate(self):
        # data = np.genfromtxt("./Kernels.txt",delimiter=",")

        # print(data)
        x = int(self.data[self.Iteration])
        # print(x)
        self.h = int(x / self.q)
        qh = self.q*self.h
        xqh = x-qh
        axqh = self.a*xqh
        result = axqh-(self.r*self.h)
        result = int((self.a * (x - qh)) - (self.r * self.h))
        if (result < 0):
            result = result + 2147483647
        self.Iteration += 1
        return int(result)

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

    def GetBLoodReturnTime(self):  # convert to
        Value = self.Generate()

        result = float((100*((float(Value) / 100) % 1)/1.98))+150
        return result

    def GetExponential(self, average):
        Value = self.GetUniform()
        while(Value == 0):
            Value = self.GetUniform()
        Value = -average * math.log(Value)
        return Value

    def GetNormal(self):
        sum = float(0)
        for i in range(10):
            r = self.Generate()
            # x=int(r)
            r = (r/100) % 1
            sum = sum+r
        result = float(((sum - 5) / (math.sqrt(100/12))) + 500)
        return result

# Distributions()
