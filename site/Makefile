PAGES=$(wildcard *.md)
STAGE_PAGES=$(patsubst %.md,stage/%.html,$(PAGES))

INCLUDE=$(wildcard include/*)
STAGE_INCLUDE=$(patsubst include/%,stage/%,$(INCLUDE))

THUMB_DIR=$(HOME)/Dropbox/ztatlock.net-thumbs/thumb
PUBS_DIR=$(HOME)/Dropbox/ztatlock.net-pubs
TALKS_DIR=$(HOME)/Dropbox/ztatlock.net-talks

.PHONY: stage
stage: $(STAGE_PAGES) $(STAGE_INCLUDE) stage/thumb stage/pubs stage/talks

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

stage/thumb:
	[ -d "$(THUMB_DIR)" ] && ln -s "$(THUMB_DIR)" stage/thumb

stage/pubs:
	[ -d "$(PUBS_DIR)" ] && ln -s "$(PUBS_DIR)" stage/pubs

stage/talks:
	[ -d "$(TALKS_DIR)" ] && ln -s "$(TALKS_DIR)" stage/talks

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

.PHONY: clean
clean:
	rm -rf stage/*
