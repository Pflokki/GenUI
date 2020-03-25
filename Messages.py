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
        self.CPU = []
        self.RAM = []
        self.Connects = []
        self.Traffic = []

    def get_message(self):
        return json.dumps({
            't': self.tag,
            'cpu': self.CPU,
            'ram': self.RAM,
            'connects': self.Connects,
            'traffic': self.Traffic,
        }).encode()

    @classmethod
    def decode(cls, msg):
        if 't' in msg:
            if msg['t'] == cls.tag:
                instance = cls()
                instance.CPU = msg['cpu']
                instance.RAM = msg['ram']
                instance.Connects = msg['connects']
                instance.Traffic = msg['traffic']
                return instance
        else:
            raise TypeError

