import os
import sys
import numpy as np
import dill
import yaml 
from pandas import DataFrame
from us_visa.exception import USVisaException
from us_visa.logger import logging


def read_yaml_file (file_path: str) -> dict:
    """
    This function reads a yaml file and returns its contents as a dictionary.
    """
    try:
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"File not found: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e


    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    This function writes a dictionary to a yaml file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        logging.error(f"Error writing to file: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e


def load_object(file_path: str) -> object:
    logging.info("Enter the load_object method of utils")
    try:
        with open(file_path, "rb") as file_object:
            obj = dill.load(file_object)
            logging.info("Exit the file load_object method of utils")
            return obj
    except Exception as e:
        logging.error(f"Error loading object from file: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """
    save numpy array data to file
    file_path: str location of the file
    array: np.array data to save

    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        logging.error(f"Error saving numpy array to file: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e
    

def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of the file
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        logging.error(f"Error loading numpy array from file: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e
    

def save_object(file_path: str, obj: object) -> None:
    """
    save object to file
    file_path: str location of the file
    obj: object data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        logging.error(f"Error saving object to file: {file_path} \n error: {e}")
        raise USVisaException(e, sys) from e
    

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    drop columns from DataFrame
    df: DataFrame object
    cols: list of column names to drop
    return: DataFrame object with dropped columns
    """
    try:
        return df.drop(columns=cols, axis=1)
    except Exception as e:
        logging.error(f"Error dropping columns from DataFrame: {df} \n error: {e}")
        raise USVisaException(e, sys) from e