def get_user_input():
    """
    This function gets and validates the user input according to the specifications.
    """
    while True:
        try:
            # Input format: X Y Z (algorithm, number of processes, time quantum)
            x, y, z = map(int, input("Enter X Y Z: ").split())
            
            # Validate inputs
            if x not in [0, 1, 2, 3] or not (3 <= y <= 100) or not (1 <= z <= 100):
                raise ValueError("Invalid input. Please adhere to the constraints.")
            
            # Get process details
            processes = []
            print(f"Enter {y} lines of A B C (process ID, arrival time, burst time):")
            for _ in range(y):
                a, b, c = map(int, input().split())
                processes.append((a, b, c))
            
            return x, y, z, processes
        except ValueError as e:
            print(e)
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
    """Round-Robin Scheduling."""
    # Placeholder for RR implementation
    pass

def main():
    x, y, z, processes = get_user_input()  # For actual use
    # x, y, z, processes = simulate_user_input(inputs)  # For testing purposes
    
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
