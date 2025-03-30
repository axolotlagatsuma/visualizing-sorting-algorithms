import matplotlib.pyplot as plt
import numpy as np
import sys
import time

def loading_animation():
    animation = "|/-\\"
    for i in range(40):  # Adjust the number of iterations for how long the animation runs
        sys.stdout.write(f'\rLoading {animation[i % len(animation)]}')
        sys.stdout.flush()
        time.sleep(0.3)

def matrix():
    monologue = np.random.randint(8)
    if monologue == 0:
        print("Oops! It seems like that wasn't a valid algorithm."
              " No worries, though! Just take a moment and try entering a valid algorithm."
              " I'm here to help you get it right!")
    elif monologue == 1:
        print("Invalid input!"
              " Please enter a valid algorithm option."
              " Let's try again and get it right this time.")
    elif monologue == 2:
        print("Uh-oh, that’s not quite what we’re looking for!"
              " Looks like that wasn’t a valid option."
              " Don’t worry, take another shot at it!")
    elif monologue == 3:
        print("Your choice of algorithm appears to be invalid."
              " Please enter a valid algorithm option to proceed."
              " Thank you for your patience.")
    elif monologue == 4:
        print("Incorrect entry detected."
              " The system expects an valid algorithm."
              " Please make sure you're entering a valid number and try again.")
    elif monologue == 5:
        print("Hmm, that didn’t quite work."
              " It looks like you entered an invalid option."
              " No problem—just try again with a valid algorithm, and we’ll keep things moving!")
    else:
        print("Hmmm... I never heard that algorithm.\n")
        time.sleep(1)
        print(str(algorithm) + " huh??")
        time.sleep(0.3)
        print("Let me check my database again...")
        loading_animation()
        print("\nYeahhh, I don't have that one. Sorry mate!")

# Generate random list and x-axis positions
amount = int(input("Choose an amount: "))
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

def bubble(lst):
    n = len(lst) #length
    plt.ion()  # interactive mode

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            colors = ['blue'] * amount  #fefault color for bars
            colors[j] = colors[j + 1] = 'red'  #highlight compared elements

            plt.bar(x, lst, color=colors)
            plt.pause(0.05)
            plt.clf()

            if lst[j] > lst[j + 1]:  # swap condition
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                colors[j] = colors[j + 1] = 'orange'  # highlight swap

                plt.bar(x, lst, color=colors)
                plt.pause(0.05)
                plt.clf()

        if not swapped:
            break  # stops if there are no swaps

        colors[n - i - 1] = 'green'  # marks sorted element

    # show final sorted visualization
    plt.bar(x, lst, color='green')
    plt.show()

def insert(lst):
    n = len(lst) #lenght
    plt.ion() #interactive mode

    for i in range(1, n):
        key = lst[i]
        j = i-1
        colors = ['blue'] * amount  # fefault color for bars
        while j >= 0 and key < lst[j] :
            colors[j] = colors[j + 1] = 'red'  # highlight compared elements
            colors[i] = 'orange'  # show selected element before swap
            lst[j + 1] = lst[j]
            j -= 1
            plt.bar(x, lst, color=colors)
            plt.pause(0.01)
        lst[j + 1] = key
        # show final sorted visualization
    plt.bar(x, lst, color='green')
    plt.show()


def select(lst):
    n = len(lst) #length
    plt.ion()  # interactive mode

    for i in range(n):
        colors = ['blue'] * amount  # default color for bars
        min_idx = i
        for j in range(i + 1, n):
            colors[j] = 'red'  # highlight compared elements
            colors[i] = 'orange'  # show selected min before swap
            if lst[min_idx] > lst[j]:
                min_idx = j
            plt.bar(x, lst, color=colors)
            plt.pause(0.01)
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    # show final sorted visualization
    plt.bar(x, lst, color='green')
    plt.show()

def partitioninator(lst, start, end):
    pivot = lst[start]
    low = start + 1
    high = end
    colors = ['blue'] * amount  # default color for bars
    colors[start] = 'yellow'  # highlight pivot

    while True:
        while low <= high and lst[high] >= pivot:
            colors[high] = 'red'  # highlight comparison
            plt.clf()
            plt.bar(x, lst, color=colors)
            plt.pause(0.01)
            colors[high] = 'blue'  # reset color
            high -= 1

        while low <= high and lst[low] <= pivot:
            colors[low] = 'red'  # highlight comparison
            plt.clf()
            plt.bar(x, lst, color=colors)
            plt.pause(0.01)
            colors[low] = 'blue'  # reset color
            low += 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
            colors[low], colors[high] = 'orange', 'orange'  # highlight swap
            plt.clf()
            plt.bar(x, lst, color=colors)
            plt.pause(0.01)
            colors[low], colors[high] = 'blue', 'blue'  # reset color
        else:
            break

    lst[start], lst[high] = lst[high], lst[start]
    return high

def quick(lst, start, end):
    if start >= end:
        return

    p = partitioninator(lst, start, end)

    colors = ['blue'] * amount  # color reset
    colors[p] = 'yellow'  # remains yellow
    plt.clf()
    plt.bar(x, lst, color=colors)
    plt.pause(0.1)

    quick(lst, start, p-1)
    quick(lst, p+1, end)

    if start == 0 and end == amount - 1:  #  marks all green
        plt.clf()
        plt.bar(x, lst, color='green')
        plt.show()


def heapakadavra(lst, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  colors = ['blue'] * len(lst)  # default color
  colors[i] = 'yellow'  # highlight root

  if l < n and lst[i] < lst[l]:
      largest = l

  if r < n and lst[largest] < lst[r]:
      largest = r

  if largest != i:
      lst[i], lst[largest] = lst[largest], lst[i]
      colors[i], colors[largest] = 'red', 'red'  # highlight swap

      plt.clf()
      plt.bar(x, lst, color=colors)
      plt.pause(0.1)
      heapakadavra(lst, n, largest)


def heap(lst):
    n = len(lst)
    plt.ion()  # interactive mode

    # max heap
    for i in range(n // 2 - 1, -1, -1):
        heapakadavra(lst, n, i)

    # extract elements
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # swap max to the end

        colors = ['green'] * (n - i) + ['blue'] * i  # öark sorted elements as green
        plt.clf()
        plt.bar(x, lst, color=colors)
        plt.pause(0.1)

        heapakadavra(lst, i, 0)

    # final
    plt.clf()
    plt.bar(x, lst, color='green')
    plt.show()

while True:
    # get user input
    try:
        algorithm = int(input("Choose an algorithm 1 = Bubble Sort, 2 = Insertion Sort, 3 = Selection Sort, 4 = Quick Sort, 5 = Heap Sort: "))
    except ValueError:
        matrix()
        continue  # this will restart the loop if the user doesn't enter a valid integer

    # Check if the input is valid
    if algorithm == 1:
        bubble(lst)
        break
    elif algorithm == 2:
        insert(lst)
        break
    elif algorithm == 3:
        select(lst)
        break
    elif algorithm == 4:
        quick(lst, 0, amount - 1)
        break
    elif algorithm == 5:
        heap(lst)
        break
    else:
        matrix()  # This will print the invalid input message and then loop again for valid input