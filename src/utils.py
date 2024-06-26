from pandas import DataFrame, read_csv
import yaml


def get_conf():
    """
    Reads a YAML configuration file and returns the configuration as a dictionary.

    Parameters:
    - conf_path: Path to the YAML configuration file.

    Returns:
    - config: Dictionary containing the configuration settings.
    """
    with open('../conf/conf.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config



def read_csv_file(file_path: str, file_name:str) -> DataFrame:
    """
    Reads a CSV file from a specified path and returns it as a pandas DataFrame

    Parameters:
    - file_path: The path to the CSV file to be read.
    - file_name: The filename of the DataFrame to be read.

    Returns:
    - df: A pandas DataFrame containing the data from the specified CSV file.
    """
    if not file_path.endswith('/'):
        file_path += '/'
    
    read_path = f"{file_path}{file_name}.csv"

    df = read_csv(read_path)

    return df

def read_csv_file_with_rows(file_path: str, file_name:str, nrows:int) -> DataFrame:
    """
    Reads a CSV file from a specified path and returns it as a pandas DataFrame

    Parameters:
    - file_path: The path to the CSV file to be read.
    - file_name: The filename of the DataFrame to be read.

    Returns:
    - df: A pandas DataFrame containing the data from the specified CSV file.
    """
    if not file_path.endswith('/'):
        file_path += '/'
    
    read_path = f"{file_path}{file_name}.csv"

    df = read_csv(filepath_or_buffer=read_path,nrows=nrows)

    return df


def read_images():
    """
    Reads the images from the specified path and returns them as a list of numpy arrays.

    Parameters:"""
    return 0