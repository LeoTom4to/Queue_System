# Queue_System For M/M/1

initialization:
  - Set arrival rate λ (number of customers arriving per hour)
  - Set service rate μ (number of customers served per hour)
  - Initialize an empty queue
  - Initialize the current time to 0
  - Initialize wait time to 0
  - Initialize service end time to 0 (time when the current service will be completed)

Loop until simulation ends:
    1. Calculate the arrival time of the next customer using exponential distribution with rate λ.
    
    2. If the queue is empty and current time >= service end time:
          - The next customer goes directly to the service window.
          - Calculate the service end time for this customer using current time + service duration (from exponential distribution with rate μ).
       otherwise:
          - Add the next customer to the queue.
    
    3. If the current time >= service end time and the queue is not empty:
          - Remove the next customer from the queue.
          - Calculate the service end time for this customer using current time + service duration.
          - Calculate the wait time for this customer (current time - arrival time).
          - Accumulate the wait time to calculate the average later.
    
    4. Update current time to the arrival time of the next customer.
    
    5. Record data such as waiting time and queue length.

Calculate summary statistics:
    - Calculate average waiting time.
    - Calculate average queue length.
    - Calculate server utilization.


# Queue_System For M/G/1


initialization:
    - Set arrival rate λ (number of customers arriving per hour)
    - Define the service time distribution (could be any general distribution)
    - Initialize an empty queue
    - Initialize the current time to 0
    - Initialize wait time to 0
    - Initialize service end time to 0 (time when the current service will be completed)

Loop until simulation ends:
    1. Calculate the arrival time of the next customer using exponential distribution with rate λ.

    2. If the queue is empty and current time >= service end time:
          - The next customer goes directly to the service window.
          - Calculate the service end time for this customer using current time + service duration (from the general distribution).
       otherwise:
          - Add the next customer to the queue.
    
    3. If the current time >= service end time and the queue is not empty:
          - Remove the next customer from the queue.
          - Calculate the service end time for this customer using current time + service duration (from the general distribution).
          - Calculate the wait time for this customer (current time - arrival time).
          - Accumulate the wait time to calculate the average later.

    4. Update current time to the arrival time of the next customer or to the service end time if it comes first.
    
    5. Record data such as waiting time, queue length, and service times.

Calculate summary statistics:
    - Calculate average waiting time.
    - Calculate average queue length.
    - Calculate server utilization.
    - Analyze the distribution of service times.
