import heapq

def get_user_input(file=None):
    """
    This function gets and validates the user input according to the specifications.
    """
    while True:
        try:
            # Input format: X Y Z (algorithm, number of processes, time quantum)
            if (file == None):
                x, y, z = map(int, input("Enter X Y Z: ").split())
                print(f"You entered: X={x} (scheduling algorithm), Y={y} (number of processes), Z={z} (time quantum). Now, please enter details for {y} processes:")
            else:
                with open(file, 'r') as f:
                    x, y, z = map(int, f.readline().split())
            
            # If the CPU scheduling algorithm indicated by the value of x is not the Round-Robin algorithm, 
            # z value must be set to 1
            if x != 3:
                z = 1
            
            # Validate inputs
            if x not in [0, 1, 2, 3] or not (3 <= y <= 100) or not (1 <= z <= 100):
                raise ValueError("Invalid input. Please adhere to the constraints.")
            
            # Get process details
            processes = []
            if (file == None):
                print(f"Enter {y} lines of A B C (process ID, arrival time, burst time):")
                for _ in range(y):
                    a, b, c = map(int, input().split())
                    processes.append((a, b, c))
            else:
                with open(file, 'r') as f:
                    f.readline() # Skip the first line
                    for _ in range(y):
                        a, b, c = map(int, f.readline().split())
                        processes.append((a, b, c))
            
            return x, y, z, processes
        except (FileNotFoundError, ValueError) as e:
            print("ERROR: ", e)
            if file is not None:
                return
            # If there's an error, loop back for correct input
            continue

#  simulate inputs for testing.
def simulate_user_input(inputs):
    """
    Simulates user input from a list of predefined inputs for demonstration.
    """
    def input(prompt):
        print(prompt, end='')
        return inputs.pop(0)
    
    return get_user_input()

# Example inputs for testing
inputs = [
    "0 3 1",  # FCFS, 3 processes, time quantum (ignored)
    "1 0 5",  # Process 1: Arrival time 0, Burst time 5
    "2 1 3",  # Process 2: Arrival time 1, Burst time 3
    "3 2 1",  # Process 3: Arrival time 2, Burst time 1
]


#TODO: Implement the scheduling algorithms below
def fcfs(processes):
    """First-Come-First-Serve Scheduling, conforming to specified input-output format."""
    processes.sort(key=lambda x: x[1])  # Sort by arrival time

    current_time = 0
    total_waiting_time = 0
    process_output = []

    for pid, arrival_time, burst_time in processes:
        if current_time < arrival_time:
            current_time = arrival_time
        start_time = current_time
        end_time = start_time + burst_time
        waiting_time = start_time - arrival_time
        total_waiting_time += waiting_time
        
        process_output.append((start_time, pid, end_time, waiting_time))
        current_time += burst_time
    
    # Ensuring the output is sorted by start time, although it should already be in order due to FCFS nature
    for start_time, pid, end_time, waiting_time in sorted(process_output):
        print(f"P[{pid}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time}")

    average_waiting_time = total_waiting_time / len(processes)
    print(f"Average waiting time: {average_waiting_time:.2f}")

def sjf(processes):
    """Shortest-Job First Scheduling."""
    curr_time = 0 # Initialize time counter
    ready = [] # Ready queue
    terminated = [] # Terminated processes
    gantt = [] # Gantt chart using non-preemptive
    avg = 0 # Average waiting time
    result = [] # Container for the result
    
    # Sort processes based on arrival time and then burst time
    processes.sort(key= lambda x: (x[1], x[2])) 

    # Loop while not all processes have been terminated
    while (len(terminated) != len(processes)):
        # Add processes to ready queue if they have arrived
        for process in processes:
            if process[1] <= curr_time and process not in ready and process not in terminated:
                ready.append(process)
        
        # Sort the ready queue based on burst time
        # If burst time is equal, sort by arrival time
        # If arrival time is equal, sort by pid
        ready.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)

        # If ready queue is not empty, execute the next process
        # Record their start, end, and wait times
        if (ready):
            pid, arrival, burst = ready.pop()
            start_time = curr_time
            end_time = curr_time + burst
            wait_time = curr_time - arrival
            curr_time = end_time
            terminated.append((pid, arrival, burst))
            gantt.append((pid, start_time, end_time, wait_time, curr_time))

    # Sort the gantt chart so it can be used for printing      
    # Sort based on start time  
    gantt.sort(key = lambda x: (x[1]))

    # Print
    for i in gantt:
        result.append(f"P[{i[0]}] Start time: {i[1]} End time: {i[2]} | Waiting time: {i[3]}")
        avg += i[3]
    result.append(f"Average waiting time: {avg / len(processes):.2f}")
    print('\n'.join(result))
    return result

def srtf(processes):
    """Shortest-Remaining-Time-First Scheduling."""
    priority_queue = []  # Store processes based on remaining burst time
    heapq.heapify(priority_queue)  # List to heap

    curr_time = 0  
    finished_processes = []  # Store completed processes
    total_waiting_time = 0  # Calc total waiting time

    # Extract algorithm config
    _, y, _ = processes.pop(0)

    while processes or priority_queue:
        # Check for new arrivals and add them to priority_queue
        while processes and processes[0][0] <= curr_time:
            arrival_time, burst_time, process_id = processes.pop(0)
            heapq.heappush(priority_queue, (burst_time, arrival_time, process_id))

        if priority_queue:
            # Select  process with the shortest remaining burst time
            burst_time, arrival_time, process_id = heapq.heappop(priority_queue)

            start_time = max(curr_time, arrival_time)  # Start time of the process
            end_time = start_time + 1  # End time of the process

            # Update waiting time for finished processes
            total_waiting_time += start_time - arrival_time

            # Execute the process for one time unit
            burst_time -= 1
            curr_time += 1

            if burst_time > 0:
                heapq.heappush(priority_queue, (burst_time, arrival_time, process_id))  # Return to priority_queue for future execution
            else:
                finished_processes.append((process_id, start_time, end_time))  # Process done
                print(f"P[{process_id}] start time: {start_time} end time: {end_time} | Waiting time: {start_time - arrival_time}")

        else:
            curr_time += 1  # If no process is currently executing, go to the next unit of time

    # Calculate average waiting time
    if finished_processes:
        average_waiting_time = total_waiting_time / len(finished_processes)
        print(f"Average waiting time: {average_waiting_time:.2f}")
    else:
        print("No processes completed.")

    return finished_processes, average_waiting_time


def rr(processes, time_quantum):
  """round-robin scheduling."""
  n = len(processes)

  pdict = {p[0]: [p[1], p[2], 0] for p in processes}

  # initialize queue with the first process, assuming no leading waiting time
  # one process shall be ensured to start at 0ms
  queue = [processes[0][0]]
  start_time = 0
  end_time = 0

  # main scheduling loop
  while queue:
      # get the next process from the queue
      id = queue.pop(0)

      # execute the process for the time quantum or until completion
      if pdict[id][1] > 0:
          if pdict[id][1] >= time_quantum:
              end_time += time_quantum
              pdict[id][1] -= time_quantum
          else:
              end_time += pdict[id][1]
              pdict[id][1] = 0

          # update queue with processes that arrived during the execution of the current process
          for j in range(n):
              x, y, z = processes[j]
              if x not in queue and x != id and y <= end_time:
                  queue.append(x)

          # update waiting time anddict[id][2]al time for the current process
          pdict[id][2] += start_time - pdict[id][0]
          pdict[id][0] = end_time

          # print process details
          print(f"P[{id}] start time: {start_time} end time: {end_time} | Waiting time: {pdict[id][2]}")

          # update start time for the next process
          start_time = end_time

          # add the current process back to the queue if it is not completed
          queue.append(id)

  # calculate and print the average waiting time
  avg_waiting_time = sum(p[2] for p in pdict.values()) / n
  print(f"Average waiting time: {avg_waiting_time}")

def main():
    # Choose if Manual Input or File Input
    while True:
        input_type = input("Choose an Input Type:\n[1] Manual Input \n[2] File Input\nAnswer: ").strip()
        if input_type in ['1', '2']:
            break
        else:
            print("Invalid input. Please enter 1 or 2.\n- - - - - - - - - - - - -")
    
    if (input_type == '1'):
        x, y, z, processes = get_user_input()
    else:
        filename = input("Specify the file name: ")
        x, y, z, processes = get_user_input(filename)

    # x, y, z, processes = simulate_user_input(inputs)  # For testing purposes

    print("Algorithm Config (XYZ): ", x, y, z) # For testing purposes
    print("The processes are: ", processes) # For testing purposes
    
    # Select and execute the scheduling algorithm based on user input
    if x == 0:
        fcfs(processes)
    elif x == 1:
        sjf(processes)
    elif x == 2:
        srtf(processes)
    elif x == 3:
        rr(processes, z)
    else:
        print("Invalid scheduling algorithm selected.")

if __name__ == "__main__":
    main()
