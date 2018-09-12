
class BloodUnit():
    _BloodId=0
    _BloodA=0
    _BloodB=0
    def __init__(self,BDPoint,tempTime,BloodTypeOrder):
        # self.ID=BloodUnit._BloodId
        # if(BloodTypeOrder=="A" or BloodTypeOrder=="B"):
        self.BloodType=BloodTypeOrder
        # else:
            # self.BloodType=BDPoint.Distributions.GetBloodType()
        self.ExpirationDate = tempTime
        BloodUnit._BloodId+=1
        if(self.BloodType=="A"):
            BloodUnit._BloodA+=1
        else:
            BloodUnit._BloodB+=1
        

        
        
