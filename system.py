
import json


class Project:
    def __init__(self):
        self.id = 0
        self.sum = None
        self.data_result = []
        self.status = ''

    def action(self, x, y, z):
        if z == "+":
            self.sum = x + y
        elif z == "-":
            self.sum = x - y
        elif z == "*":
            self.sum = x * y
        elif z == "/":
            self.sum = x / y
        self.id += 1
        self.data_result.append({
            "id": self.id,
            "result": self.sum,
            "status": self.status
        })

    def status_request(self, a, b):
        j = f"{a} {b}"
        self.status = j

    def id_show(self):
        return {"message": f"id {self.id}"}

    def result(self):
        return json.dumps(self.data_result)
