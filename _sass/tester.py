# FILE IS TO TEST IF COPILOT IS BETTER IN PY THAN IPYNB
## IMPORTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


## MAKE DATA
# make gpa_dict
# make a dictionary of gpa's for each class for each quarter from fall 2017 to spring 2022

gpa_dict = {
    'fall_2017': {
        'class_1': 3,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'winter_2018': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'spring_2018': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'fall_2018': {
        'class_1': 3,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'winter_2019': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'spring_2019': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'fall_2019': {
        'class_1': 3,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'winter_2020': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'spring_2020': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'fall_2020': {
        'class_1': 3,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'winter_2021': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'spring_2021': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'fall_2021': {
        'class_1': 3,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    },
    'winter_2022': {
        'class_1': 3.5,
        'class_2': 3.5,
        'class_3': 3.5,
        'class_4': 3.5,
    }, 
}