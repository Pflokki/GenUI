import json


class Message:
    def __init__(self):
        self.tag = "Ping"

    def get_message(self):
        return json.dumps({'t': self.tag}).encode()

    def decode(self, msg):
        if 't' in msg:
            if msg['t'] == self.tag:
                return self
        else:
            raise TypeError


class StartAttackMessage(Message):
    def __init__(self):
        super().__init__()
        self.tag = "StartAttack"


class StopAttackMessage(Message):
    def __init__(self):
        super().__init__()
        self.tag = "StopAttack"


class GetStatus(Message):
    def __init__(self):
        super().__init__()
        self.tag = "GetStatus"
