def getInput():
    """Function to take user input for number of processes, resources, max matrix, allocation matrix, and available resources."""
    processes = int(input("Enter number of Processes: "))
    resources = int(input("Enter number of Resources: "))

    print("Enter Max matrix (each row for a process):")
    maxMatrix = [list(map(int, input().split())) for i in range(processes)]

    print("Enter Allocation matrix (each row for a process):")
    allocMatrix = [list(map(int, input().split())) for i in range(processes)]

    available = list(map(int, input("Enter Available resources: ").split()))

    return processes, resources, maxMatrix, allocMatrix, available


def calculateNeedMatrix(processes, resources, maxMatrix, allocMatrix):
    """Function to calculate the Need Matrix as Need[i][j] = Max[i][j] - Allocation[i][j]"""
    needMatrix = [[maxMatrix[i][j] - allocMatrix[i][j] for j in range(resources)] for i in range(processes)]
    return needMatrix


def bankersAlgorithm(processes, resources, maxMatrix, allocMatrix, available):
    """Function implementing Banker's Algorithm for deadlock avoidance."""

    # Calculate Need Matrix
    needMatrix = calculateNeedMatrix(processes, resources, maxMatrix, allocMatrix)

    # Track finished processes
    finish = [False] * processes

    # Copy available resources
    avail = available[:]

    # Safe sequence
    safeSeq = []

    executedCount = 0  # Count of completed processes
    index = 0  # Start index for checking processes

    while executedCount < processes:
        found = False

        for i in range(index, processes):  # Start checking from current index
            if not finish[i] and all(needMatrix[i][j] <= avail[j] for j in range(resources)):
                # Process can execute
                for j in range(resources):
                    avail[j] += allocMatrix[i][j]  # Update available resources

                safeSeq.append(i)
                finish[i] = True
                executedCount += 1
                found = True

        if not found:  # No process executed in the last iteration
            print("System is in an unsafe state!")
            return None  # No safe sequence possible

    return safeSeq  # Return the safe sequence


# Main Execution
if __name__ == "__main__":
    processes, resources, maxMatrix, allocMatrix, available = getInput()
    
    # Display Need Matrix
    needMatrix = calculateNeedMatrix(processes, resources, maxMatrix, allocMatrix)
    print("\nNeed Matrix:")
    for row in needMatrix:
        print(row)

    result = bankersAlgorithm(processes, resources, maxMatrix, allocMatrix, available)
    
    if result is None:
        print("System is unsafe!")
    else:
        print("\nSafe sequence:", " -> ".join(map(str, result)))
