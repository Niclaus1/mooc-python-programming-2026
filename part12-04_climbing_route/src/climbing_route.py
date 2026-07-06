class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def by_length(route: ClimbingRoute):
    return route.length


def by_grade(route: ClimbingRoute):
    return (route.grade, route.length)


# Write your solution here:
def sort_by_length(routes: list):
    return sorted(routes, key=by_length, reverse=True)


def sort_by_difficulty(routes: list):
    return sorted(routes, key=by_grade, reverse=True)


if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 9, "7A")
    r3 = ClimbingRoute("Syncro", 14, "8C+")
    reply = sort_by_difficulty([r1, r2, r3])

    for route in reply:
        print(route)
