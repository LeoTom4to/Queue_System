# Queue Systems Simulation

## M/M/1 Queue System

### Initialization
- Set arrival rate λ (number of customers arriving per hour).
- Set service rate μ (number of customers served per hour).
- Initialize an empty queue.
- Initialize the current time to 0.
- Initialize wait time to 0.
- Initialize service end time to 0 (time when the current service will be completed).

### Simulation Loop
Run until the simulation ends:
1. **Calculate Arrival Time:** Calculate the arrival time of the next customer using exponential distribution with rate λ.
2. **Queue or Serve:** 
   - If the queue is empty and current time >= service end time, send the customer directly to the service window and calculate the service end time.
   - Otherwise, add the customer to the queue.
3. **Service Completion:** 
   - If the service end time <= the arrival time of the next customer and the queue is not empty, remove the customer from the queue, serve the next customer, and update the service end time.
4. **Update Time:** Update the current time to the arrival time of the next customer.
5. **Record Data:** Record data such as waiting time and queue length.

### Summary Statistics
- Calculate the average waiting time.
- Calculate the average queue length.
- Calculate server utilization.

---

## M/G/1 Queue System

### Initialization
- Set arrival rate λ (number of customers arriving per hour).
- Define the service time distribution (can be any general distribution).
- Initialize an empty queue.
- Initialize the current time to 0.
- Initialize wait time to 0.
- Initialize service end time to 0 (time when the current service will be completed).

### Simulation Loop
Run until the simulation ends:
1. **Calculate Arrival Time:** Calculate the arrival time of the next customer using exponential distribution with rate λ.
2. **Queue or Serve:** 
   - If the queue is empty and current time >= service end time, send the customer directly to the service window and calculate the service end time.
   - Otherwise, add the customer to the queue.
3. **Service Completion:** 
   - If the current time >= service end time and the queue is not empty, remove the customer from the queue, serve the next customer, and update the service end time.
4. **Update Time:** Update the current time to the arrival time of the next customer or to the service end time if it comes first.
5. **Record Data:** Record data such as waiting time, queue length, and service times.

### Summary Statistics
- Calculate the average waiting time.
- Calculate the average queue length.
- Calculate server utilization.
- Analyze the distribution of service times.
