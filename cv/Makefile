TARGETS = \
	ztatlock-cv.pdf

LATEXMK = latexmk -outdir=out

.PHONY: all
all: $(TARGETS)

%.pdf: %.tex
	$(LATEXMK) -pdf $<
	ln -sf out/$@ .

.PHONY: clean
clean:
	$(LATEXMK) -C
	rm -f $(TARGETS)
