from typing import List

# Runtime: 1072 ms, faster than 100.00% of Python3 online submissions for Design SQL.
# Memory Usage: 31.6 MB, less than 100.00% of Python3 online submissions for Design SQL.
class Table:
    def __init__(self):
        self.rows = {

        }
        self.counter = 1

    def insert_row(self, contents):
        self.rows[self.counter] = contents
        self.counter += 1

    def delete_row(self, row_id):
        del self.rows[row_id]

    def select_cell(self, row_id, column):
        return self.rows[row_id][column-1]


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {n: Table() for n in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        self.tables[name].insert_row(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        self.tables[name].delete_row(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name].select_cell(rowId, columnId)