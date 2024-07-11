from __future__ import annotations
import openpyxl

class TimesheetParser:
    """
    class to parse data from .xlsx file that contains timesheets and form .xlsx report
    """

    def __init__(self: TimesheetParser, filename: str) -> None:
        """
        :param filename: file name of .xlsx file that contains timesheets
        :raises FileNotFoundError: if there is no file named filename
        """
        self.workbook = openpyxl.load_workbook(filename=filename) # automatically raises FileNotFoundError if there is no such file



if __name__ == "__main__":
    obj = TimesheetParser("lol.xlsx")
