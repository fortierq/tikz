include ./.env
export
run:
	python main.py ${TOKEN}
	git add -A
	git commit -m "Update"
	git push
pdf:
	python pdf.py