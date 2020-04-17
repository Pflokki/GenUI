import time
import random
import json

MAX_POINT = 150


class GraphCreator:
    def __init__(self):
        self._CPU = []
        self._RAM = []
        self._Connect = []
        self._TrafficSum = []

        self._AttackLabel = []

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

        try:
            random_cpu_value = min(self._CPU[-1] * 1.15, random_cpu_value)
            random_ram_value = min(self._RAM[-1] * 1.15, random_ram_value)
            random_connect_value = min(self._Connect[-1] * 1.15, random_connect_value)
            random_traffic_sum_value = min(self._TrafficSum[-1] * 1.15, random_traffic_sum_value)
        except IndexError:
            pass

        self.add_tick(random_cpu_value, random_ram_value, random_connect_value, random_traffic_sum_value)

    def generate_die_data(self):
        self.add_tick(0, 0, 0, 0)

    def create_train_data(self, data_size=10000, attack_ver=0.2):
        while len(self._AttackLabel) < data_size:
            if random.randint(0, 10) / 10 <= attack_ver:
                attack_length = random.randint(0, 50)
                while attack_length > 0:
                    attack_length -= 1
                    self.generate_attack()
                    self._AttackLabel.append(1)
            else:
                normal_work_length = random.randint(0, 100)
                while normal_work_length > 0:
                    normal_work_length -= 1
                    self.update_graph()
                    self._AttackLabel.append(0)

        train_data, train_predicate = [], []
        for index in range(len(self._AttackLabel)):
            train_data.append(
                (self._CPU[index], self._RAM[index],
                 self._TrafficSum[index], self._Connect[index])
            )
            train_predicate.append(self._AttackLabel[index])

        return train_data[:data_size], train_predicate[:data_size]

    def write_to_file(self, train_data, train_predicate):
        time_postfix = time.strftime('%Y-%M-%d-%H:%M:%S', time.gmtime())
        with open('./logs/[{}]train_data.txt'.format(time_postfix), 'w') as file:
            for items in zip(train_data, train_predicate):
                file.write(json.dumps(items) + '\n')


if __name__ == '__main__':
    gc = GraphCreator()
    train_data, train_predicate = gc.create_train_data(10000, 0.2)
    gc.write_to_file(train_data, train_predicate)
