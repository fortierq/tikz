-include ./.env
export

RULES_DIR=proof/deduction_rules
RULES_TEX=$(wildcard $(RULES_DIR)/*.tex)

run:
	python main.py ${TOKEN}
	git add -A
	git commit -m "Update"
	git push
pdf:
	python pdf.py

rules-pdf:
	@for f in $(RULES_TEX); do \
		echo "[pdf] $$f"; \
		latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(RULES_DIR) "$$f" || exit 1; \
	done

rules-png: rules-pdf
	@for f in $(RULES_TEX); do \
		base=$$(basename "$$f" .tex); \
		echo "[png] $(RULES_DIR)/$$base.pdf -> $(RULES_DIR)/$$base.png"; \
		convert -density 300 -units PixelsPerInch "$(RULES_DIR)/$$base.pdf" -quality 90 "$(RULES_DIR)/$$base.png" || exit 1; \
	done

rules-clean:
	@rm -f $(RULES_DIR)/*.aux $(RULES_DIR)/*.log $(RULES_DIR)/*.out $(RULES_DIR)/*.fls $(RULES_DIR)/*.fdb_latexmk