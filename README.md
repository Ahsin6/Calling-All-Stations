# Calling-All-Stations
Project Overview

This project simulates the communication process in a distributed system consisting of internet-connected devices. Each device raises alerts, propagates them to other devices, and cancels them once the issue is resolved. The simulation models how these devices exchange information following predefined propagation rules and delays, and how messages flow through the system in real time.

Project Structure

The project is divided into multiple modules to handle different parts of the simulation:

project1.py: 
The main module that initializes and runs the simulation.
Handles the propagation rules and message delays between devices.
Controls the simulation’s timeline, schedules events, and manages the overall simulation process.

device.py: Manages the behavior of individual devices, including raising alerts and processing cancellations.
test_project1.py: Contains unit tests to verify the correctness of the simulation and its components.
Input File Specifications

The program reads input files with the following structure:

LENGTH n: Specifies the simulation length in milliseconds.
DEVICE id: Declares a device by its ID.
PROPAGATE id1 id2 delay: Defines the propagation rule from device id1 to id2 with a delay.
ALERT id description time: Raises an alert at the specified time from a particular device.
CANCEL id description time: Cancels an alert at the specified time.
Example Input:
# These are the four devices from that example
DEVICE 1
DEVICE 2
DEVICE 3
DEVICE 4


# These are the propagation rules described in that example
PROPAGATE 1 2 750
PROPAGATE 2 3 1250
PROPAGATE 3 4 500
PROPAGATE 4 1 1000

Output Format

As the simulation runs, the program generates output detailing the propagation of alerts and cancellations between devices:

@time: #device RECEIVED ALERT FROM #device: description
@time: #device SENT ALERT TO #device: description
@time: #device RECEIVED CANCELLATION FROM #device: description
@time: #device SENT CANCELLATION TO #device: description

Output Example:
@0 #1: SENT ALERT TO #2: Trouble
@750 #2: RECEIVED ALERT FROM #1: Trouble
@750 #2: SENT ALERT TO #3: Trouble
@2000 #3: RECEIVED ALERT FROM #2: Trouble
@2000 #3: SENT ALERT TO #4: Trouble
@2200 #1: SENT CANCELLATION TO #2: Trouble
@2500 #4: RECEIVED ALERT FROM #3: Trouble
@2500 #4: SENT ALERT TO #1: Trouble
@2950 #2: RECEIVED CANCELLATION FROM #1: Trouble
@2950 #2: SENT CANCELLATION TO #3: Trouble
@3500 #1: RECEIVED ALERT FROM #4: Trouble
@4200 #3: RECEIVED CANCELLATION FROM #2: Trouble
@4200 #3: SENT CANCELLATION TO #4: Trouble
@4700 #4: RECEIVED CANCELLATION FROM #3: Trouble
@4700 #4: SENT CANCELLATION TO #1: Trouble
@5700 #1: RECEIVED CANCELLATION FROM #4: Trouble


