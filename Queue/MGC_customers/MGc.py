import numpy as np
import matplotlib.pyplot as plt
import os

# Class representing a single server desk.
class ServerDesk:
    def __init__(self):
        self.end_time = 0  # Initialize the end time of service at the desk to 0.
    
# Class for simulating the M/G/c queuing system.
class MGc:
    # Initialize the M/G/c system with given parameters.
    def __init__(self, run_rounds=10, total_service_time=0, customers=300, server_time_mean=2, service_time_std=0.5, desks=6, lambda_rates=5):
        self.total_service_time = total_service_time
        self.server_time_mean = server_time_mean
        self.desks_num = desks
        self.arrival_time = None
        self.service_time = None
        self.desks = [ServerDesk() for _ in range(desks)]  # Create a list of ServerDesk objects.
        self.round = run_rounds
        self.total_work_time = np.zeros(run_rounds + 1)
        self.total_bolcking_time = np.zeros(run_rounds + 1)
        self.lambda_rates = lambda_rates
        self.server_time_mean = server_time_mean
        self.service_time_std = service_time_std
        
    # Function to simulate the queue processing.
    def queue(self, customer_num):
        # Initializing the arrays for start and end times for each customer.
        self.start_time = np.zeros(customer_num)
        self.end_time = np.zeros(customer_num)
        # ... [Rest of the queue function code] ...

    # Function to initialize the simulation with customer arrival and service times.
    def inital(self, customer_num):
        # Generate customer arrival times with Poisson distribution.
        arrival = np.random.exponential(1/self.lambda_rates, customer_num)
        # Generate service times with normal distribution, clipped at 0 to avoid negative service times.
        service = np.random.normal(self.server_time_mean, self.service_time_std, customer_num)
        self.service_time = np.clip(service, 0, None)
        self.arrival_time = np.cumsum(arrival)  # Cumulative sum to get arrival times.
        
    # Function to plot the simulation results.
    def plots(self, x, y, title, y_label):
        # ... [Rest of the plots function code] ...

    # Function to analyze the system performance over multiple repetitions.
    def analyze(self, customers, num_repetitions):
        # ... [Rest of the analyze function code] ...

    # Main function to run the analysis.
    def main(self, customers, num_repetitions):
        self.analyze(customers, num_repetitions)
            
# Entry point of the script.
if __name__ == '__main__':
    # Define the range of customers and the number of repetitions for the simulation.
    customers = [100, 200, 300, ... , 1500]
    num_repetitions = 20
    # Create an instance of the MGc class and run the main function.
    mgc = MGc()
    mgc.main(customers, num_repetitions)
