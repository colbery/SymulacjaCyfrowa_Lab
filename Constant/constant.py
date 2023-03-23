import random
import math

class Constant:
    def __init__(self):
        self.l = 5000 # stała równa 5000 m
        self.x = 2000 # stała równa 2000 m
        self.v = random.uniform(5, 50) # zmienna losowa o rozkładzie jednostajnym na przedziale [5, 50] m/s
        self.t = 20e-3 # stała równa 20 ms
        self.s = random.gauss(0, 4) # zmienna losowa o rozkładzie Gaussa ze średnia równą 0 i odchyleniem standardowym równym 4 dB
        self.delta = 8 # stała równa 8 dB
        self.tau = random.expovariate(1/float(self.t)) # zmienna losowa o rozkładzie wykładniczym o intensywności λ = 1/τ
