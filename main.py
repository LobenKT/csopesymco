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
    # Placeholder for SJF implementation
    pass

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
