import os
import pandas as pd

def read_csv_data(base_path, subfolder, inner_folder, file_name):
    """
    Read data from a CSV file located in a specified directory.

    Parameters:
    base_path (str): The base directory path.
    subfolder (str): The subfolder within the base directory.
    inner_folder (str): The inner folder within the subfolder.
    file_name (str): The name of the CSV file to read.

    Returns:
    pd.DataFrame or None: A pandas DataFrame containing the data if the file exists, or None if it doesn't.
    """
    folder_path = os.path.join(base_path, subfolder, inner_folder, file_name)
    if os.path.exists(folder_path):
        return pd.read_csv(folder_path)
    return None
