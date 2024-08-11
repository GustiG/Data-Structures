# mark pages with an x
class Page:
    def __init__(self, dimension):
        if dimension in ['A4', '2/A4']:
            self.dimension = dimension
        else:
            raise ValueError("Invalid dimension. Choose 'A4' or '2/A4'.")

    def x(self):
        pages_no = input("Number of pages: ")
        


# Example usage:
page = Page('A4')
print(page.dimension)  # Output: A4

