class BloodUnit():
    
    def __init__(self,system,tempTime):
        system.BDPoint.BloodId+=1
        self.ExpirationDate = tempTime
        self.ID=system.BDPoint.BloodId
        
