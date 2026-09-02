class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["name"],
            data["description"],
            data["priority"]
        )