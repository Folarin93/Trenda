from language_list import list_of_languages
from jobs import Job 

"""For Loop for updating json file holding jobs for each programming language """
for lang in list_of_languages:
    language = Job(lang)
    language.job_seeker()
    language.data_update_process()
    