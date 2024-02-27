def get_user_input(file=None):
    """
    This function gets and validates the user input according to the specifications.
    """
    while True:
        try:
            # Input format: X Y Z (algorithm, number of processes, time quantum)
            if (file == None):
                x, y, z = map(int, input("Enter X Y Z: ").split())
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
    """First-Come-First-Serve Scheduling."""
    # Placeholder for FCFS implementation
    pass

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
    # Placeholder for SRTF implementation
    pass

def rr(processes, time_quantum):
    """Round-Robin Scheduling."""
    # Placeholder for RR implementation
    pass

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
