import random

class Array:

    def create_array(self, length: int, duplicates: bool, reverse: bool)-> list[int]:
        arr = list((range(1, length + 1)))
        
        if duplicates:
            arr += random.choices(range(1, length + 1), k = length // 2)
        if reverse:
            arr.sort()
            arr.reverse()
            return arr

        random.shuffle(arr)
        
        return arr
    