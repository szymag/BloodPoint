class BloodUnit():
    
    def __init__(self,system,tempTime):
        system.BloodNumber+=1
        self.ExpirationDate = tempTime
        self.ID=system.BloodNumber
        
