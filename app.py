import tkinter as tk
import random
import time
import os
import sys

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

        # Handle PyInstaller's temp directory (_MEIPASS)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        icon_path = os.path.join(base_path, "icon.ico")

        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        else:
            print(f"Warning: Icon file not found at {icon_path}")

        self.canvas = tk.Canvas(root, width=1000, height=500, bg="#eff1f5")
        self.canvas.pack()

        self.elapsed_time = 0
        self.time_label = tk.Label(root, text=f"Time: {self.elapsed_time:.2f} ms", bg="#eff1f5", fg="#4c4f69")
        self.time_label.pack()

        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        self.amount = tk.IntVar(value=20)
        scale = tk.Scale(self.control_frame, from_=2, to=100, orient="horizontal", showvalue=True, label="Dataset Width", variable=self.amount)
        scale.pack()

        self.buttons = []
        buttons = [
            ("Bubble Sort", self.bubble, "Sorts by repeatedly swapping adjacent elements if they are in the wrong order."),
            ("Insertion Sort", self.insert, "Sorts by building a sorted array one element at a time."),
            ("Selection Sort", self.select, "Sorts by repeatedly finding the minimum element and moving it to the sorted portion."),
            ("Quick Sort", lambda: self.start_sorting(lambda: self.quick(0, len(self.lst) - 1)), "Sorts by partitioning the array around a pivot element."),
            ("Heap Sort", self.heap, "Sorts by building a heap and repeatedly extracting the maximum element."),
            ("Bogo Sort", self.bogo_sort, "Sorts by randomly shuffling the array until it is sorted."),
        ]

        for text, command, tooltip in buttons:
            button = tk.Button(self.control_frame, text=text, command=lambda cmd=command: self.start_sorting(cmd), bg="#eff1f5", fg="#4c4f69", relief="groove")
            button.pack(side="left")
            Tooltip(button, tooltip)
            self.buttons.append(button)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_sorting, bg="#eff1f5", fg="#4c4f69", relief="groove")
        #self.stop_button.place(relx=0.5, rely=1, anchor="center")
        self.stop_button.pack(side="bottom")

        self.lst = []
        self.running = False
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
        self.running = True
        self.toggle_buttons(state="disabled")

        start_time = time.time()
        sorting_function()
        end_time = time.time()

        self.elapsed_time = (end_time - start_time) * 1000  # ms
        self.time_label.config(text=f"Time: {self.elapsed_time:.2f} ms")
        print(f"Sorting took {self.elapsed_time:.2f} ms")

        if self.running:
            self.draw(["#40a02b"] * len(self.lst))  # Final sorted list in green
        self.toggle_buttons(state="normal")

    def stop_sorting(self):
        self.running = False

    def toggle_buttons(self, state):
        for button in self.buttons:
            button.config(state=state)

    def bubble(self):
        n = len(self.lst)
        for i in range(n):
            if not self.running:
                break
            for j in range(0, n - i - 1):
                if not self.running:
                    break
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    self.draw(["#d20f39" if x == j or x == j + 1 else "#1e66f5" for x in range(n)])
                    time.sleep(0.05)

    def insert(self):
        n = len(self.lst)
        for i in range(1, n):
            if not self.running:
                break
            key = self.lst[i]
            j = i - 1
            while j >= 0 and self.lst[j] > key:
                if not self.running:
                    break
                self.lst[j + 1] = self.lst[j]
                j -= 1
                self.draw(["#d20f39" if x == j or x == i else "#1e66f5" for x in range(n)])
                time.sleep(0.05)
            self.lst[j + 1] = key

    def select(self):
        n = len(self.lst)
        for i in range(n):
            if not self.running:
                break
            min_idx = i
            for j in range(i + 1, n):
                if not self.running:
                    break
                if self.lst[j] < self.lst[min_idx]:
                    min_idx = j
                    self.draw(["#d20f39" if x == min_idx or x == j else "#1e66f5" for x in range(n)])
                    time.sleep(0.05)
            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]

    def quick(self, start, end):
        if start >= end or not self.running:
            return
        pivot = self.lst[start]
        low = start + 1
        high = end
        while True:
            if not self.running:
                return
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
        self.draw()
        time.sleep(0.05)
        self.quick(start, high - 1)
        self.quick(high + 1, end)

    def heap(self):
        n = len(self.lst)

        def heapify(n, i):
            if not self.running:
                return
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
            if not self.running:
                break
            self.lst[i], self.lst[0] = self.lst[0], self.lst[i]
            self.draw(["#d20f39" if x == i or x == 0 else "#1e66f5" for x in range(len(self.lst))])
            time.sleep(0.05)
            heapify(i, 0)

    def bogo_sort(self):
        def is_sorted():
            return all(self.lst[i] <= self.lst[i + 1] for i in range(len(self.lst) - 1))
        while not is_sorted():
            if not self.running:
                break
            random.shuffle(self.lst)
            self.draw()
            time.sleep(0.1)

# Run the Tkinter GUI
root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()