import random

MAX_POINT = 150


class GraphCreator:
    def __init__(self):
        self._CPU = []
        self._RAM = []
        self._Connect = []
        self._TrafficSum = []

    @property
    def CPU(self):
        return self._CPU[-MAX_POINT:]

    @property
    def RAM(self):
        return self._RAM[-MAX_POINT:]

    @property
    def Connect(self):
        return self._Connect[-MAX_POINT:]

    @property
    def TrafficSum(self):
        return self._TrafficSum[-MAX_POINT:]

    def add_tick(self, cpu_value, ram_value, connect_value, traffic_sum_value):
        self._CPU.append(cpu_value)
        self._RAM.append(ram_value)
        self._Connect.append(connect_value)
        self._TrafficSum.append(traffic_sum_value)

    def update_graph(self):
        random_cpu_value = random.uniform(15, 50)
        random_ram_value = random.uniform(40, 50)
        random_connect_value = random.randint(1, 100)
        random_traffic_sum_value = random.randint(1000, 2000)
        self.add_tick(random_cpu_value, random_ram_value, random_connect_value, random_traffic_sum_value)

    def generate_attack(self):
        random_cpu_value = random.uniform(95, 100)
        random_ram_value = random.uniform(97, 100)
        random_connect_value = random.randint(95, 100)
        random_traffic_sum_value = random.randint(8000, 10000)
        self.add_tick(random_cpu_value, random_ram_value, random_connect_value, random_traffic_sum_value)

    def write_to_file(self, output_file=""):
        with open('./logs/meta_CPU.txt', 'w') as output_file:
            output_file.writelines("%s\n" % i for i in self._CPU)
        with open('./logs/meta_RAM.txt', 'w') as output_file:
            output_file.writelines("%s\n" % i for i in self._RAM)
        with open('./logs/meta_Connect.txt', 'w') as output_file:
            output_file.writelines("%s\n" % i for i in self._Connect)
        with open('./logs/meta_TrafficSum.txt', 'w') as output_file:
            output_file.writelines("%s\n" % i for i in self._TrafficSum)
