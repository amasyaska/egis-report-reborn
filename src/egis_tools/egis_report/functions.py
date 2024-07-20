import os

def get_report_html(fields_amount: int) -> str:
    """
    :param fields_amount: amount of fields to generate report
    :returns html_output: html page with corresponding amount of fields
    """
    html_output = None
    basepath = os.path.dirname(__file__)                            # get absolute path to this file
    filepath = os.path.abspath(os.path.join(basepath, "templates", "index_files_input.html"))
    with open(filepath, "r") as f:        # html file contains "{}" in place to format to html_addable
        html_output = f.read()
    html_addable = ""
    for i in range(fields_amount):
        html_addable += f"""<label for="xlsx_file_{i}">Enter file url: </label>
            <input type="text" name="xlsx_file_{i}"><br>"""
    html_output = html_output.format(html_addable)
    return html_output
