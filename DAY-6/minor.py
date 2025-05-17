''' eg of train ticket booking '''


class Train():
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):
        print(f"Ticket is booked on train no {self.trainNo} from {fro} to {to}")
        
t=Train(12233)
t.book("Uk","London")
        