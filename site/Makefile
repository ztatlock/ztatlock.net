PUBS_DIR=$(HOME)/Dropbox/ztatlock-pubs

TALKS_DIR=$(HOME)/Dropbox/ztatlock-talks

PAGES=$(wildcard *.md)
STAGE_PAGES=$(patsubst %.md,stage/%.html,$(PAGES))

INCLUDE=$(wildcard include/*)
STAGE_INCLUDE=$(patsubst include/%,stage/%,$(INCLUDE))

.PHONY: stage
stage: stage/pubs stage/talks $(STAGE_PAGES) $(STAGE_INCLUDE)

stage/pubs:
	[ -d "$(PUBS_DIR)" ] && ln -s $(PUBS_DIR) stage/pubs

stage/talks:
	[ -d "$(TALKS_DIR)" ] && ln -s $(TALKS_DIR) stage/talks

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
	cp -r $< stage/

.PHONY: sync
sync:
	rsync \
		--verbose \
		--recursive \
		--copy-dirlinks \
		--delete \
		--force \
		stage/ ztatlock@tatlock.net:/var/www/tatlock.net

.PHONY: publish
publish: stage sync

.PHONY: clean
clean:
	rm -rf stage/*
