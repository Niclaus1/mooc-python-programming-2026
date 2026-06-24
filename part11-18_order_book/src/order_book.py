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
        return (finished_count, unfinished_count, finished_amount, unfinished_amount)


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
