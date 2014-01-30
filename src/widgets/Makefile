all: communication startup mainscreen

communication:
	echo -ne "N\n" | taurusuic4 --execute linacOverview.ui --output=ui_linacOverview.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute linacPlcWidget.ui --output=ui_linacPlcWidget.py ; echo -ne "\n"

startup:
	echo -ne "N\n" | taurusuic4 --execute linacStartupSynoptic.ui --output=ui_linacStartupSynoptic.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute coolingLoop.ui --output=ui_coolingLoop.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute eGunLV.ui --output=ui_eGunLV.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute klystron1ictk.ui --output=ui_klystron1ictk.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute klystron2ictk.ui --output=ui_lystron2ictk.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute klystronLV.ui --output=ui_klystronLV.py ; echo -ne "\n"

mainscreen:
	echo -ne "N\n" | taurusuic4 --execute linacMainscreenSynoptic.ui --output=ui_linacMainscreenSynoptic.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute klystronHV.ui --output=ui_klystronHV.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute attenuator.ui --output=ui_attenuator.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute phaseShifter.ui --output=ui_phaseShifter.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute magnet.ui --output=ui_magnet.py ; echo -ne "\n"
	echo -ne "N\n" | taurusuic4 --execute eGunHV.ui --output=ui_eGunHV.py ; echo -ne "\n"
