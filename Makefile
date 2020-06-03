all: buildmo

buildmo:
	@echo "Building the mo files"
	# WARNING: the second sed below will only works correctly with the languages that don't contain "-"
	for file in `ls po/*.po`; do \
		lang=`echo $$file | sed 's@po/@@' | sed 's/\.po//' | sed 's/lights-on-//'`; \
		install -d opt/lights-on/locale/$$lang/LC_MESSAGES/; \
		msgfmt -o opt/lights-on/locale/$$lang/LC_MESSAGES/lights-on.mo $$file; \
	done \

clean:
	rm -rf opt/lights-on/locale
