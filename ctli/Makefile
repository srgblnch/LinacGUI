PYUIC = taurusuic4

all: ui

ui: widgets application

application:
	$(PYUIC) ctli.ui -o ui_ctli.py

widgets:
	cd widgets && $(MAKE)

clean:
	$(RM) ui_ctli.py
	make -C widgets clean
