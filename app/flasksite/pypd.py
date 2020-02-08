
import slate3k as slate

def get_text(path):
	with path as f:
		extracted_text = slate.PDF(f)
		s = extracted_text.text()
	return s



	

