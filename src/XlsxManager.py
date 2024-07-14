from __future__ import annotations
import os
import urllib.request

class XlsxManager:
    """
    class to work with different xlsx origins (from local files/url) and unify their representation
    it stores all files in resources directory
    """
    
    def __init__(self: XlsxManager) -> None:
        self.is_loaded = False  # flag to check if file was loaded (to be able to output)

    @staticmethod
    def get_xlsx_file_from_url_google_docs(url: str) -> str:
        """
        Loads file from google docs url (using urllib) and saves to resources directory (using docs id as name)
        :param url: google docs url that contains xlsx file
        :raises ValueError: if url is wrong (not google docs one)
        :returns filename: as a result of an execution, a new file called *filename* (docs id) will be created in resources directory
        """
        if (url[:39] != "https://docs.google.com/spreadsheets/d/"):     # url to :39 is https://docs.google.com/spreadsheets/d/, tested
            raise ValueError("url should be in format: https://docs.google.com/spreadsheets/d/<file_code>")
        docs_id = url.split('/')[5]
        basepath = os.path.dirname(__file__)                            # get absolute path to this file
        filepath = os.path.abspath(os.path.join(basepath, "..", "resources", f"{docs_id}.xlsx"))
        url_to_download = f"https://docs.google.com/spreadsheets/d/{docs_id}/export?format=xlsx" # adding /export?format=xlsx to url to download from google docs
        with urllib.request.urlopen(url_to_download) as response, open(filepath, "wb") as file:
            buff = response.read()
            file.write(buff)
        return f"{docs_id}.xlsx"

if __name__ == "__main__":
    obj = XlsxManager()
    print(obj.get_xlsx_file_from_url_google_docs(input("Enter url: ")))
