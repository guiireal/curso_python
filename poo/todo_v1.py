from datetime import datetime


class Task:
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.now()
        self.completed_at = False

    def complete(self):
        self.completed_at = True

    def __str__(self):
        return self.description + (" (concluída)" if self.completed_at else "")


def main():
    house = []
    house.append(Task("Passar roupa"))
    house.append(Task("Lavar louça"))
    house.append(Task("Limpar o chão"))

    [task.complete() for task in house if task.description == "Lavar louça"]

    for task in house:
        print(f"- {task}")


if __name__ == "__main__":
    main()
