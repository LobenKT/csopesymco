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
    """First-Come-First-Serve Scheduling."""
    # Placeholder for FCFS implementation
    pass

def sjf(processes):
    """Shortest-Job First Scheduling."""
    # Placeholder for SJF implementation
    pass

def srtf(processes):
    """Shortest-Remaining-Time-First Scheduling."""
    # Placeholder for SRTF implementation
    pass

def rr(processes, time_quantum):
    """round robin scheduling"""
    n = len(processes)
    # sort processes by arrival time then burst time
    processes = sorted(processes, key=lambda x: (x[1], x[2]))

    # initialize lists of arrivals, remaining times, and waiting times
    arrival_time = [process[1] for process in processes]
    remaining_time = [process[2] for process in processes]
    waiting_time = [0 for _ in range(n)]
    result = [] # for testing

    # initialize queue with the first process, assuming no leading waiting time
    # one process shall be ensured to start at 0ms
    queue = [processes[0][0]]
    start_time = 0
    end_time = 0

    # main scheduling loop
    while any(remaining_time):
        # get the next process from the queue
        id = queue.pop(0)

        # iterate through processes to find the current process
        for i in range(n):
            pid = processes[i][0]

            # skip processes until the current one is found
            if id != pid:
                continue

            # execute the process for the time quantum or until completion
            if remaining_time[i] > 0:
                if remaining_time[i] >= time_quantum:
                    end_time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    end_time += remaining_time[i]
                    remaining_time[i] = 0

                # update queue with processes that arrived during the execution of the current process
                for j in range(i+1, n):
                    x, y, z = processes[j]
                    if y <= end_time:
                        queue.append(x)

                # update waiting time and arrival time for the current process
                waiting_time[i] = start_time - arrival_time[i]
                arrival_time[i] = end_time

                # print process details
                print(f"P[{pid}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time[i]}")
                result.append(f"P[{pid}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time[i]}")

                # update start time for the next process
                start_time = end_time

                # add the current process back to the queue if it is not completed
                queue.append(pid)

    # calculate and print the average waiting time
    avg_waiting_time = sum(waiting_time) / n
    print(f"Average waiting time: {avg_waiting_time}")
    result.append(f"Average waiting time: {avg_waiting_time}")
    return result

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

    # print("Algorithm Config (XYZ): ", x, y, z) # For testing purposes
    # print("The processes are: ", processes) # For testing purposes
    
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



