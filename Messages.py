import json


class Message:
    tag = "Ping"

    def __init__(self):
        pass

    def get_message(self):
        return json.dumps({'t': self.tag}).encode()

    @classmethod
    def decode(cls, msg):
        if 't' in msg:
            if msg['t'] == cls.tag:
                return cls()
        else:
            raise TypeError


class StartAttackMessage(Message):
    tag = "StartAttack"

    def __init__(self):
        super().__init__()


class StopAttackMessage(Message):
    tag = "StopAttack"

    def __init__(self):
        super().__init__()


class GetStatus(Message):
    tag = "GetStatus"

    def __init__(self):
        super().__init__()


class DieMessage(Message):
    tag = "Die"

    def __init__(self):
        super().__init__()


class ClientStatus(Message):
    tag = "ClientStatus"

    def __init__(self):
        super().__init__()
        self.cpu = []
        self.ram = []
        self.connection_value = []
        self.traffic_value = []

    def get_message(self):
        return json.dumps({
            't': self.tag,
            'cpu': self.cpu,
            'ram': self.ram,
            'connects': self.connection_value,
            'traffic': self.traffic_value,
        }).encode()

    @classmethod
    def decode(cls, msg):
        if 't' in msg:
            if msg['t'] == cls.tag:
                instance = cls()
                instance.cpu = msg['cpu']
                instance.ram = msg['ram']
                instance.connection_value = msg['connects']
                instance.traffic_value = msg['traffic']
                return instance
        else:
            raise TypeError

