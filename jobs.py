import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
from data import Data

class Job: 
    def __init__(self,lang_name: str):
        self.lang_name = lang_name
        self.date_dictionary = {}
        self.job_dictionary = {self.lang_name:{}}
        
    """Method for webscraping and data cleansing using beautiful soup"""
    def job_seeker(self) -> float:
        seek_html = urlopen(f"https://www.seek.com.au/jobs?keywords={self.lang_name}")
        indeed_html = urlopen(f"https://au.indeed.com/jobs?q={self.lang_name}&l=")
        bs = BeautifulSoup(seek_html.read(), "html.parser")
        bs_2 = BeautifulSoup(indeed_html.read(), "html.parser")
        raw_data_seek = (bs.find("strong", {"data-automation": "totalJobsCount"}))
        raw_data_indeed = (bs_2.find("div", {"id": "searchCountPages"}))
        try:
            raw_data_1 = int((raw_data_seek.text).replace(",", ""))
            raw_data_2 = int(((raw_data_indeed.text.strip())[10:-5]).replace(",", ""))
        except:
            raw_data_1 = 0
            raw_data_2 = 0

        
        job_average = (raw_data_1 + raw_data_2)/2
        self.job_average = job_average
        return self.job_average
        
    """Method for opening and appending to Json data file using methods from data.py"""
    def data_update_process(self):
        lang_data_file = Data.load("language_data.json")
        self.date_dictionary.update({str(date.today()):self.job_average})
        if self.lang_name not in lang_data_file.keys():
            lang_data_file.update({self.lang_name: self.date_dictionary})
        else:
            lang_data_file[self.lang_name].update(self.date_dictionary)

        return Data.save("language_data.json", lang_data_file)