import time
import random
import json

MAX_POINT = 150


class GraphCreator:
    def __init__(self):
        self._cpu = []
        self._ram = []
        self._connection_value = []
        self._traffic_value = []

        self._attack_labels = []

    @property
    def cpu(self):
        return self._cpu[-MAX_POINT:]

    @property
    def ram(self):
        return self._ram[-MAX_POINT:]

    @property
    def connection_value(self):
        return self._connection_value[-MAX_POINT:]

    @property
    def traffic_value(self):
        return self._traffic_value[-MAX_POINT:]

    def add_tick(self, cpu_value, ram_value, connect_value, traffic_sum_value, is_attack):
        self._cpu.append(cpu_value)
        self._ram.append(ram_value)
        self._connection_value.append(connect_value)
        self._traffic_value.append(traffic_sum_value)
        self._attack_labels.append(int(is_attack))

    def update_graph(self):
        random_cpu_value = random.uniform(15, 50)
        random_ram_value = random.uniform(40, 50)
        random_connect_value = random.randint(1, 100)
        random_traffic_sum_value = random.randint(1000, 2000)
        self.add_tick(random_cpu_value, random_ram_value,
                      random_connect_value, random_traffic_sum_value,
                      is_attack=False)

    def generate_attack(self):
        random_cpu_value = random.uniform(95, 100)
        random_ram_value = random.uniform(97, 100)
        random_connect_value = random.randint(95, 100)
        random_traffic_sum_value = random.randint(8000, 10000)

        try:
            random_cpu_value = min(self._cpu[-1] * 1.15, random_cpu_value)
            random_ram_value = min(self._ram[-1] * 1.15, random_ram_value)
            random_connect_value = min(self._connection_value[-1] * 1.15, random_connect_value)
            random_traffic_sum_value = min(self._traffic_value[-1] * 1.15, random_traffic_sum_value)
        except IndexError:
            pass

        self.add_tick(random_cpu_value, random_ram_value,
                      random_connect_value, random_traffic_sum_value,
                      is_attack=True)

    def generate_die_data(self):
        self.add_tick(0, 0, 0, 0, is_attack=False)

    def create_train_data(self, data_size=10000, attack_ver=0.2):
        while len(self._attack_labels) < data_size:
            if random.randint(0, 10) / 10 <= attack_ver:
                attack_length = random.randint(0, 50)
                while attack_length > 0:
                    attack_length -= 1
                    self.generate_attack()
                    self._attack_labels.append(1)
            else:
                normal_work_length = random.randint(0, 100)
                while normal_work_length > 0:
                    normal_work_length -= 1
                    self.update_graph()
                    self._attack_labels.append(0)

        train_data, train_predicate = self.train_data_formatter()

        return train_data[:data_size], train_predicate[:data_size]

    def train_data_formatter(self):
        train_data, train_predicate = [], []
        for index in range(len(self._attack_labels)):
            train_data.append(
                (self._cpu[index], self._ram[index],
                 self._traffic_value[index], self._connection_value[index])
            )
            train_predicate.append(self._attack_labels[index])

        return train_data, train_predicate

    @staticmethod
    def write_to_file(train_data, train_predicate):
        time_postfix = time.strftime('%Y-%M-%d-%H:%M:%S', time.gmtime())
        with open('./logs/[{}]train_data.txt'.format(time_postfix), 'w') as file:
            for items in zip(train_data, train_predicate):
                file.write(json.dumps(items) + '\n')


if __name__ == '__main__':
    gc = GraphCreator()
    train_data, train_predicate = gc.create_train_data(10000, 0.2)
    gc.write_to_file(train_data, train_predicate)
