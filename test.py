import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import logging
from tqdm import tqdm
import time
import sys


def start_check()->int:
    path = './completed_urls.txt'
    if not os.path.isfile(path):
        s=0
        f = open(path,'w+')
        print(f'{path} file was created')
        
    else:
        f = open(path,'r')
        if f.mode == 'r':
            snumber = f.read()
        s=int(snumber)
        print(f'file {path} exists!')
    
    return s
