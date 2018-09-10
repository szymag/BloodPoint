<<<<<<< HEAD
# from KernelsGenerator import KernelsGenerator
import math
class Distributions():
    

    def __init__(self):
        self.Iteration=20001
        self.q=127773
        self.a=16807
        self.r=2836
        f = open("./Kernels.txt", 'r')
        self.data = f.readlines()
        f.close()
        # self.KernelsGenerator = KernelsGenerator()
        pass
    def Generate(self):
        # data = np.genfromtxt("./Kernels.txt",delimiter=",")

   

        # print(data)
        x =int(self.data[self.Iteration])
        # print(x)
        self.h = int(x / self.q)
        qh = self.q*self.h
        xqh=x-qh
        axqh=self.a*xqh
        result=axqh-(self.r*self.h)
        result = int((self.a * (x - qh)) - (self.r * self.h))
        if (result < 0):
            result = result + 2147483647
        self.Iteration+=1
        return result
        
    def GetGeometric(self):
        i=0
        flag=False
        GeometricValue = self.Generate()
        while (flag != True):
            flag = self.Bernouli(GeometricValue)
            if (flag!= True):
                i+=1
            GeometricValue= self.Generate()
        return i

    def GetUniform(self):
        Value = self.Generate()
        result = (float(Value) / 100) % 1
        return result

    def Bernouli(self,randomVariable):
        BernouliValue = self.GetUniform()
        if (BernouliValue < 0.2): #W=0.2 wynika ze sredniej potrzebnej do tego zadania
            return True
        else:
            return False

    def GetUniformToEnlagmnet(self):
        Value = self.Generate()
        result = (Value / 6) % 5
        return result

    def GetExponential(self,average):
        Value = self.GetUniform()
        while(Value==0):
            Value = self.GetUniform()
        Value = -average * math.log(Value)
        return Value

    def GetNormal(self):
        sum = 0 
        for i in range(10):
            r=float(self.Generate())
            x=int(r)
            r=(r/100)%1
            sum=sum+r
        result = ((( sum - 5) / (math.sqrt(100/12))) +500 )
        return result
=======
import KernelsGenerator
class Distributions():
    def __init__(self):
        self.KernelsGenerator = KernelsGenerator.KernelsGenerator()
        pass

    def GetGeometric(self):
        i=0
        flag=False
        GeometricValue = self.KernelsGenerator.Generate()
        while (flag != True):
            flag = self.Bernouli(GeometricValue)
            if (flag!= True):
                i+=1
            GeometricValue= self.KernelsGenerator.Generate()
        return i

    def GetUniform(self):
        Value = self.KernelsGenerator.Generate()
        result = (Value / 100) % 1
        return result

    def Bernouli(self,randomVariable):
        BernouliValue = self.GetUniform()
        if (BernouliValue < 0.2): #W=0.2 wynika ze sredniej potrzebnej do tego zadania
            return True
        else:
            return False
>>>>>>> 4f4fc14c96e7c6c9d79354c4f43045ef07401993
