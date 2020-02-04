import pypd
import os
from create_profile import create_profile
from os import listdir
from os.path import isfile, join
from io import StringIO
import pandas as pd
from collections import Counter


pdf_path = open('/home/madscientist/Downloads/docu.pdf', 'rb') 

keyword_dict = pd.read_csv('keywords.csv')
keyword_dict = keyword_dict.loc[:, ~keyword_dict.columns.str.contains('^Unnamed')]
col_name = keyword_dict.columns.to_list()
col_name = ['Candidate Names'] + col_name
#print(col_name)
main_frame = pd.DataFrame(columns=col_name)
main_frame.set_index('Candidate Names')
text = pypd.get_text(pdf_path)
main_frame = create_profile(text,main_frame)
print(main_frame)
main_frame.to_csv('profile.csv', sep='\t', encoding='utf-8', index=False)








