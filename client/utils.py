from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressDialog, QApplication
import sys

def parseToDictWithProgress(data, desc, cursor):
    result_list = []
    columns = [column[0] for column in cursor.description]  # Get the column names

    if 'unittest' in sys.modules:
        # If running in a unit test environment, perform a simplified parsing without progress dialog
        for row in data:
            result_dict = dict(zip(columns, row))
            result_list.append(result_dict)
    else:
        # Perform parsing with progress dialog
        progress_dialog = QProgressDialog(desc, None, 0, len(data))
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setWindowTitle("Progress")
        progress_dialog.show()

        for i, row in enumerate(data):
            result_dict = dict(zip(columns, row))
            result_list.append(result_dict)
            progress_dialog.setValue(i + 1)
            QApplication.processEvents()

        progress_dialog.accept()  # Close the progress dialog when finished

    return result_list
