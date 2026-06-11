import pygame

class Visualize:
    def visualize(self, array: list[int], length: int, screen: pygame.Surface, active_idx: int = None, color: tuple = (50, 50, 50)):
        width, height = screen.get_size()
        bar_width = width / length
        max_val = max(array)

        screen.fill((50, 74, 168))

        for index, value in enumerate(array):
            scaled_height = max(1, round((value / max_val) * height))
            if index == active_idx:
                pygame.draw.rect(screen, (255, 255, 255),
                                ( 
                                index * bar_width,                                                 # x
                                0,                                                                 # y
                                max(1, int((index + 1) * width / length) - (index * bar_width)),   # width
                                height                                                             # height
                                )
                )
            else:
                pygame.draw.rect(screen, color,
                                ( 
                                index * bar_width,                                                 # x
                                height - scaled_height,                                            # y
                                max(1, int((index + 1) * width / length) - (index * bar_width)),   # width
                                scaled_height                                                      # height
                                )
                )