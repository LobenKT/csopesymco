import unittest
from main import sjf, get_user_input

class TestSJF(unittest.TestCase):
    # Simulate the results of https://www.youtube.com/watch?v=pYO-FAg-TpQ and Test File Input
    def test_valid_input(self):
        x, y, z, processes = get_user_input('sjf.txt')
        expected_output = [
            "P[4] Start time: 0 End time: 6 | Waiting time: 0",
            "P[1] Start time: 6 End time: 7 | Waiting time: 4",
            "P[3] Start time: 7 End time: 8 | Waiting time: 3",
            "P[5] Start time: 8 End time: 11 | Waiting time: 6",
            "P[2] Start time: 11 End time: 16 | Waiting time: 10",
            "Average waiting time: 4.60"
        ]
        output = sjf(processes) 
        self.assertEqual(output, expected_output)

    # When Remaining Time of two or more processes are the same, assume the lower numbered process has priority    
    # From CPU Scheduling Practice
    def test_pid_prio(self):
        processes = [(1, 0, 5), (2, 0, 4), (3, 0, 6), (4, 0, 5)]
        expected_output = [
            "P[2] Start time: 0 End time: 4 | Waiting time: 0",
            "P[1] Start time: 4 End time: 9 | Waiting time: 4",
            "P[4] Start time: 9 End time: 14 | Waiting time: 9",
            "P[3] Start time: 14 End time: 20 | Waiting time: 14",
            "Average waiting time: 6.75"
        ]
        output = sjf(processes) 
        self.assertEqual(output, expected_output)

    # When Remaining Time of two or more processes are the same, use Arrival Time as priority
    # From CPU Scheduling Practice
    def test_at_prio(self):
        processes = [(1, 0, 5), (2, 1, 4), (3, 3, 6), (4, 6, 5)]
        expected_output = [
            "P[1] Start time: 0 End time: 5 | Waiting time: 0",
            "P[2] Start time: 5 End time: 9 | Waiting time: 4",
            "P[4] Start time: 9 End time: 14 | Waiting time: 3",
            "P[3] Start time: 14 End time: 20 | Waiting time: 11",
            "Average waiting time: 4.50"
        ]
        output = sjf(processes) 
        self.assertEqual(output, expected_output)

    # Test when all processes have the same burst time
    def test_equal_burst_time(self):
        processes = [(1, 0, 5), (2, 1, 5), (3, 2, 5), (4, 3, 5)]
        expected_output = [
            "P[1] Start time: 0 End time: 5 | Waiting time: 0",
            "P[2] Start time: 5 End time: 10 | Waiting time: 4",
            "P[3] Start time: 10 End time: 15 | Waiting time: 8",
            "P[4] Start time: 15 End time: 20 | Waiting time: 12",
            "Average waiting time: 6.00"
        ]
        output = sjf(processes)
        self.assertEqual(output, expected_output)

    # Test when all processes have the same arrival time
    def test_equal_arrival_time(self):
        processes = [(1, 0, 3), (2, 0, 4), (3, 0, 2), (5, 0, 5)]
        expected_output = [
            "P[3] Start time: 0 End time: 2 | Waiting time: 0",
            "P[1] Start time: 2 End time: 5 | Waiting time: 2",
            "P[2] Start time: 5 End time: 9 | Waiting time: 5",
            "P[5] Start time: 9 End time: 14 | Waiting time: 9",
            "Average waiting time: 4.00"
        ]
        output = sjf(processes)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()