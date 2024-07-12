from __future__ import annotations
import openpyxl

class TimesheetParser:
    """
    class to parse data from list of .xlsx files (of particular format) that contain timesheets and form .xlsx report
    """

    def __init__(self: TimesheetParser, filenames: list[str]) -> None:
        """
        :param filenames: list of file names of .xlsx files that contain timesheets
        :raises FileNotFoundError: if there is no file named filename
        """
        self.workbook_list = list()
        for filename in filenames:
            self.workbook_list.append(openpyxl.load_workbook(filename=filename)) # automatically raises FileNotFoundError if there is no such file

    def get_report_by_project_name(project_name: str, project_pseudonyms: list[str]) -> dict[dict[str, float]]:
        """
        :param project_name: string that represents project name in timesheet
        :param project_pseudonyms: list of pseudonyms that can be used as an alternative project name (mainly for legacy support)
        :returns report: report is a dictionary in format {section1: {employee1: hours, ...}, section2: {employee1: hours, ...}, ...}
        """
        report = dict()

    @staticmethod
    def find_timesheet_table_coordinates_by_sheet(sheet: openpyxl.worksheet.worksheet.Worksheet) -> tuple[int, int, int, int]:
        """
        different timesheets can have different coordinates of start and end, this function searches for table coordinates based on top-right, top-left, bottom-right and bottom-left cell values.
        :param sheet: openpyxl sheet that has timesheet table
        :raises ValueError: if table coordinates cannot be found
        :returns coordinates: tuple of four coordinates of timesheet table: row_start, row_end, column_start, column_end
        """
        # setting variables to None in order to be able to check if they had been set after search 
        row_start = None
        row_end = None
        column_start = None
        column_end = None

        # timesheet table borders are defined by top-right, top-left, bottom-right and bottom-left cell values
        # right now, top-left has "Day" and cell on the right has "Working days(%)" / "Hours worked(%)" / "Number of hours"
        # top-right has "Scope of design work(short description of performed activities)" and cell on the right has "Type of work"
        # bottom-left has "Approval by the supervising person"
        for row in sheet.iter_rows():
            for cell in row:
                if (type(cell.value) != str):
                    continue
                hours_possible_column_names = ["workingdays(%)", "numberofhours", "hoursworked(%)"]
                if ( (cell.value.replace(" ", "").lower() == "day") and (sheet.cell(row=cell.row, column=cell.column + 1).value.replace(" ", "").lower() in hours_possible_column_names) ):
                    row_start = cell.row
                    column_start = cell.column
                if ( (cell.value.replace(" ", "").lower() == '''Scope of design work
                    (short description of performed activities)'''.replace(" ", "").lower()) and (sheet.cell(row=cell.row, column=cell.column + 1).value.replace(" ", "").lower() == "Тype of work".replace(" ", "").lower()) ):
                    column_end = cell.column
                if (cell.value.replace(" ", "").lower() == "Approval by the supervising person".replace(" ", "").lower()):
                    row_end = cell.row
        
        print(f"row_start: {row_start}, column_start: {column_start}, row_end: {row_end}, column_end: {column_end}")

        if (row_start == None or column_start == None):  # if start coordinates of table hadn't been found
            raise ValueError(f"Start of timesheet table hadn't been found. Sheet: {sheet.title}")
        
        if (row_end == None or column_end == None):
            raise ValueError(f"End of timesheet table hadn't been found. Sheet: {sheet.title}")

        return (row_start, column_start, row_end, column_end)

if __name__ == "__main__":
    obj = TimesheetParser(["test_3_month.xlsx"])
    for sheet in obj.workbook_list[0]:
        try:
            print(TimesheetParser.find_timesheet_table_coordinates_by_sheet(sheet))
        except Exception as ex:
            print(f"{ex} happened")
