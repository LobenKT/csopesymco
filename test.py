import unittest
from main import sjf, get_user_input

class TestSJF(unittest.TestCase):
    # Simulate the results of https://www.youtube.com/watch?v=pYO-FAg-TpQ and Test File Input
    def test_valid_input(self):
        x, y, z, processes = get_user_input('inputs/sjf.txt')
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

    # SJF Additional Test Case
    def test_additional_input(self):
        x, y, z, processes = get_user_input('inputs/26-Input-SJF.txt')
        expected_output = [
            "P[0] Start time: 0 End time: 9 | Waiting time: 0",
            "P[1] Start time: 9 End time: 11 | Waiting time: 8",
            "P[4] Start time: 11 End time: 13 | Waiting time: 3",
            "P[2] Start time: 13 End time: 16 | Waiting time: 9",
            "P[6] Start time: 16 End time: 19 | Waiting time: 5",
            "P[10] Start time: 19 End time: 21 | Waiting time: 0",
            "P[14] Start time: 21 End time: 23 | Waiting time: 0",
            "P[5] Start time: 23 End time: 27 | Waiting time: 13",
            "P[9] Start time: 27 End time: 31 | Waiting time: 9",
            "P[16] Start time: 31 End time: 32 | Waiting time: 0",
            "P[3] Start time: 32 End time: 37 | Waiting time: 27",
            "P[11] Start time: 37 End time: 42 | Waiting time: 17",
            "P[20] Start time: 42 End time: 44 | Waiting time: 0",
            "P[21] Start time: 44 End time: 45 | Waiting time: 0",
            "P[17] Start time: 45 End time: 49 | Waiting time: 6",
            "P[23] Start time: 49 End time: 52 | Waiting time: 2",
            "P[25] Start time: 52 End time: 53 | Waiting time: 1",
            "P[24] Start time: 53 End time: 55 | Waiting time: 3",
            "P[22] Start time: 55 End time: 59 | Waiting time: 9",
            "P[15] Start time: 59 End time: 64 | Waiting time: 34",
            "P[19] Start time: 64 End time: 70 | Waiting time: 24",
            "P[18] Start time: 70 End time: 78 | Waiting time: 30",
            "P[12] Start time: 78 End time: 87 | Waiting time: 58",
            "P[7] Start time: 87 End time: 98 | Waiting time: 71",
            "P[8] Start time: 98 End time: 110 | Waiting time: 81",
            "P[13] Start time: 110 End time: 125 | Waiting time: 90",
            "Average waiting time: 19.23"
        ]
        output = sjf(processes) 
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()