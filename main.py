import pygame
import random
from generate_array import Array
from visualize import Visualize
from algorithms import BubbleSort, InsertionSort, QuickSort, MergeSort, HeapSort

class App:
    def run(self, length: int, duplicates: bool, reverse: bool):
        pygame.init()
        screen = pygame.display.set_mode((1000,500))
        pygame.display.set_caption("Sorting Algorithm")
        running = True
        # create instaces of all classes I import
        a = Array() # create a random array
        arr = a.create_array(length, duplicates, reverse)
        vis = Visualize()
        bubble = BubbleSort()
        insert = InsertionSort()
        quick = QuickSort()
        merge = MergeSort()
        heap = HeapSort()
        once = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if not once:
                for index, step in enumerate(heap.heap_sort(arr)):
                    if index % 1 == 0: # only show every n steps, so visualizing the sort on a larger array doesnt take to long
                        vis.visualize(step[0], length, screen, step[1])
                        pygame.display.flip()
                        pygame.time.delay(10)
                vis.visualize(arr, length, screen)
                once = True

            vis.visualize(arr, length, screen, color = (0, 255, 0))
            
            pygame.display.flip()
        pygame.quit()

app = App()
app.run(100, False, False)