TPAGES=$(wildcard *.template)
MPAGES=$(wildcard *.md) $(patsubst %.template,%.md,$(TPAGES))
STAGE_PAGES=$(patsubst %.md,stage/%.html,$(MPAGES))

INCLUDE=$(wildcard include/*)
STAGE_INCLUDE=$(patsubst include/%,stage/%,$(INCLUDE))

THUMB_DIR=$(HOME)/Dropbox/ztatlock.net/thumbs/thumb
PUBS_DIR=$(HOME)/Dropbox/ztatlock.net/pubs
TALKS_DIR=$(HOME)/Dropbox/ztatlock.net/talks

.PHONY: stage
stage: \
	$(STAGE_INCLUDE) \
	stage/thumb \
	stage/pubs \
	stage/talks \
	stage/sitemap.xml \
	stage/ztatlock-cv.pdf \
	$(STAGE_PAGES)

publications.md: publications.template ../pubs.json
	python3 gen-pubs.py

stage/%.html: %.md TEMPLATE.html REFLINKS
	@echo PANDOC $<
	@pandoc \
		--from=markdown \
		--to=html5 \
		--template=TEMPLATE.html \
		--standalone \
		--fail-if-warnings \
		$< REFLINKS --output=$@

stage/%: include/%
	cp -r $< $@

stage/thumb:
	[ -d "$(THUMB_DIR)" ] && ln -s "$(THUMB_DIR)" $@

stage/pubs:
	[ -d "$(PUBS_DIR)" ] && ln -s "$(PUBS_DIR)" $@

stage/talks:
	[ -d "$(TALKS_DIR)" ] && ln -s "$(TALKS_DIR)" $@

stage/sitemap.xml: $(MPAGES) mksitemap.sh
	./mksitemap.sh > $@

stage/ztatlock-cv.pdf: ../cv/ztatlock-cv.tex
	$(MAKE) --directory ../cv ztatlock-cv.pdf
	cp ../cv/ztatlock-cv.pdf $@

.PHONY: sync
sync:
	rsync \
		--verbose \
		--recursive \
		--copy-dirlinks \
		--delete \
		--force \
		stage/ ztatlock@ztatlock.net:/var/www/ztatlock.net

.PHONY: publish
publish: stage sync

.PHONY: check
check: stage
	html5validator \
	  --root stage/ \
	  --also-check-css \
	  --show-warnings \
	  --format text 2>&1 \
	| tr -d "'" \
	| awk 'BEGIN {RS=","; ORS="\n"} /Error/ || /Warning/ {print "\n"} {print $$0}'

.PHONY: clean
clean:
	rm -rf publications.md
	rm -rf stage/*
