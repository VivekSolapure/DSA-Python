def min_elevators(boxWeights):
    # Sort the weights in descending order to prioritize heavier boxes
    boxWeights.sort(reverse=True)
    
    left = 0
    right = len(boxWeights) - 1
    elevators = 0

    while left <= right:
        # Always take the heaviest box first
        if left == right:  # If only one box is left
            elevators += 1
            break

        if boxWeights[left] + boxWeights[right] <= 150:
            # If the heaviest and lightest box can share an elevator
            right -= 1

        # Always move the pointer for the heaviest box
        left += 1
        
        # Increment the elevator count
        elevators += 1

    return elevators

# Example usage
if __name__ == "__main__":
    # Take input from the user
    boxWeights = list(map(int, input("Enter the weights of the boxes separated by spaces (e.g., '50 100 50'): ").split()))
    print("Minimum number of elevators needed:", min_elevators(boxWeights))
