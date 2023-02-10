include .env
export
run:
	python main.py ${TOKEN}
pdf:
	python pdf.py