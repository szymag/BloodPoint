
class BloodUnit():
    _BloodId=0
    _BloodA=0
    _BloodB=0
    def __init__(self,BDPoint,tempTime,BloodTypeOrder,OrderType):
        self.ID=BloodUnit._BloodId
        # if(BloodTypeOrder=="A" or BloodTypeOrder=="B"):
        self.OrderType=OrderType
        self.BloodType=BloodTypeOrder
        self.BloodTime=BDPoint.SystemTime
        # else:
        print("Dodano jednostę krwi, grupy" + self.BloodType + " o ID:" + str(self._BloodId))
            # self.BloodType=BDPoint.Distributions.GetBloodType()
        self.ExpirationDate = tempTime
        BloodUnit._BloodId+=1
        if(self.BloodType=="A"):
            BloodUnit._BloodA+=1
            self.IDA=BloodUnit._BloodA
        else:
            BloodUnit._BloodB+=1
            self.IDB=BloodUnit._BloodB
        

        
        
