import yaml
import pandas as pd
from dotenv import dotenv_values



env_name = "config_env.env" # following example.env template change to your own .env file name
config = dotenv_values(env_name)


def get_conf(conf_path='conf\conf.yml'):
    """_Thos functon returns the configuration details of the project. It reads the conf.yml file and returns the configuration details as a dictionary._
    Args:
        conf_path (str, optional): Path configurations to the project. Defaults to 'conf\conf.yml' includes paths, models, parameters, etc.

    Returns:
        conf (dictionary): returns the configuration details as a dictionary.
    """
    with open(conf_path, "r") as f:
        conf = yaml.safe_load(f)
    return conf



def get_csv_data(task_type):
    """This returs the csv data files for a given task type. Task type can be train, test or eval.
    Args:
        task_type (str): train/test/eval

    Returns:
        data (dataframe): returns the csv data file as a dataframe.
    """
    conf = get_conf()
    if task_type == "train":
        path = conf["paths"]["training_data_csv"]
    elif task_type == "test":
        path = conf["paths"]["test_data_csv"]
    elif task_type == "eval":
        path = conf["paths"]["eval_data_csv"]
    else:
        print("Invalid task type")
    data = pd.read_csv(path)
    return data



def get_img_data(task_type):
    """This returs the image data files for a given task type. Task type can be train, test or eval.
    Args:
        task_type (str): train/test/eval

    Returns:
        data (dataframe): returns the images in a folder
    """
    conf = get_conf()
    if task_type == "train":
        path = conf["paths"]["training_data_images"]
    elif task_type == "test":
        path = conf["paths"]["test_data_images"]
    elif task_type == "eval":
        path = conf["paths"]["eval_data_images"]
    else:
        print("Invalid task type")
    images = ""
    return images


def get_csv_files():
    train_data_csv = config['train_csv_data']
    test_data_csv = config['test_csv_data']
    validate_data_csv = config['validate_csv_data']
    return train_data_csv, test_data_csv, validate_data_csv

def get_img_path():
    train_img_path = config['train_imgs_path']
    test_img_path = config['test_imgs_path']
    validate_img_path = config['validate_imgs_path']
    return train_img_path, test_img_path, validate_img_path
    

