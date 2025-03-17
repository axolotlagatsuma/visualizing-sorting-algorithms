import matplotlib.pyplot as plt
import numpy as np

# Get user input
amount = int(input("Choose an amount: "))
algorithm = int(input("Choose an algorithm 1 = Bubble Sort, 2 = Selection Sort, 3 = Insertion Sort, 4 = Quick Sort, 5 = Merge Sort: "))

# Generate random list and x-axis positions
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

def bubble_sort():
    n = len(lst)
    plt.ion()  # Interactive mode for animation

    for i in range(n):
        for j in range(0, n-i-1):
            colors = ['blue'] * amount
            colors[j] = colors[j+1] = 'red'  # Highlight compared elements

            plt.bar(x, lst, color=colors)
            plt.pause(0.0001)
            plt.clf()

            if lst[j] > lst[j+1]:  # Swap if needed
                lst[j], lst[j+1] = lst[j+1], lst[j]

        # Mark the last sorted element in green
        colors[n-i-1] = 'green'

    # Final sorted visualization
    plt.bar(x, lst, color='green')
    plt.show()

# Call the selected sorting algorithm
if algorithm == 1:
    bubble_sort()
