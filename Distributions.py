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