import pdfplumber
import re
pdf = pdfplumber.open("The_Living_World.pdf")
l=len(pdf.pages)

for i in range(0,l):
	page = pdf.pages[i]
	text = page.extract_text()

	questions = re.compile(r'^[0-9]. *')
	mcq = re.compile(r'^[(][0-9][)] *')
	sol = re.compile(r'^[S][o][l][.] *')
	r = re.compile(r'^[R][ ][:] *')
	for line in text.split('\n'):
		if questions.match(line) or mcq.match(line) or sol.match(line) or r.match(line):
			print(line)
	
