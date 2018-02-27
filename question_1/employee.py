class Employee:
    def __init__(self, employee_id, first_name, last_name, address, department):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.department = department

    def jsonify(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "department": self.department
        }
