import numpy as np

class ServerDesk:
    def __init__(self):
        self.end_time=0

class MGc:
    
    def __init__(self,lambda_rate = 5,total_service_time=0,server_time_mean = 2,service_time_std=0.5,customers=10000,desks=2):
        self.lambda_rate=lambda_rate
        self.total_service_time=total_service_time
        self.server_time_mean=server_time_mean
        self.service_time_std=service_time_std
        self.customers=customers
        self.arrival_time=None
        self.service_time=None
        self.start_time=np.zeros(self.customers)
        self.end_time=np.zeros(self.customers)
        self.desks=[ServerDesk() for _ in range(desks)]
        
        
    def queue(self):
        
        for i in range(self.customers):
            next_desk = min(self.desks,key=lambda desks: desks.end_time)
            start_time = max(next_desk.end_time,self.arrival_time[i])
            end_time = start_time+self.service_time[i]
            
            self.start_time[i]=start_time
            next_desk.end_time=end_time
            self.end_time[i] = end_time
            
        self.total_work_time=max(desk.end_time for desk in self.desks)
            
    def inital(self):
        
        # Generate a random number following a Poisson distribution
        arrival = np.random.exponential(1/self.lambda_rate,self.customers)
        service = np.random.normal(self.server_time_mean,self.service_time_std,self.customers)
        
        self.service_time=np.clip(service,0,None)
        self.arrival_time=np.cumsum(arrival)
        
        
        
    def main(self):
        
        self.inital()
        self.queue()
        print(self.total_work_time)
        
        
if __name__=='__main__':
    mgc=MGc()
    mgc.main()