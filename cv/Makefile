ztatlock-cv.pdf: ztatlock-cv.tex
	latexmk -pdf -pdflatex='pdflatex -interaction=nonstopmode -halt-on-error' ztatlock-cv.tex

.PHONY: clean
clean:
	latexmk -C
