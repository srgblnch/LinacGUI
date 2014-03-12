####
# Makefile vbles help
# $@ -is the name of the target currently being processed.
# $< -is the name of the first dependency.

PYUIC = taurusuic4

COMM_UI = linacOverview.ui linacPlcWidget.ui
START_UI = linacStartupSynoptic.ui coolingLoop.ui eGunLV.ui \
           klystron1ictk.ui klystron2ictk.ui klystronLV.ui
MAIN_UI = linacMainscreenSynoptic.ui klystronHV.ui attenuator.ui \
          phaseShifter.ui magnet.ui eGunHV.ui
SNAPSHOT_UI = snapshot_coolingloops.ui snapshot_klystrons.ui \
              snapshot_radiofrequency.ui snapshot_vacuum.ui \
              snapshot_egun.ui snapshot_magnets.ui snapshot_timing.ui

UI_FILES = ui/$(COMM_UI) ui/$(START_UI) ui/$(MAIN_UI) ui/$(SNAPSHOT_UI)

################

UI_PY_FILES = $(UI_FILES:%.ui=ui_%.py)

all: $(UI_PY_FILES)

ui_%.py: %.ui
	$(PYUIC) $< -o $@

clean:
	$(RM) $(UI_PY_FILES)
