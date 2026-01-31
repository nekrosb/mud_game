class rooms:

    def __init__(self, name, content,):
        self.name = name
        self.content = content
        self.neighbours = {}
        self.items = []
        self.bots = []

    def add_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def print_name_and_discription(self):
        print(f"{self.name} \n {self.content}")

    def print_all_direction(self):
        print(f"you can go to this direction \n {self.neighbours}")

    def get_neighbour(self, direction):
        return self.neighbours[direction]