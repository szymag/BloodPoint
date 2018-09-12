class BloodUnit():
    _BloodId=0
    def __init__(self,tempTime):
        self.ID=BloodUnit._BloodId
        self.ExpirationDate = tempTime
        BloodUnit._BloodId+=1
        
        
        
