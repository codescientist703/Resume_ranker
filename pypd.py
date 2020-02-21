
import slate3k as slate

def get_text(path):
	true_path = open(path, 'rb')
	with true_path as f:
		extracted_text = slate.PDF(f)
		s = extracted_text.text()
		s = s.lower()
	return s



	

