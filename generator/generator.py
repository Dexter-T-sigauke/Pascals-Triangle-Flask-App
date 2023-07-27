
class Generator:
    def generate(self, rows: int) -> list[list[int]]:
        """The generator code"""
        if rows == 0:
            return []
        elif rows == 1:
            return [[1]]
        else:
            triangle = self.generate(rows - 1)
            last_row = triangle[-1]
            new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
            triangle.append(new_row)
            return triangle
