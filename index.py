class ComplexAlgorithm:
    def __init__(self):
        self.data = [5, 10, 3, 8, 1, 12, 9]

    def execute(self):
        self.sort_data()
        self.perform_calculations()

    def sort_data(self):
        # Sort the data in descending order
        self.data.sort(reverse=True)

    def perform_calculations(self):
        total = sum(self.data)
        average = total / len(self.data)
        print("Data:", self.data)
        print("Total:", total)
        print("Average:", average)

if __name__ == "__main__":
    algorithm = ComplexAlgorithm()
    algorithm.execute()
