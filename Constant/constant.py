import random

class Constant:
    def __init__(self):
        # stała równa 5000 m
        self.l = 5000 
        # stała równa 2000 m
        self.x = 2000 
        # zmienna losowa o rozkładzie jednostajnym na przedziale [5, 50] m/s
        self.v = random.uniform(5, 50) 
        # stała równa 20 ms
        self.t = 20e-3 
        # zmienna losowa o rozkładzie Gaussa ze średnia równą 0 i odchyleniem standardowym równym 4 dB
        self.s = random.gauss(0, 4) 
        # stała równa 8 dB
        self.delta = 8 
        # zmienna losowa o rozkładzie wykładniczym o intensywności λ = 1/τ
        self.tau = random.expovariate(1/float(self.t)) 
