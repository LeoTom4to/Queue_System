import numpy as np

class MM1:
    
    def __init__(self,lambda_rate = 5,total_service_time=0,server_time_mean = 2,customers=10000,mu_rate=0.5):
        self.lambda_rate=lambda_rate
        self.total_service_time=total_service_time
        self.server_time_mean=server_time_mean
        self.customers=customers
        self.arrival_time=None
        self.service_time=None
        self.start_time=np.zeros(self.customers)
        self.end_time=np.zeros(self.customers)
        self.mu_rate=mu_rate
        
    def queue(self):
        
        for i in range(self.customers):
            if i==0:
                self.start_time[i]=self.arrival_time[i]
            else:
                self.start_time[i]=max(self.end_time[i-1],self.arrival_time[i])
            self.end_time[i]=self.start_time[i]+self.service_time[i]
            
    def inital(self):
        
        # Generate a random number following a Poisson distribution
        arrival = np.random.exponential(1/self.lambda_rate,self.customers)
        self.service_time=np.random.exponential(1/self.mu_rate,self.customers)
        self.arrival_time=np.cumsum(arrival)
        
        
        
    def main(self):
        self.inital()
        self.queue()
        print(self.end_time[99])
        
            
            
if __name__=='__main__':
    mm1=MM1()
    mm1.main()