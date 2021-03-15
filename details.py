from language_list import list_of_languages
from jobs import Job 
from tabulate import tabulate
from job_statistics import Stats
    

def details():
    lang_name = []
    lang_info = []
    for lang in list_of_languages:
        prog_lang = Stats(lang)
        """Table content creation for each programming lanaguage job market"""
        lang_name.append(prog_lang.name)
        lang_info.append(prog_lang.table_content)
    detail_return = dict(zip(lang_name, lang_info))
    return (detail_return)


# print(type(details()))

    # """Creating table for display"""
    # table = tabulate(table_info, headers = ["Today's Job Postings", "Net Change", "% Change","1 Month", "Last Updated"] )