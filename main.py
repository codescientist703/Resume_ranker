import PyPDF2
import pypd
import os
from os import listdir
from os.path import isfile, join
from io import StringIO
import pandas as pd
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.matcher import PhraseMatcher

pdf_path = open('/home/madscientist/Downloads/graph.pdf', 'rb') 

s = pypd.get_text(pdf_path)
print(s)

