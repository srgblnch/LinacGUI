####
# Makefile vbles help
# $@ -is the name of the target currently being processed.
# $< -is the name of the first dependency.

PYUIC = taurusuic4

COMM_UI = linacOverview.ui linacPlcWidget.ui
START_UI = linacStartupSynoptic.ui coolingLoop.ui eGunLV.ui \
           klystron1ictk.ui klystron2ictk.ui klystronLV.ui
MAIN_UI = linacMainscreenSynoptic.ui klystronHV.ui attenuator.ui \
          phaseShifter.ui magnet.ui eGunHV.ui beamChargeMonitors.ui
SNAPSHOT_UI = snapshot_coolingloops.ui snapshot_klystrons.ui \
              snapshot_radiofrequency.ui snapshot_vacuum.ui \
              snapshot_egun.ui snapshot_magnets.ui snapshot_timing.ui

UI_FILES = ui/$(COMM_UI) ui/$(START_UI) ui/$(MAIN_UI) ui/$(SNAPSHOT_UI)

################

UI_PY_FILES = $(UI_FILES:%.ui=ui_%.py)

#all: $(UI_PY_FILES)

ui_%.py: %.ui
	$(PYUIC) $< -o $@

clean:
	$(RM) $(UI_PY_FILES)

communications:
	taurusuic4 ui/linacOverview.ui  -o ui_linacOverview.py
	taurusuic4 ui/linacPlcWidget.ui -o ui_linacPlcWidget.py

startup:
	taurusuic4 ui/coolingLoop.ui          -o ui_coolingLoop.py
	taurusuic4 ui/eGunLV.ui               -o ui_eGunLV.py
	taurusuic4 ui/klystron1ictk.ui        -o ui_klystron1ictk.py
	taurusuic4 ui/klystron2ictk.ui        -o ui_klystron2ictk.py
	taurusuic4 ui/klystronLV.ui           -o ui_klystronLV.py
	taurusuic4 ui/linacStartupSynoptic.ui -o ui_linacStartupSynoptic.py

mainscreen:
	taurusuic4 ui/eGunHV.ui                  -o ui_eGunHV.py
	taurusuic4 ui/klystronHV.ui              -o ui_klystronHV.py
	taurusuic4 ui/attenuator.ui              -o ui_attenuator.py
	taurusuic4 ui/phaseShifter.ui            -o ui_phaseShifter.py
	taurusuic4 ui/magnet.ui                  -o ui_magnet.py
	taurusuic4 ui/beamChargeMonitors.ui      -o ui_beamChargeMonitors.py
	taurusuic4 ui/linacMainscreenSynoptic.ui -o ui_linacMainscreenSynoptic.py

snapshot:
	taurusuic4 ui/snapshot_coolingloops.ui    -o ui_snapshot_coolingloops.py
	taurusuic4 ui/snapshot_egun.ui            -o ui_snapshot_egun.py
	taurusuic4 ui/snapshot_klystrons.ui       -o ui_snapshot_klystrons.py
	taurusuic4 ui/snapshot_magnets.ui         -o ui_snapshot_magnets.py
	taurusuic4 ui/snapshot_radiofrequency.ui  -o ui_snapshot_radiofrequency.py
	taurusuic4 ui/snapshot_timing.ui          -o ui_snapshot_timing.py
	taurusuic4 ui/snapshot_vacuum.ui          -o ui_snapshot_vacuum.py
	taurusuic4 ui/linacConfigurationScreen.ui -o linacConfigurationScreen.ui

all: communications startup mainscreen snapshot