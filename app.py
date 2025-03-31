import tkinter as tk
import random
import time

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        if self.tooltip is None:
            self.tooltip = tk.Toplevel(self.widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            label = tk.Label(self.tooltip, text=self.text, background="#dce0e8", foreground="#4c4f69", relief="raised", borderwidth=2)
            label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.iconbitmap('icon.ico')

        self.canvas = tk.Canvas(root, width=1000, height=500, bg="#eff1f5")
        self.canvas.pack()

        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        self.amount = tk.IntVar(value=20)
        scale = tk.Scale(self.control_frame, from_=2, to=100, orient="horizontal", label="Number of Elements", variable=self.amount)
        scale.pack()
        scale_label = tk.Label(self.control_frame, text="Number of Elements")
        scale_label.place(relx=0.5, rely=0, anchor="n")

        bubble_button = tk.Button(self.control_frame, text="Bubble Sort", command=lambda: self.start_sorting(self.bubble), bg="#eff1f5", fg="#4c4f69", relief="groove")
        bubble_button.pack(side="left")
        Tooltip(bubble_button, "Sorts by repeatedly swapping adjacent elements if they are in the wrong order.")

        insertion_button = tk.Button(self.control_frame, text="Insertion Sort", command=lambda: self.start_sorting(self.insert), bg="#eff1f5", fg="#4c4f69", relief="groove")
        insertion_button.pack(side="left")
        Tooltip(insertion_button, "Sorts by building a sorted array one element at a time.")

        selection_button = tk.Button(self.control_frame, text="Selection Sort", command=lambda: self.start_sorting(self.select), bg="#eff1f5", fg="#4c4f69", relief="groove")
        selection_button.pack(side="left")
        Tooltip(selection_button, "Sorts by repeatedly finding the minimum element and moving it to the sorted portion.")

        quick_button = tk.Button(self.control_frame, text="Quick Sort", command=lambda: self.start_sorting(lambda: self.quick(0, len(self.lst) - 1)), bg="#eff1f5", fg="#4c4f69", relief="groove")
        quick_button.pack(side="left")
        Tooltip(quick_button, "Sorts by partitioning the array around a pivot element.")

        heap_button = tk.Button(self.control_frame, text="Heap Sort", command=lambda: self.start_sorting(self.heap), bg="#eff1f5", fg="#4c4f69", relief="groove")
        heap_button.pack(side="left")
        Tooltip(heap_button, "Sorts by building a heap and repeatedly extracting the maximum element.")

        bogo_button = tk.Button(self.control_frame, text="Bogo Sort", command=lambda: self.start_sorting(self.bogo_sort), bg="#eff1f5", fg="#4c4f69", relief="groove")
        bogo_button.pack(side="left")
        Tooltip(bogo_button, "Sorts by randomly shuffling the array until it is sorted.")

        self.lst = []
        self.generate()

    def generate(self):
        self.lst = [random.randint(10, 300) for _ in range(self.amount.get())]
        self.draw()

    def draw(self, color_map=None):
        self.canvas.delete("all")
        width = 800 / len(self.lst)
        offset = (1000 - 800) / 2  # Centering the rectangles horizontally
        for i, value in enumerate(self.lst):
            x0 = i * width + offset
            y0 = 400 - value
            x1 = (i + 1) * width + offset
            y1 = 400
            color = color_map[i] if color_map else "#1e66f5"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#8c8fa1", width="0.03")
        self.root.update()

    def start_sorting(self, sorting_function):
        self.generate()
        sorting_function()
        self.draw(["#40a02b"] * len(self.lst))  # Final sorted list in green

    def bubble(self):
        n = len(self.lst)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    self.draw(["#d20f39" if x == j or x == j + 1 else "#1e66f5" for x in range(n)])
                    time.sleep(0.05)

    def insert(self):
        n = len(self.lst)
        for i in range(1, n):
            key = self.lst[i]
            j = i - 1
            while j >= 0 and self.lst[j] > key:
                self.lst[j + 1] = self.lst[j]
                j -= 1
                self.draw(["#d20f39" if x == j or x == i else "#1e66f5" for x in range(n)])
                time.sleep(0.05)
            self.lst[j + 1] = key

    def select(self):
        n = len(self.lst)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.lst[j] < self.lst[min_idx]:
                    min_idx = j
                    self.draw(["#d20f39" if x == min_idx or x == j else "#1e66f5" for x in range(n)])
                    time.sleep(0.05)
            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]

    def quick(self, start, end):
        if start >= end:
            return

        pivot = self.lst[start]
        low = start + 1
        high = end

        while True:
            while low <= high and self.lst[high] >= pivot:
                high -= 1
            while low <= high and self.lst[low] <= pivot:
                low += 1
            if low <= high:
                self.lst[low], self.lst[high] = self.lst[high], self.lst[low]
                self.draw(["#d20f39" if x == low or x == high else "#1e66f5" for x in range(len(self.lst))])
                time.sleep(0.05)
            else:
                break

        self.lst[start], self.lst[high] = self.lst[high], self.lst[start]
        self.draw(["#d20f39" if x == start or x == high else "#1e66f5" for x in range(len(self.lst))])
        time.sleep(0.05)

        self.quick(start, high - 1)
        self.quick(high + 1, end)

    def heap(self):
        n = len(self.lst)

        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self.lst[l] > self.lst[largest]:
                largest = l
            if r < n and self.lst[r] > self.lst[largest]:
                largest = r

            if largest != i:
                self.lst[i], self.lst[largest] = self.lst[largest], self.lst[i]
                self.draw(["#d20f39" if x == i or x == largest else "#1e66f5" for x in range(len(self.lst))])
                time.sleep(0.05)
                heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.lst[i], self.lst[0] = self.lst[0], self.lst[i]
            self.draw(["#40a02b" if x > i else "#1e66f5" for x in range(len(self.lst))])
            time.sleep(0.05)
            heapify(i, 0)

    def bogo_sort(self):
        def is_sorted():
            return all(self.lst[i] <= self.lst[i + 1] for i in range(len(self.lst) - 1))

        while not is_sorted():
            random.shuffle(self.lst)
            self.draw()
            time.sleep(0.1)

# Run the Tkinter GUI
root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()