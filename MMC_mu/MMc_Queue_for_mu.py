import numpy as np
import matplotlib.pyplot as plt
import os

class ServerDesk:
    def __init__(self):
        self.end_time=0
    
class MMc:
    
    def __init__(self,run_rounds = 10,total_service_time=0,server_time_mean = 2,customers=300,mu_rate=0.5,desks=4,lambda_rates=5):
        
        self.total_service_time=total_service_time
        self.server_time_mean=server_time_mean
        self.customers=customers
        self.desks_num=desks
        self.arrival_time=None
        self.service_time=None
        self.start_time=np.zeros(self.customers)
        self.end_time=np.zeros(self.customers)
        self.desks=[ServerDesk() for _ in range(desks)]
        #self.mu_rate=mu_rate
        self.round=run_rounds
        self.total_work_time=np.zeros(run_rounds+1)
        self.total_bolcking_time=np.zeros(run_rounds+1)
        self.lambda_rates=lambda_rates
        
    def plots(self,x,y,title,y_label):
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, marker='o')
            plt.title(title)
            plt.xlabel('mu Rates')
            plt.ylabel(y_label)
            plt.grid(True)
            if not os.path.exists('MMC_mu_plots'):
                os.makedirs('MMC_mu_plots')
            plt.savefig(f'MMC_mu_plots/{title}.png')
            
            
    def analyze(self,mu_rates,num_repetitions):
        
        overall_average_waiting_times=[]
        overall_average_queue_length=[]
        overall_system_utilization=[]
        overall_response_time=[]
        
        for rate in mu_rates:
            
            #Initialize array for each indicator
            average_waiting_times=np.zeros(num_repetitions)
            average_queue_length=np.zeros(num_repetitions)
            system_utilization=np.zeros(num_repetitions)
            response_time=np.zeros(num_repetitions)
            
            for n in range(num_repetitions):
                self.inital(rate)
                per_average_waiting_time, per_average_queue_length, per_system_utilization,\
                    per_response_time = self.queue()
                
                #Average Waiting Time
                average_waiting_times[n]=per_average_waiting_time
                #Average Queue Length
                average_queue_length[n]=per_average_queue_length
                #System Utilization
                system_utilization[n]=per_system_utilization
                #Response Time
                response_time[n]=per_response_time
            
            overall_average_waiting=np.mean(average_waiting_times)
            overall_average_waiting_times.append(overall_average_waiting)
            
            overall_average_queue=np.mean(average_queue_length)
            overall_average_queue_length.append(overall_average_queue)
            
            overall_sys_utilization =np.mean(system_utilization)
            overall_system_utilization.append(overall_sys_utilization)
            
            overall_rep_time=np.mean(response_time)
            overall_response_time.append(overall_rep_time)
        
        self.plots(mu_rates, overall_average_waiting_times, "Overall Average Waiting Times", "Average Waiting Time")
        self.plots(mu_rates, overall_average_queue_length, "Overall Average Queue Length", "Average Queue Length")
        self.plots(mu_rates, overall_system_utilization, "Overall System Utilization", "System Utilization")
        self.plots(mu_rates, overall_response_time, "Overall Response Time", "Response Time")


        
            
    def queue(self):
        response_time = 0
        queue_lengths=[]
        total_waiting_time=0
        total_system_utilization=0
        wait_time=0
        total_simulation_time=0
        total_busy_time_per_desk=[0 for _ in range(self.desks_num)]
        total_response_time=0
        
        for i in range(self.customers):
            next_desk = min(self.desks,key=lambda desks: desks.end_time)
            desk_index = self.desks.index(next_desk) 
            if next_desk.end_time>self.arrival_time[i]:
                start_time = next_desk.end_time
                wait_time=next_desk.end_time-self.arrival_time[i]
                
                total_waiting_time+=wait_time
                
            else:
                start_time=self.arrival_time[i]
                
            end_time = start_time+self.service_time[i]
            
            self.start_time[i]=start_time
            next_desk.end_time=end_time
            self.end_time[i] = end_time
            response_time=self.end_time[i]-self.arrival_time[i]
            
            total_response_time+=response_time
            total_busy_time_per_desk[desk_index]+=self.service_time[i]
            total_simulation_time=max(total_simulation_time,self.end_time[i])
            
            
            current_queue_length = sum(desk.end_time > self.arrival_time[i] for desk in self.desks)
            print(f"Current queue length at customer {i}: {current_queue_length}")  # 调试输出
            queue_lengths.append(current_queue_length)
            
        per_average_waiting_time=total_waiting_time/self.customers
        per_average_queue_length = np.mean(queue_lengths)
        for busy_time in total_busy_time_per_desk:
            total_system_utilization+=busy_time/total_simulation_time
            
        per_system_utilization=total_system_utilization/self.desks_num
        per_response_time=total_response_time/self.customers
        
        return(per_average_waiting_time, per_average_queue_length, per_system_utilization,\
            per_response_time)
    
    
    def inital(self,rate):
        # Generate a random number following a Poisson distribution
        arrival = np.random.exponential(1/self.lambda_rates,self.customers)
        self.service_time=np.random.exponential(1/rate,self.customers)
        self.arrival_time=np.cumsum(arrival)
        
        

    def main(self,lambda_rates,num_repetitions):
        self.analyze(lambda_rates, num_repetitions)
            
            
if __name__=='__main__':
    mu_rates= [.25,.5,.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75,4,4.25,4.5,4.75,5.5,6,6.5,7,7.5,8,8.5,9]
    num_repetitions=20
    mmc=MMc()
    mmc.main(mu_rates,num_repetitions)