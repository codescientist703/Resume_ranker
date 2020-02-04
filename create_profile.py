import pandas as pd
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.matcher import PhraseMatcher

def create_profile(text,main_frame):
	temp_frame = main_frame
	keyword_dict = pd.read_csv('keywords.csv')
	keyword_dict = keyword_dict.loc[:, ~keyword_dict.columns.str.contains('^Unnamed')]
	col_name = keyword_dict.columns.to_list()
	words = []
	for ele in col_name:
		temp = [nlp(text) for text in keyword_dict[ele].dropna(axis = 0)]
		words.append(temp)

	matcher = PhraseMatcher(nlp.vocab)
	for i in range(len(col_name)):
		matcher.add(col_name[i], None, *words[i])
	
	doc = nlp(text)
	matches = matcher(doc)
	d = {}
	for match_id, start, end in matches:
		rule_id = nlp.vocab.strings[match_id] 
		span = doc[start : end]  
		if rule_id in d:
			d[rule_id] = d[rule_id] + 1
		else:
			d[rule_id] = 1
	
	nd = {}
	nd['Candidate Names'] = 'Nihal'
	for u in col_name:
		if u not in d:
			nd[u] = 0
		else:
			nd[u] = d[u]

	temp_frame = temp_frame.append(nd, ignore_index=True)
	return temp_frame
	


 


	
	




