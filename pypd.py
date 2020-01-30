import PyPDF2 as pypd 
mypath = ''
def get_text(file):
	pdffile = pypd.PdfFileReader(file)
	countpage = pdffile.getNumPages()
	count = 0
	text = []
	while count < countpage:
		cur_page = pdffile.getPage(count)
		t = cur_page.extractText()
		text.append(t)
		count = count + 1
	text = str(text)
	text = text.replace("\\n","")
	text = text.lower()
	return text

pdf_path = open('/home/madscientist/Downloads/graph.pdf', 'rb') 
print(get_text(pdf_path))

