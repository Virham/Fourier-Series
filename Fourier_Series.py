import pygame
pygame.init()
import time
import math
from vector import Vector

class Main:
    def __init__(self):
        self.size = 720
        self.win = pygame.display.set_mode((self.size, self.size))

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.last_time = time.time()

        self.pos = round(Vector(150, self.size / 2))
        self.angle = 0
        self.radius = 100

        self.samples = [False] * 300
        self.sample_pos = None
        self.sample_interval = 1
        self.current_interval = 0

        self.sample_startpos = 400
        self.sample_moving_speed = 1

    def draw(self):
        self.win.fill((255, 255, 255))
        prev_pos = self.pos

        for n in range(25):
            n = n * 2 + 1
            radius = (self.size / 4) // n

            x = radius * math.cos(n * self.angle)
            y = radius * math.sin(n * self.angle)

            pos = Vector(x, y)
            pos.magnitude = radius



            pygame.draw.circle(self.win, (0, 0, 0), round(prev_pos), round(radius + 1), 1)
            pygame.draw.line(self.win, (255, 0, 0), round(prev_pos), round(prev_pos + pos))

            prev_pos = round(prev_pos + pos)

        self.sample_pos = prev_pos

        if self.samples[0]:
            pygame.draw.line(self.win, (0, 255, 0), self.sample_pos, Vector(self.sample_startpos, self.samples[0].y), 5)


        for i in range(len(self.samples) - 1):
            if self.samples[i] and self.samples[i + 1]:
                pygame.draw.line(self.win, (0, 0, 255), Vector(self.sample_startpos + (i * self.sample_moving_speed),  self.samples[i].y), Vector(self.sample_startpos + ((i + 1) * self.sample_moving_speed),  self.samples[i + 1].y), 5)

        pygame.display.update()

    def GetDeltatime(self):
        dt = time.time() - self.last_time
        dt *= 60
        self.last_time = time.time()
        return dt

    def loop(self):
        while True:
            self.draw()
            self.current_interval += 1
            self.current_interval %= self.sample_interval
            if self.current_interval == 0:
                self.samples.insert(0, self.sample_pos)
                self.samples.pop(-1)

            dt = self.GetDeltatime()
            self.angle += 0.02 * dt
            self.angle %= math.tau


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.clock.tick(self.fps)

Main().loop()