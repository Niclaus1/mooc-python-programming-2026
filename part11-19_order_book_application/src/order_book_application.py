# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
class Task:
    id = 0

    def __init__(
        self,
        description: str,
        programmer: str,
        workload: int,
    ):
        Task.id += 1
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.status = False
        self.id = Task.id

    def __str__(self):
        if self.status:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

    def mark_finished(self):
        self.status = True

    def is_finished(self):
        if self.status:
            return True
        else:
            return False


class OrderBook:
    def __init__(self):
        self._book_List = []

    def add_order(
        self,
        description: str,
        programmer: str,
        workload: int,
    ):
        self._book_List.append(Task(description, programmer, workload))
        print("added!\n")

    def all_orders(self):
        return self._book_List

    def programmers(self):
        unique_List = set([name.programmer for name in self._book_List])
        return list(unique_List)

    def mark_finished(self, id: int):
        found = False
        for name in self._book_List:
            if name.id == id:
                name.mark_finished()
                found = True
                print("marked as finished")
        if not found:
            raise ValueError

    def unfinished_orders(self):
        return [task for task in self._book_List if not task.status]

    def finished_orders(self):
        return [task for task in self._book_List if task.status]

    def status_of_programmer(self, programmer: str):
        programmer_Data = [
            task for task in self._book_List if task.programmer == programmer
        ]

        finished = [status for status in programmer_Data if status.status]
        unfinished = [status for status in programmer_Data if not status.status]

        finished_count = len(finished)
        finished_amount = sum([work.workload for work in finished])

        unfinished_count = len(unfinished)
        unfinished_amount = sum([work.workload for work in unfinished])

        if not programmer_Data:
            raise ValueError
        return f"tasks: finished {finished_count} not finished {unfinished_count}, hours: done {finished_amount} scheduled {unfinished_amount}"


class Application(OrderBook):
    def __init__(self):
        super().__init__()

    def main(self):
        print(
            "commands:\n"
            "0 exit\n"
            "1 add order\n"
            "2 list finished tasks\n"
            "3 list unfinished tasks\n"
            "4 mark task as finished\n"
            "5 programmers\n"
            "6 status of programmer\n"
        )

        while True:
            try:
                command = input("command:")
                match command:
                    case "0":
                        break
                    case "1":
                        description = input("description:")
                        programmer, workload = input(
                            "programmer and workload estimate:"
                        ).split()
                        workload = int(workload)
                        self.add_order(description, programmer, workload)

                    case "2":
                        finished_list = self.finished_orders()
                        if not finished_list:
                            print("no finished tasks")

                        for task in finished_list:
                            print(task)
                        print()

                    case "3":
                        pass
                        unfinished_list = self.unfinished_orders()
                        if not unfinished_list:
                            return "no unfinished tasks"

                        for task in unfinished_list:
                            print(task)
                        print()

                    case "4":
                        self.mark_finished(int(input("id: ")))
                        print()

                    case "5":
                        for person in self.programmers():
                            print(person)
                        print()

                    case "6":
                        programmer = input("programmer:")
                        print(self.status_of_programmer(programmer))
                        print()
                    case _:
                        print("erroneous input")
                        continue
            except ValueError:
                print("erroneous input")
                continue


app = Application()
app.main()
