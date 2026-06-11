# Sorting Algorithm Visualizer

A real-time sorting visualizer I built with Pygame in Python. This was primarily
a learning project to learn about sorting algorithms and Python generators.

## What I Built
A visualizer that animates five sorting algorithms on a randomized array of
integers with the possibility to add duplicates or reverse the array, rendering each comparison and swap in real time using Pygame.

## What I Learned

### Sorting Algorithms
I implemented and analyzed five algorithms from scratch:
- **Bubble Sort** – O(n²), simple but slow algorithm. Can exit early if no swaps happened.
- **Insertion Sort** – O(n²), efficient for small or nearly sorted arrays but still slow.
- **Merge Sort** – O(n log n), reducing the large array to lots of small ones and then merging those together.
- **Quick Sort** – O(n log n) average, picks a pivot and regroups all smaller elements to its left and larger elements to its right, then recurses on both sides.
- **Heap Sort** – O(n log n), two phases: build a max-heap, then extract elements one by one.

### Python Generators
The biggest technical challenge was converting each algorithm into a generator
so the visualizer could step through the sorting process frame by frame.
Especially converting the algorithms, that use recursion, to generators was difficult because I initially did not use in-place sorting.
Key concepts I learned about:
- `yield` pauses execution and passes state to the caller
- `yield from` delegates to a sub-generator, forwarding all its yields up the chain
- How each of these 5 sorting algorithms work and why some of them perform better than others.

### Pygame Rendering
- Pygame doesn't clear the screen between frames, so `screen.fill()` has to be called manually each frame
- Bar widths computed as `max(1, int((index + 1) * width / length) - (index * bar_width))`, which allows for arrays that are bigger than the screen width.
- Frame skipping (`index % 1 == 0`) to control animation speed without changing the algorithm

## Usage
pip install pygame
python main.py

To change the algorithm, open `main.py` and replace the algorithm in the main loop:
heap.heapsort(arr)      # default

Available options:
bubble.bubble_sort(arr)
insert.insertion_sort(arr)
merge.merge_sort(arr)
quick.quick_sort(arr)
heap.heap_sort(arr)
