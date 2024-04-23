# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_UED.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
from pyqtgraph import ImageView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1396, 1010)
        self.actionDetector = QAction(MainWindow)
        self.actionDetector.setObjectName(u"actionDetector")
        self.actionLeak_valve = QAction(MainWindow)
        self.actionLeak_valve.setObjectName(u"actionLeak_valve")
        self.actionSOL_Heater = QAction(MainWindow)
        self.actionSOL_Heater.setObjectName(u"actionSOL_Heater")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.vertical_cross_frame = QFrame(self.centralwidget)
        self.vertical_cross_frame.setObjectName(u"vertical_cross_frame")
        self.horizontalLayout = QHBoxLayout(self.vertical_cross_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.vertical_cross_plot = PlotWidget(self.vertical_cross_frame)
        self.vertical_cross_plot.setObjectName(u"vertical_cross_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_cross_plot.sizePolicy().hasHeightForWidth())
        self.vertical_cross_plot.setSizePolicy(sizePolicy)
        self.vertical_cross_plot.setMinimumSize(QSize(0, 150))

        self.horizontalLayout.addWidget(self.vertical_cross_plot)


        self.gridLayout.addWidget(self.vertical_cross_frame, 1, 1, 1, 1)

        self.main_image = ImageView(self.centralwidget)
        self.main_image.setObjectName(u"main_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_image.sizePolicy().hasHeightForWidth())
        self.main_image.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.main_image, 0, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.millis_btn = QRadioButton(self.frame_3)
        self.millis_btn.setObjectName(u"millis_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.millis_btn.sizePolicy().hasHeightForWidth())
        self.millis_btn.setSizePolicy(sizePolicy3)
        self.millis_btn.setLayoutDirection(Qt.LeftToRight)
        self.millis_btn.setChecked(True)

        self.gridLayout_3.addWidget(self.millis_btn, 0, 1, 1, 1)

        self.micros_btn = QRadioButton(self.frame_3)
        self.micros_btn.setObjectName(u"micros_btn")
        sizePolicy3.setHeightForWidth(self.micros_btn.sizePolicy().hasHeightForWidth())
        self.micros_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.micros_btn, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 6, 0, 1, 1)

        self.exposure_slider = QSlider(self.groupBox)
        self.exposure_slider.setObjectName(u"exposure_slider")
        sizePolicy1.setHeightForWidth(self.exposure_slider.sizePolicy().hasHeightForWidth())
        self.exposure_slider.setSizePolicy(sizePolicy1)
        self.exposure_slider.setMinimum(1)
        self.exposure_slider.setMaximum(10000)
        self.exposure_slider.setSliderPosition(1000)
        self.exposure_slider.setOrientation(Qt.Vertical)
        self.exposure_slider.setInvertedAppearance(False)
        self.exposure_slider.setInvertedControls(False)
        self.exposure_slider.setTickPosition(QSlider.TicksBothSides)
        self.exposure_slider.setTickInterval(1000)

        self.gridLayout_2.addWidget(self.exposure_slider, 1, 1, 6, 1)

        self.expo200_btn = QPushButton(self.groupBox)
        self.expo200_btn.setObjectName(u"expo200_btn")
        sizePolicy3.setHeightForWidth(self.expo200_btn.sizePolicy().hasHeightForWidth())
        self.expo200_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.expo200_btn, 5, 0, 1, 1)

        self.live_acquire_btn = QPushButton(self.groupBox)
        self.live_acquire_btn.setObjectName(u"live_acquire_btn")
        sizePolicy3.setHeightForWidth(self.live_acquire_btn.sizePolicy().hasHeightForWidth())
        self.live_acquire_btn.setSizePolicy(sizePolicy3)
        self.live_acquire_btn.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout_2.addWidget(self.live_acquire_btn, 2, 0, 1, 1)

        self.expo500_btn = QPushButton(self.groupBox)
        self.expo500_btn.setObjectName(u"expo500_btn")
        sizePolicy3.setHeightForWidth(self.expo500_btn.sizePolicy().hasHeightForWidth())
        self.expo500_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.expo500_btn, 4, 0, 1, 1)

        self.exposure_label = QLabel(self.groupBox)
        self.exposure_label.setObjectName(u"exposure_label")
        sizePolicy2.setHeightForWidth(self.exposure_label.sizePolicy().hasHeightForWidth())
        self.exposure_label.setSizePolicy(sizePolicy2)
        self.exposure_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.exposure_label, 0, 1, 1, 1)

        self.expo1000_btn = QPushButton(self.groupBox)
        self.expo1000_btn.setObjectName(u"expo1000_btn")
        sizePolicy3.setHeightForWidth(self.expo1000_btn.sizePolicy().hasHeightForWidth())
        self.expo1000_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.expo1000_btn, 3, 0, 1, 1)

        self.live_btn = QPushButton(self.groupBox)
        self.live_btn.setObjectName(u"live_btn")
        sizePolicy3.setHeightForWidth(self.live_btn.sizePolicy().hasHeightForWidth())
        self.live_btn.setSizePolicy(sizePolicy3)
        self.live_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_2.addWidget(self.live_btn, 0, 0, 1, 1)

        self.live_stop_btn = QPushButton(self.groupBox)
        self.live_stop_btn.setObjectName(u"live_stop_btn")
        self.live_stop_btn.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.live_stop_btn.sizePolicy().hasHeightForWidth())
        self.live_stop_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.live_stop_btn, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setColumnStretch(0, 3)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.autorange_btn = QPushButton(self.groupBox_2)
        self.autorange_btn.setObjectName(u"autorange_btn")

        self.gridLayout_4.addWidget(self.autorange_btn, 1, 0, 1, 2)

        self.fit_chkbx = QCheckBox(self.groupBox_2)
        self.fit_chkbx.setObjectName(u"fit_chkbx")

        self.gridLayout_4.addWidget(self.fit_chkbx, 3, 1, 1, 1)

        self.integral_label = QLabel(self.groupBox_2)
        self.integral_label.setObjectName(u"integral_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.integral_label.sizePolicy().hasHeightForWidth())
        self.integral_label.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.integral_label, 4, 0, 1, 1)

        self.ROI_chkbx = QCheckBox(self.groupBox_2)
        self.ROI_chkbx.setObjectName(u"ROI_chkbx")

        self.gridLayout_4.addWidget(self.ROI_chkbx, 2, 1, 1, 1)

        self.lock_cross_chkbx = QCheckBox(self.groupBox_2)
        self.lock_cross_chkbx.setObjectName(u"lock_cross_chkbx")

        self.gridLayout_4.addWidget(self.lock_cross_chkbx, 4, 1, 1, 1)

        self.pixel_info_lbl = QLabel(self.groupBox_2)
        self.pixel_info_lbl.setObjectName(u"pixel_info_lbl")
        sizePolicy4.setHeightForWidth(self.pixel_info_lbl.sizePolicy().hasHeightForWidth())
        self.pixel_info_lbl.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.pixel_info_lbl, 2, 0, 2, 1)

        self.fit_label = QLabel(self.groupBox_2)
        self.fit_label.setObjectName(u"fit_label")
        sizePolicy4.setHeightForWidth(self.fit_label.sizePolicy().hasHeightForWidth())
        self.fit_label.setSizePolicy(sizePolicy4)
        self.fit_label.setMinimumSize(QSize(0, 80))

        self.gridLayout_4.addWidget(self.fit_label, 5, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_4.addWidget(self.pushButton_12, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4.setCheckable(False)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.shutter_connect_btn = QPushButton(self.groupBox_4)
        self.shutter_connect_btn.setObjectName(u"shutter_connect_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.shutter_connect_btn.sizePolicy().hasHeightForWidth())
        self.shutter_connect_btn.setSizePolicy(sizePolicy5)
        self.shutter_connect_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_6.addWidget(self.shutter_connect_btn, 0, 0, 1, 1)

        self.shutter_disconnect_btn = QPushButton(self.groupBox_4)
        self.shutter_disconnect_btn.setObjectName(u"shutter_disconnect_btn")
        self.shutter_disconnect_btn.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.shutter_disconnect_btn.sizePolicy().hasHeightForWidth())
        self.shutter_disconnect_btn.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.shutter_disconnect_btn, 0, 1, 1, 1)

        self.shutter_enable_btn = QPushButton(self.groupBox_4)
        self.shutter_enable_btn.setObjectName(u"shutter_enable_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.shutter_enable_btn.sizePolicy().hasHeightForWidth())
        self.shutter_enable_btn.setSizePolicy(sizePolicy6)
        self.shutter_enable_btn.setMinimumSize(QSize(117, 0))
        self.shutter_enable_btn.setMaximumSize(QSize(16777215, 117))
        self.shutter_enable_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_6.addWidget(self.shutter_enable_btn, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 5)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_4)


        self.gridLayout.addWidget(self.frame, 0, 2, 2, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setIconSize(QSize(0, 0))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.simstep_connect_btn = QPushButton(self.tab)
        self.simstep_connect_btn.setObjectName(u"simstep_connect_btn")
        self.simstep_connect_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_8.addWidget(self.simstep_connect_btn, 0, 0, 1, 1)

        self.simstep_disconnect_btn = QPushButton(self.tab)
        self.simstep_disconnect_btn.setObjectName(u"simstep_disconnect_btn")
        self.simstep_disconnect_btn.setEnabled(False)

        self.gridLayout_8.addWidget(self.simstep_disconnect_btn, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.groupBox_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_6.setFlat(True)
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setContentsMargins(8, 0, 8, 0)
        self.stop_x_btn = QPushButton(self.groupBox_6)
        self.stop_x_btn.setObjectName(u"stop_x_btn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.stop_x_btn.sizePolicy().hasHeightForWidth())
        self.stop_x_btn.setSizePolicy(sizePolicy7)
        self.stop_x_btn.setMinimumSize(QSize(1, 0))
        self.stop_x_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.gridLayout_9.addWidget(self.stop_x_btn, 0, 7, 2, 1)

        self.ref_x_btn = QPushButton(self.groupBox_6)
        self.ref_x_btn.setObjectName(u"ref_x_btn")
        sizePolicy7.setHeightForWidth(self.ref_x_btn.sizePolicy().hasHeightForWidth())
        self.ref_x_btn.setSizePolicy(sizePolicy7)
        self.ref_x_btn.setMinimumSize(QSize(1, 0))
        self.ref_x_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout_9.addWidget(self.ref_x_btn, 0, 8, 2, 1)

        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label, 0, 1, 1, 1)

        self.move_abs_x_btn = QPushButton(self.groupBox_6)
        self.move_abs_x_btn.setObjectName(u"move_abs_x_btn")
        sizePolicy7.setHeightForWidth(self.move_abs_x_btn.sizePolicy().hasHeightForWidth())
        self.move_abs_x_btn.setSizePolicy(sizePolicy7)
        self.move_abs_x_btn.setFont(font1)
        self.move_abs_x_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_9.addWidget(self.move_abs_x_btn, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy7.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy7)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_2, 0, 2, 1, 1)

        self.move_rel_x_min_h_btn = QPushButton(self.groupBox_6)
        self.move_rel_x_min_h_btn.setObjectName(u"move_rel_x_min_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_x_min_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_x_min_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_x_min_h_btn.setMinimumSize(QSize(1, 0))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setWeight(50)
        self.move_rel_x_min_h_btn.setFont(font2)
        self.move_rel_x_min_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_9.addWidget(self.move_rel_x_min_h_btn, 0, 4, 2, 1)

        self.move_rel_x_plu_h_btn = QPushButton(self.groupBox_6)
        self.move_rel_x_plu_h_btn.setObjectName(u"move_rel_x_plu_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_x_plu_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_x_plu_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_x_plu_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_x_plu_h_btn.setFont(font2)
        self.move_rel_x_plu_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_9.addWidget(self.move_rel_x_plu_h_btn, 0, 5, 2, 1)

        self.move_rel_x_plu_btn = QPushButton(self.groupBox_6)
        self.move_rel_x_plu_btn.setObjectName(u"move_rel_x_plu_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_x_plu_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_x_plu_btn.setSizePolicy(sizePolicy7)
        self.move_rel_x_plu_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_x_plu_btn.setFont(font2)
        self.move_rel_x_plu_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_9.addWidget(self.move_rel_x_plu_btn, 0, 6, 2, 1)

        self.move_rel_x_min_btn = QPushButton(self.groupBox_6)
        self.move_rel_x_min_btn.setObjectName(u"move_rel_x_min_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_x_min_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_x_min_btn.setSizePolicy(sizePolicy7)
        self.move_rel_x_min_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_x_min_btn.setMaximumSize(QSize(16777215, 16777214))
        font3 = QFont()
        font3.setPointSize(28)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.move_rel_x_min_btn.setFont(font3)
        self.move_rel_x_min_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_9.addWidget(self.move_rel_x_min_btn, 0, 3, 2, 1)

        self.pos_x_lbl = QLabel(self.groupBox_6)
        self.pos_x_lbl.setObjectName(u"pos_x_lbl")
        sizePolicy7.setHeightForWidth(self.pos_x_lbl.sizePolicy().hasHeightForWidth())
        self.pos_x_lbl.setSizePolicy(sizePolicy7)
        self.pos_x_lbl.setFont(font1)
        self.pos_x_lbl.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.pos_x_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.pos_x_lbl, 1, 1, 1, 1)

        self.rel_stp_x_entry = QLineEdit(self.groupBox_6)
        self.rel_stp_x_entry.setObjectName(u"rel_stp_x_entry")
        sizePolicy7.setHeightForWidth(self.rel_stp_x_entry.sizePolicy().hasHeightForWidth())
        self.rel_stp_x_entry.setSizePolicy(sizePolicy7)
        self.rel_stp_x_entry.setFont(font1)
        self.rel_stp_x_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.rel_stp_x_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.rel_stp_x_entry, 1, 2, 1, 1)

        self.move_abs_x_entry = QLineEdit(self.groupBox_6)
        self.move_abs_x_entry.setObjectName(u"move_abs_x_entry")
        sizePolicy7.setHeightForWidth(self.move_abs_x_entry.sizePolicy().hasHeightForWidth())
        self.move_abs_x_entry.setSizePolicy(sizePolicy7)
        self.move_abs_x_entry.setFont(font1)
        self.move_abs_x_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.move_abs_x_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.move_abs_x_entry, 1, 0, 1, 1)

        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 1)
        self.gridLayout_9.setColumnStretch(0, 5)
        self.gridLayout_9.setColumnStretch(1, 5)
        self.gridLayout_9.setColumnStretch(2, 5)
        self.gridLayout_9.setColumnStretch(3, 3)
        self.gridLayout_9.setColumnStretch(4, 3)
        self.gridLayout_9.setColumnStretch(5, 3)
        self.gridLayout_9.setColumnStretch(6, 3)
        self.gridLayout_9.setColumnStretch(7, 3)
        self.gridLayout_9.setColumnStretch(8, 3)

        self.gridLayout_8.addWidget(self.groupBox_6, 1, 0, 1, 3)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"background-color: rgb(255, 103, 123);")
        self.groupBox_7.setFlat(True)
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(8, 0, 8, 0)
        self.move_abs_y_btn = QPushButton(self.groupBox_7)
        self.move_abs_y_btn.setObjectName(u"move_abs_y_btn")
        sizePolicy7.setHeightForWidth(self.move_abs_y_btn.sizePolicy().hasHeightForWidth())
        self.move_abs_y_btn.setSizePolicy(sizePolicy7)
        self.move_abs_y_btn.setMinimumSize(QSize(1, 0))
        self.move_abs_y_btn.setFont(font1)
        self.move_abs_y_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_10.addWidget(self.move_abs_y_btn, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy7.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy7)
        self.label_5.setMinimumSize(QSize(1, 0))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setMinimumSize(QSize(1, 0))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_6, 0, 2, 1, 1)

        self.move_abs_y_entry = QLineEdit(self.groupBox_7)
        self.move_abs_y_entry.setObjectName(u"move_abs_y_entry")
        sizePolicy7.setHeightForWidth(self.move_abs_y_entry.sizePolicy().hasHeightForWidth())
        self.move_abs_y_entry.setSizePolicy(sizePolicy7)
        self.move_abs_y_entry.setMinimumSize(QSize(1, 0))
        self.move_abs_y_entry.setFont(font1)
        self.move_abs_y_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.move_abs_y_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.move_abs_y_entry, 1, 0, 1, 1)

        self.pos_y_lbl = QLabel(self.groupBox_7)
        self.pos_y_lbl.setObjectName(u"pos_y_lbl")
        sizePolicy7.setHeightForWidth(self.pos_y_lbl.sizePolicy().hasHeightForWidth())
        self.pos_y_lbl.setSizePolicy(sizePolicy7)
        self.pos_y_lbl.setMinimumSize(QSize(1, 0))
        self.pos_y_lbl.setFont(font1)
        self.pos_y_lbl.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.pos_y_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.pos_y_lbl, 1, 1, 1, 1)

        self.rel_stp_y_entry = QLineEdit(self.groupBox_7)
        self.rel_stp_y_entry.setObjectName(u"rel_stp_y_entry")
        sizePolicy7.setHeightForWidth(self.rel_stp_y_entry.sizePolicy().hasHeightForWidth())
        self.rel_stp_y_entry.setSizePolicy(sizePolicy7)
        self.rel_stp_y_entry.setMinimumSize(QSize(1, 0))
        self.rel_stp_y_entry.setFont(font1)
        self.rel_stp_y_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.rel_stp_y_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.rel_stp_y_entry, 1, 2, 1, 1)

        self.ref_y_btn = QPushButton(self.groupBox_7)
        self.ref_y_btn.setObjectName(u"ref_y_btn")
        sizePolicy7.setHeightForWidth(self.ref_y_btn.sizePolicy().hasHeightForWidth())
        self.ref_y_btn.setSizePolicy(sizePolicy7)
        self.ref_y_btn.setMinimumSize(QSize(1, 0))
        self.ref_y_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout_10.addWidget(self.ref_y_btn, 0, 8, 2, 1)

        self.stop_y_btn = QPushButton(self.groupBox_7)
        self.stop_y_btn.setObjectName(u"stop_y_btn")
        sizePolicy7.setHeightForWidth(self.stop_y_btn.sizePolicy().hasHeightForWidth())
        self.stop_y_btn.setSizePolicy(sizePolicy7)
        self.stop_y_btn.setMinimumSize(QSize(1, 0))
        self.stop_y_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.gridLayout_10.addWidget(self.stop_y_btn, 0, 7, 2, 1)

        self.move_rel_y_plu_btn = QPushButton(self.groupBox_7)
        self.move_rel_y_plu_btn.setObjectName(u"move_rel_y_plu_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_y_plu_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_y_plu_btn.setSizePolicy(sizePolicy7)
        self.move_rel_y_plu_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_y_plu_btn.setFont(font2)
        self.move_rel_y_plu_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_10.addWidget(self.move_rel_y_plu_btn, 0, 6, 2, 1)

        self.move_rel_y_plu_h_btn = QPushButton(self.groupBox_7)
        self.move_rel_y_plu_h_btn.setObjectName(u"move_rel_y_plu_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_y_plu_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_y_plu_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_y_plu_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_y_plu_h_btn.setFont(font2)
        self.move_rel_y_plu_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_10.addWidget(self.move_rel_y_plu_h_btn, 0, 5, 2, 1)

        self.move_rel_y_min_h_btn = QPushButton(self.groupBox_7)
        self.move_rel_y_min_h_btn.setObjectName(u"move_rel_y_min_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_y_min_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_y_min_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_y_min_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_y_min_h_btn.setFont(font2)
        self.move_rel_y_min_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_10.addWidget(self.move_rel_y_min_h_btn, 0, 4, 2, 1)

        self.move_rel_y_min_btn = QPushButton(self.groupBox_7)
        self.move_rel_y_min_btn.setObjectName(u"move_rel_y_min_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_y_min_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_y_min_btn.setSizePolicy(sizePolicy7)
        self.move_rel_y_min_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_y_min_btn.setFont(font2)
        self.move_rel_y_min_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_10.addWidget(self.move_rel_y_min_btn, 0, 3, 2, 1)

        self.gridLayout_10.setColumnStretch(0, 5)
        self.gridLayout_10.setColumnStretch(1, 5)
        self.gridLayout_10.setColumnStretch(2, 5)
        self.gridLayout_10.setColumnStretch(3, 3)
        self.gridLayout_10.setColumnStretch(4, 3)
        self.gridLayout_10.setColumnStretch(5, 3)
        self.gridLayout_10.setColumnStretch(6, 3)
        self.gridLayout_10.setColumnStretch(7, 3)
        self.gridLayout_10.setColumnStretch(8, 3)

        self.gridLayout_8.addWidget(self.groupBox_7, 2, 0, 1, 3)

        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setAutoFillBackground(False)
        self.groupBox_8.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.groupBox_8.setFlat(True)
        self.gridLayout_11 = QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(8, 0, 8, 0)
        self.move_abs_z_btn = QPushButton(self.groupBox_8)
        self.move_abs_z_btn.setObjectName(u"move_abs_z_btn")
        sizePolicy7.setHeightForWidth(self.move_abs_z_btn.sizePolicy().hasHeightForWidth())
        self.move_abs_z_btn.setSizePolicy(sizePolicy7)
        self.move_abs_z_btn.setMinimumSize(QSize(1, 0))
        self.move_abs_z_btn.setFont(font1)
        self.move_abs_z_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_11.addWidget(self.move_abs_z_btn, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)
        self.label_8.setMinimumSize(QSize(1, 0))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_8)
        self.label_9.setObjectName(u"label_9")
        sizePolicy7.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy7)
        self.label_9.setMinimumSize(QSize(1, 0))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_9, 0, 2, 1, 1)

        self.move_abs_z_entry = QLineEdit(self.groupBox_8)
        self.move_abs_z_entry.setObjectName(u"move_abs_z_entry")
        sizePolicy7.setHeightForWidth(self.move_abs_z_entry.sizePolicy().hasHeightForWidth())
        self.move_abs_z_entry.setSizePolicy(sizePolicy7)
        self.move_abs_z_entry.setMinimumSize(QSize(1, 0))
        self.move_abs_z_entry.setFont(font1)
        self.move_abs_z_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.move_abs_z_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.move_abs_z_entry, 1, 0, 1, 1)

        self.pos_z_lbl = QLabel(self.groupBox_8)
        self.pos_z_lbl.setObjectName(u"pos_z_lbl")
        sizePolicy7.setHeightForWidth(self.pos_z_lbl.sizePolicy().hasHeightForWidth())
        self.pos_z_lbl.setSizePolicy(sizePolicy7)
        self.pos_z_lbl.setMinimumSize(QSize(1, 0))
        self.pos_z_lbl.setFont(font1)
        self.pos_z_lbl.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.pos_z_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.pos_z_lbl, 1, 1, 1, 1)

        self.rel_stp_z_entry = QLineEdit(self.groupBox_8)
        self.rel_stp_z_entry.setObjectName(u"rel_stp_z_entry")
        sizePolicy7.setHeightForWidth(self.rel_stp_z_entry.sizePolicy().hasHeightForWidth())
        self.rel_stp_z_entry.setSizePolicy(sizePolicy7)
        self.rel_stp_z_entry.setMinimumSize(QSize(1, 0))
        self.rel_stp_z_entry.setFont(font1)
        self.rel_stp_z_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.rel_stp_z_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.rel_stp_z_entry, 1, 2, 1, 1)

        self.move_rel_z_min_btn = QPushButton(self.groupBox_8)
        self.move_rel_z_min_btn.setObjectName(u"move_rel_z_min_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_z_min_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_z_min_btn.setSizePolicy(sizePolicy7)
        self.move_rel_z_min_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_z_min_btn.setFont(font2)
        self.move_rel_z_min_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_11.addWidget(self.move_rel_z_min_btn, 0, 3, 2, 1)

        self.move_rel_z_min_h_btn = QPushButton(self.groupBox_8)
        self.move_rel_z_min_h_btn.setObjectName(u"move_rel_z_min_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_z_min_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_z_min_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_z_min_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_z_min_h_btn.setFont(font2)
        self.move_rel_z_min_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_11.addWidget(self.move_rel_z_min_h_btn, 0, 4, 2, 1)

        self.move_rel_z_plu_h_btn = QPushButton(self.groupBox_8)
        self.move_rel_z_plu_h_btn.setObjectName(u"move_rel_z_plu_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_z_plu_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_z_plu_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_z_plu_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_z_plu_h_btn.setFont(font2)
        self.move_rel_z_plu_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_11.addWidget(self.move_rel_z_plu_h_btn, 0, 5, 2, 1)

        self.move_rel_z_plu_btn = QPushButton(self.groupBox_8)
        self.move_rel_z_plu_btn.setObjectName(u"move_rel_z_plu_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_z_plu_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_z_plu_btn.setSizePolicy(sizePolicy7)
        self.move_rel_z_plu_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_z_plu_btn.setFont(font2)
        self.move_rel_z_plu_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_11.addWidget(self.move_rel_z_plu_btn, 0, 6, 2, 1)

        self.stop_z_btn = QPushButton(self.groupBox_8)
        self.stop_z_btn.setObjectName(u"stop_z_btn")
        sizePolicy7.setHeightForWidth(self.stop_z_btn.sizePolicy().hasHeightForWidth())
        self.stop_z_btn.setSizePolicy(sizePolicy7)
        self.stop_z_btn.setMinimumSize(QSize(1, 0))
        self.stop_z_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.gridLayout_11.addWidget(self.stop_z_btn, 0, 7, 2, 1)

        self.ref_z_btn = QPushButton(self.groupBox_8)
        self.ref_z_btn.setObjectName(u"ref_z_btn")
        sizePolicy7.setHeightForWidth(self.ref_z_btn.sizePolicy().hasHeightForWidth())
        self.ref_z_btn.setSizePolicy(sizePolicy7)
        self.ref_z_btn.setMinimumSize(QSize(1, 0))
        self.ref_z_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout_11.addWidget(self.ref_z_btn, 0, 8, 2, 1)

        self.gridLayout_11.setColumnStretch(0, 5)
        self.gridLayout_11.setColumnStretch(1, 5)
        self.gridLayout_11.setColumnStretch(2, 5)
        self.gridLayout_11.setColumnStretch(3, 3)
        self.gridLayout_11.setColumnStretch(4, 3)
        self.gridLayout_11.setColumnStretch(5, 3)
        self.gridLayout_11.setColumnStretch(6, 3)
        self.gridLayout_11.setColumnStretch(7, 3)
        self.gridLayout_11.setColumnStretch(8, 3)

        self.gridLayout_8.addWidget(self.groupBox_8, 3, 0, 1, 3)

        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
        self.groupBox_9.setMinimumSize(QSize(1, 0))
        self.groupBox_9.setFont(font)
        self.groupBox_9.setAutoFillBackground(False)
        self.groupBox_9.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.groupBox_9.setFlat(True)
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(8, 0, 8, 0)
        self.move_abs_th_btn = QPushButton(self.groupBox_9)
        self.move_abs_th_btn.setObjectName(u"move_abs_th_btn")
        sizePolicy7.setHeightForWidth(self.move_abs_th_btn.sizePolicy().hasHeightForWidth())
        self.move_abs_th_btn.setSizePolicy(sizePolicy7)
        self.move_abs_th_btn.setMinimumSize(QSize(1, 0))
        self.move_abs_th_btn.setFont(font1)
        self.move_abs_th_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_12.addWidget(self.move_abs_th_btn, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setMinimumSize(QSize(1, 0))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setMinimumSize(QSize(1, 0))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_12, 0, 2, 1, 1)

        self.move_abs_th_entry = QLineEdit(self.groupBox_9)
        self.move_abs_th_entry.setObjectName(u"move_abs_th_entry")
        sizePolicy7.setHeightForWidth(self.move_abs_th_entry.sizePolicy().hasHeightForWidth())
        self.move_abs_th_entry.setSizePolicy(sizePolicy7)
        self.move_abs_th_entry.setMinimumSize(QSize(1, 0))
        self.move_abs_th_entry.setFont(font1)
        self.move_abs_th_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.move_abs_th_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.move_abs_th_entry, 1, 0, 1, 1)

        self.pos_th_lbl = QLabel(self.groupBox_9)
        self.pos_th_lbl.setObjectName(u"pos_th_lbl")
        sizePolicy7.setHeightForWidth(self.pos_th_lbl.sizePolicy().hasHeightForWidth())
        self.pos_th_lbl.setSizePolicy(sizePolicy7)
        self.pos_th_lbl.setMinimumSize(QSize(1, 0))
        self.pos_th_lbl.setFont(font1)
        self.pos_th_lbl.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.pos_th_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.pos_th_lbl, 1, 1, 1, 1)

        self.rel_stp_th_entry = QLineEdit(self.groupBox_9)
        self.rel_stp_th_entry.setObjectName(u"rel_stp_th_entry")
        sizePolicy7.setHeightForWidth(self.rel_stp_th_entry.sizePolicy().hasHeightForWidth())
        self.rel_stp_th_entry.setSizePolicy(sizePolicy7)
        self.rel_stp_th_entry.setMinimumSize(QSize(1, 0))
        self.rel_stp_th_entry.setFont(font1)
        self.rel_stp_th_entry.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.rel_stp_th_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.rel_stp_th_entry, 1, 2, 1, 1)

        self.ref_th_btn = QPushButton(self.groupBox_9)
        self.ref_th_btn.setObjectName(u"ref_th_btn")
        sizePolicy7.setHeightForWidth(self.ref_th_btn.sizePolicy().hasHeightForWidth())
        self.ref_th_btn.setSizePolicy(sizePolicy7)
        self.ref_th_btn.setMinimumSize(QSize(1, 0))
        self.ref_th_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout_12.addWidget(self.ref_th_btn, 0, 8, 2, 1)

        self.stop_th_btn = QPushButton(self.groupBox_9)
        self.stop_th_btn.setObjectName(u"stop_th_btn")
        sizePolicy7.setHeightForWidth(self.stop_th_btn.sizePolicy().hasHeightForWidth())
        self.stop_th_btn.setSizePolicy(sizePolicy7)
        self.stop_th_btn.setMinimumSize(QSize(1, 0))
        self.stop_th_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.gridLayout_12.addWidget(self.stop_th_btn, 0, 7, 2, 1)

        self.move_rel_th_plu_btn = QPushButton(self.groupBox_9)
        self.move_rel_th_plu_btn.setObjectName(u"move_rel_th_plu_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_th_plu_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_th_plu_btn.setSizePolicy(sizePolicy7)
        self.move_rel_th_plu_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_th_plu_btn.setFont(font2)
        self.move_rel_th_plu_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_12.addWidget(self.move_rel_th_plu_btn, 0, 6, 2, 1)

        self.move_rel_th_plu_h_btn = QPushButton(self.groupBox_9)
        self.move_rel_th_plu_h_btn.setObjectName(u"move_rel_th_plu_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_th_plu_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_th_plu_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_th_plu_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_th_plu_h_btn.setFont(font2)
        self.move_rel_th_plu_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_12.addWidget(self.move_rel_th_plu_h_btn, 0, 5, 2, 1)

        self.move_rel_th_min_h_btn = QPushButton(self.groupBox_9)
        self.move_rel_th_min_h_btn.setObjectName(u"move_rel_th_min_h_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_th_min_h_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_th_min_h_btn.setSizePolicy(sizePolicy7)
        self.move_rel_th_min_h_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_th_min_h_btn.setFont(font2)
        self.move_rel_th_min_h_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_12.addWidget(self.move_rel_th_min_h_btn, 0, 4, 2, 1)

        self.move_rel_th_min_btn = QPushButton(self.groupBox_9)
        self.move_rel_th_min_btn.setObjectName(u"move_rel_th_min_btn")
        sizePolicy7.setHeightForWidth(self.move_rel_th_min_btn.sizePolicy().hasHeightForWidth())
        self.move_rel_th_min_btn.setSizePolicy(sizePolicy7)
        self.move_rel_th_min_btn.setMinimumSize(QSize(1, 0))
        self.move_rel_th_min_btn.setFont(font2)
        self.move_rel_th_min_btn.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout_12.addWidget(self.move_rel_th_min_btn, 0, 3, 2, 1)

        self.gridLayout_12.setColumnStretch(0, 5)
        self.gridLayout_12.setColumnStretch(1, 5)
        self.gridLayout_12.setColumnStretch(2, 5)
        self.gridLayout_12.setColumnStretch(3, 3)
        self.gridLayout_12.setColumnStretch(4, 3)
        self.gridLayout_12.setColumnStretch(5, 3)
        self.gridLayout_12.setColumnStretch(6, 3)
        self.gridLayout_12.setColumnStretch(7, 3)
        self.gridLayout_12.setColumnStretch(8, 3)

        self.gridLayout_8.addWidget(self.groupBox_9, 4, 0, 1, 3)

        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 3)
        self.gridLayout_8.setRowStretch(2, 3)
        self.gridLayout_8.setRowStretch(3, 3)
        self.gridLayout_8.setRowStretch(4, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_17 = QGridLayout(self.tab_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_11 = QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.jog_up_btn = QPushButton(self.groupBox_11)
        self.jog_up_btn.setObjectName(u"jog_up_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.jog_up_btn.sizePolicy().hasHeightForWidth())
        self.jog_up_btn.setSizePolicy(sizePolicy8)

        self.verticalLayout_5.addWidget(self.jog_up_btn)

        self.jog_down_btn = QPushButton(self.groupBox_11)
        self.jog_down_btn.setObjectName(u"jog_down_btn")
        sizePolicy8.setHeightForWidth(self.jog_down_btn.sizePolicy().hasHeightForWidth())
        self.jog_down_btn.setSizePolicy(sizePolicy8)

        self.verticalLayout_5.addWidget(self.jog_down_btn)


        self.gridLayout_17.addWidget(self.groupBox_11, 0, 3, 6, 1)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.groupBox_10)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_6.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_17.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_17)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_7.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_19)

        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.groupBox_10)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy9)
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.gridLayout_17.addWidget(self.groupBox_10, 6, 0, 1, 4)

        self.freq_entry = QLineEdit(self.tab_2)
        self.freq_entry.setObjectName(u"freq_entry")

        self.gridLayout_17.addWidget(self.freq_entry, 5, 2, 1, 1)

        self.volt_label = QLabel(self.tab_2)
        self.volt_label.setObjectName(u"volt_label")

        self.gridLayout_17.addWidget(self.volt_label, 2, 0, 1, 1)

        self.volt_entry = QLineEdit(self.tab_2)
        self.volt_entry.setObjectName(u"volt_entry")

        self.gridLayout_17.addWidget(self.volt_entry, 3, 2, 1, 1)

        self.enable_btn = QPushButton(self.tab_2)
        self.enable_btn.setObjectName(u"enable_btn")

        self.gridLayout_17.addWidget(self.enable_btn, 0, 1, 1, 1)

        self.disable_btn_2 = QPushButton(self.tab_2)
        self.disable_btn_2.setObjectName(u"disable_btn_2")

        self.gridLayout_17.addWidget(self.disable_btn_2, 0, 2, 1, 1)

        self.cap_LCD = QLCDNumber(self.tab_2)
        self.cap_LCD.setObjectName(u"cap_LCD")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.cap_LCD.sizePolicy().hasHeightForWidth())
        self.cap_LCD.setSizePolicy(sizePolicy10)
        self.cap_LCD.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.cap_LCD.setDigitCount(7)
        self.cap_LCD.setSegmentStyle(QLCDNumber.Flat)
        self.cap_LCD.setProperty("value", 0.000000000000000)

        self.gridLayout_17.addWidget(self.cap_LCD, 1, 0, 1, 1)

        self.volt_LCD = QLCDNumber(self.tab_2)
        self.volt_LCD.setObjectName(u"volt_LCD")
        sizePolicy10.setHeightForWidth(self.volt_LCD.sizePolicy().hasHeightForWidth())
        self.volt_LCD.setSizePolicy(sizePolicy10)
        self.volt_LCD.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.volt_LCD.setDigitCount(7)
        self.volt_LCD.setSegmentStyle(QLCDNumber.Flat)
        self.volt_LCD.setProperty("value", 0.000000000000000)

        self.gridLayout_17.addWidget(self.volt_LCD, 3, 0, 1, 1)

        self.set_volt_btn = QPushButton(self.tab_2)
        self.set_volt_btn.setObjectName(u"set_volt_btn")

        self.gridLayout_17.addWidget(self.set_volt_btn, 3, 1, 1, 1)

        self.freq_label = QLabel(self.tab_2)
        self.freq_label.setObjectName(u"freq_label")

        self.gridLayout_17.addWidget(self.freq_label, 4, 0, 1, 1)

        self.freq_LCD = QLCDNumber(self.tab_2)
        self.freq_LCD.setObjectName(u"freq_LCD")
        sizePolicy10.setHeightForWidth(self.freq_LCD.sizePolicy().hasHeightForWidth())
        self.freq_LCD.setSizePolicy(sizePolicy10)
        self.freq_LCD.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.freq_LCD.setDigitCount(7)
        self.freq_LCD.setSegmentStyle(QLCDNumber.Flat)
        self.freq_LCD.setProperty("value", 0.000000000000000)

        self.gridLayout_17.addWidget(self.freq_LCD, 5, 0, 1, 1)

        self.set_freq_btn = QPushButton(self.tab_2)
        self.set_freq_btn.setObjectName(u"set_freq_btn")

        self.gridLayout_17.addWidget(self.set_freq_btn, 5, 1, 1, 1)

        self.cap_btn = QPushButton(self.tab_2)
        self.cap_btn.setObjectName(u"cap_btn")

        self.gridLayout_17.addWidget(self.cap_btn, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.gridLayout_17.setColumnStretch(0, 1)
        self.gridLayout_17.setColumnStretch(1, 1)
        self.gridLayout_17.setColumnStretch(2, 1)
        self.gridLayout_17.setColumnStretch(3, 1)
        self.gridLayout_17.setRowMinimumHeight(0, 1)
        self.gridLayout_17.setRowMinimumHeight(1, 4)
        self.gridLayout_17.setRowMinimumHeight(2, 1)
        self.gridLayout_17.setRowMinimumHeight(3, 4)
        self.gridLayout_17.setRowMinimumHeight(4, 1)
        self.gridLayout_17.setRowMinimumHeight(5, 4)
        self.gridLayout_17.setRowMinimumHeight(6, 4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_58 = QGridLayout(self.tab_10)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.groupBox_32 = QGroupBox(self.tab_10)
        self.groupBox_32.setObjectName(u"groupBox_32")
        sizePolicy4.setHeightForWidth(self.groupBox_32.sizePolicy().hasHeightForWidth())
        self.groupBox_32.setSizePolicy(sizePolicy4)
        self.groupBox_32.setStyleSheet(u"background-color: rgb(255, 103, 123);")
        self.gridLayout_43 = QGridLayout(self.groupBox_32)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setVerticalSpacing(0)
        self.gridLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_33 = QGroupBox(self.groupBox_32)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.gridLayout_44 = QGridLayout(self.groupBox_33)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_6 = QComboBox(self.groupBox_33)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_44.addWidget(self.comboBox_6, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_33, 0, 0, 1, 1)

        self.groupBox_34 = QGroupBox(self.groupBox_32)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.gridLayout_45 = QGridLayout(self.groupBox_34)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_13 = QLineEdit(self.groupBox_34)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_45.addWidget(self.lineEdit_13, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_34, 0, 1, 1, 1)

        self.groupBox_35 = QGroupBox(self.groupBox_32)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.gridLayout_46 = QGridLayout(self.groupBox_35)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_14 = QLineEdit(self.groupBox_35)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_46.addWidget(self.lineEdit_14, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_35, 0, 2, 1, 1)

        self.groupBox_36 = QGroupBox(self.groupBox_32)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.gridLayout_47 = QGridLayout(self.groupBox_36)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_15 = QLineEdit(self.groupBox_36)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_47.addWidget(self.lineEdit_15, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_36, 0, 3, 1, 1)

        self.gridLayout_43.setColumnStretch(0, 1)
        self.gridLayout_43.setColumnStretch(1, 1)
        self.gridLayout_43.setColumnStretch(2, 1)
        self.gridLayout_43.setColumnStretch(3, 1)

        self.gridLayout_58.addWidget(self.groupBox_32, 1, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.tab_10)
        self.groupBox_27.setObjectName(u"groupBox_27")
        sizePolicy4.setHeightForWidth(self.groupBox_27.sizePolicy().hasHeightForWidth())
        self.groupBox_27.setSizePolicy(sizePolicy4)
        self.groupBox_27.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.gridLayout_41 = QGridLayout(self.groupBox_27)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setVerticalSpacing(0)
        self.gridLayout_41.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_28 = QGroupBox(self.groupBox_27)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.gridLayout_37 = QGridLayout(self.groupBox_28)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_5 = QComboBox(self.groupBox_28)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_37.addWidget(self.comboBox_5, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.groupBox_28, 0, 0, 1, 1)

        self.groupBox_29 = QGroupBox(self.groupBox_27)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.gridLayout_38 = QGridLayout(self.groupBox_29)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_9 = QLineEdit(self.groupBox_29)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_38.addWidget(self.lineEdit_9, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.groupBox_29, 0, 1, 1, 1)

        self.groupBox_30 = QGroupBox(self.groupBox_27)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_39 = QGridLayout(self.groupBox_30)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_10 = QLineEdit(self.groupBox_30)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAutoFillBackground(False)
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_39.addWidget(self.lineEdit_10, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.groupBox_30, 0, 2, 1, 1)

        self.groupBox_31 = QGroupBox(self.groupBox_27)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.gridLayout_40 = QGridLayout(self.groupBox_31)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_11 = QLineEdit(self.groupBox_31)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setAutoFillBackground(False)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_40.addWidget(self.lineEdit_11, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.groupBox_31, 0, 3, 1, 1)

        self.gridLayout_41.setColumnStretch(0, 1)
        self.gridLayout_41.setColumnStretch(1, 1)
        self.gridLayout_41.setColumnStretch(2, 1)
        self.gridLayout_41.setColumnStretch(3, 1)

        self.gridLayout_58.addWidget(self.groupBox_27, 0, 0, 1, 1)

        self.groupBox_37 = QGroupBox(self.tab_10)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy4.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy4)
        self.groupBox_37.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.gridLayout_48 = QGridLayout(self.groupBox_37)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setVerticalSpacing(0)
        self.gridLayout_48.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_38 = QGroupBox(self.groupBox_37)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.gridLayout_49 = QGridLayout(self.groupBox_38)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_7 = QComboBox(self.groupBox_38)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_49.addWidget(self.comboBox_7, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_38, 0, 0, 1, 1)

        self.groupBox_39 = QGroupBox(self.groupBox_37)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.gridLayout_50 = QGridLayout(self.groupBox_39)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_17 = QLineEdit(self.groupBox_39)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_50.addWidget(self.lineEdit_17, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_39, 0, 1, 1, 1)

        self.groupBox_40 = QGroupBox(self.groupBox_37)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.gridLayout_51 = QGridLayout(self.groupBox_40)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_18 = QLineEdit(self.groupBox_40)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_51.addWidget(self.lineEdit_18, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_40, 0, 2, 1, 1)

        self.groupBox_41 = QGroupBox(self.groupBox_37)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.gridLayout_52 = QGridLayout(self.groupBox_41)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_19 = QLineEdit(self.groupBox_41)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_52.addWidget(self.lineEdit_19, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_41, 0, 3, 1, 1)

        self.gridLayout_48.setColumnStretch(0, 1)
        self.gridLayout_48.setColumnStretch(1, 1)
        self.gridLayout_48.setColumnStretch(2, 1)
        self.gridLayout_48.setColumnStretch(3, 1)

        self.gridLayout_58.addWidget(self.groupBox_37, 2, 0, 1, 1)

        self.groupBox_42 = QGroupBox(self.tab_10)
        self.groupBox_42.setObjectName(u"groupBox_42")
        sizePolicy4.setHeightForWidth(self.groupBox_42.sizePolicy().hasHeightForWidth())
        self.groupBox_42.setSizePolicy(sizePolicy4)
        self.groupBox_42.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.gridLayout_53 = QGridLayout(self.groupBox_42)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setVerticalSpacing(0)
        self.gridLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_43 = QGroupBox(self.groupBox_42)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.gridLayout_54 = QGridLayout(self.groupBox_43)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_8 = QComboBox(self.groupBox_43)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_54.addWidget(self.comboBox_8, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_43, 0, 0, 1, 1)

        self.groupBox_44 = QGroupBox(self.groupBox_42)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.gridLayout_55 = QGridLayout(self.groupBox_44)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_21 = QLineEdit(self.groupBox_44)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_55.addWidget(self.lineEdit_21, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_44, 0, 1, 1, 1)

        self.groupBox_45 = QGroupBox(self.groupBox_42)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.gridLayout_56 = QGridLayout(self.groupBox_45)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_22 = QLineEdit(self.groupBox_45)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_56.addWidget(self.lineEdit_22, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_45, 0, 2, 1, 1)

        self.groupBox_46 = QGroupBox(self.groupBox_42)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.gridLayout_57 = QGridLayout(self.groupBox_46)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_23 = QLineEdit(self.groupBox_46)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.gridLayout_57.addWidget(self.lineEdit_23, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_46, 0, 3, 1, 1)

        self.gridLayout_53.setColumnStretch(0, 1)
        self.gridLayout_53.setColumnStretch(1, 1)
        self.gridLayout_53.setColumnStretch(2, 1)
        self.gridLayout_53.setColumnStretch(3, 1)

        self.gridLayout_58.addWidget(self.groupBox_42, 3, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.tab_10)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_58.addWidget(self.pushButton_10, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_42 = QGridLayout(self.tab_11)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.pushButton_7 = QPushButton(self.tab_11)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_42.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_11)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_42.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.tab_11)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_42.addWidget(self.pushButton_11, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.tab_11)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy5.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy5)
        self.checkBox.setBaseSize(QSize(0, 0))
        self.checkBox.setFont(font4)
        self.checkBox.setIconSize(QSize(30, 30))
        self.checkBox.setChecked(True)

        self.gridLayout_42.addWidget(self.checkBox, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_11, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_35 = QGridLayout(self.tab_13)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.folder_btn = QPushButton(self.tab_13)
        self.folder_btn.setObjectName(u"folder_btn")

        self.gridLayout_35.addWidget(self.folder_btn, 4, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.frame_10 = QFrame(self.tab_13)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_10)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.pushButton_6 = QPushButton(self.frame_10)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_36.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.quadro_init_btn = QPushButton(self.frame_10)
        self.quadro_init_btn.setObjectName(u"quadro_init_btn")

        self.gridLayout_36.addWidget(self.quadro_init_btn, 0, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_36.addWidget(self.pushButton_8, 0, 2, 1, 1)


        self.gridLayout_35.addWidget(self.frame_10, 7, 3, 1, 1)

        self.groupBox_18 = QGroupBox(self.tab_13)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_27 = QGridLayout(self.groupBox_18)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.comboBox_2 = QComboBox(self.groupBox_18)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_27.addWidget(self.comboBox_2, 0, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.groupBox_18)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_28 = QGridLayout(self.groupBox_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.spinBox_2 = QSpinBox(self.groupBox_20)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setValue(100)

        self.gridLayout_28.addWidget(self.spinBox_2, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.groupBox_20, 1, 0, 1, 1)


        self.gridLayout_35.addWidget(self.groupBox_18, 0, 2, 8, 1)

        self.groupBox_26 = QGroupBox(self.tab_13)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_34 = QGridLayout(self.groupBox_26)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.groupBox_14 = QGroupBox(self.groupBox_26)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_23 = QGridLayout(self.groupBox_14)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setVerticalSpacing(0)
        self.gridLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit = QLineEdit(self.groupBox_14)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_23.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_14, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_26)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_24 = QGridLayout(self.groupBox_15)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setVerticalSpacing(0)
        self.gridLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_2 = QLineEdit(self.groupBox_15)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_24.addWidget(self.lineEdit_2, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_15, 1, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_26)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_20 = QGridLayout(self.groupBox_12)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(0)
        self.gridLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.comboBox = QComboBox(self.groupBox_12)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_20.addWidget(self.comboBox, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_26)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_22 = QGridLayout(self.groupBox_13)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(0)
        self.gridLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.spinBox = QSpinBox(self.groupBox_13)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(200000)
        self.spinBox.setSingleStep(1000)
        self.spinBox.setValue(30000)

        self.gridLayout_22.addWidget(self.spinBox, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_13, 0, 1, 1, 1)

        self.groupBox_17 = QGroupBox(self.groupBox_26)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_26 = QGridLayout(self.groupBox_17)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setVerticalSpacing(0)
        self.gridLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_4 = QLineEdit(self.groupBox_17)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_26.addWidget(self.lineEdit_4, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_17, 2, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBox_26)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_25 = QGridLayout(self.groupBox_16)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(0)
        self.gridLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_3 = QLineEdit(self.groupBox_16)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_25.addWidget(self.lineEdit_3, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_16, 2, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.groupBox_26)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_21 = QGridLayout(self.groupBox_24)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setVerticalSpacing(0)
        self.gridLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_6 = QLineEdit(self.groupBox_24)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_21.addWidget(self.lineEdit_6, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_24, 3, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.groupBox_26)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.gridLayout_33 = QGridLayout(self.groupBox_25)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setVerticalSpacing(0)
        self.gridLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_7 = QLineEdit(self.groupBox_25)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_33.addWidget(self.lineEdit_7, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_25, 3, 1, 1, 1)


        self.gridLayout_35.addWidget(self.groupBox_26, 0, 0, 8, 1)

        self.groupBox_19 = QGroupBox(self.tab_13)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_29 = QGridLayout(self.groupBox_19)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.pushButton_5 = QPushButton(self.groupBox_19)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_29.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.groupBox_19)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_30 = QGridLayout(self.groupBox_21)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setVerticalSpacing(0)
        self.gridLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.quadro_namepattern_entry = QLineEdit(self.groupBox_21)
        self.quadro_namepattern_entry.setObjectName(u"quadro_namepattern_entry")

        self.gridLayout_30.addWidget(self.quadro_namepattern_entry, 0, 0, 1, 1)

        self.quadro_namenumber_entry = QLineEdit(self.groupBox_21)
        self.quadro_namenumber_entry.setObjectName(u"quadro_namenumber_entry")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.quadro_namenumber_entry.sizePolicy().hasHeightForWidth())
        self.quadro_namenumber_entry.setSizePolicy(sizePolicy11)

        self.gridLayout_30.addWidget(self.quadro_namenumber_entry, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.groupBox_22 = QGroupBox(self.groupBox_19)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_31 = QGridLayout(self.groupBox_22)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setVerticalSpacing(0)
        self.gridLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_3 = QComboBox(self.groupBox_22)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_31.addWidget(self.comboBox_3, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_22, 1, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.groupBox_19)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_32 = QGridLayout(self.groupBox_23)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_4 = QComboBox(self.groupBox_23)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_32.addWidget(self.comboBox_4, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_23, 2, 0, 1, 1)


        self.gridLayout_35.addWidget(self.groupBox_19, 0, 1, 8, 1)

        self.folder_path_entry = QLineEdit(self.tab_13)
        self.folder_path_entry.setObjectName(u"folder_path_entry")

        self.gridLayout_35.addWidget(self.folder_path_entry, 5, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_35.addItem(self.verticalSpacer_7, 2, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.tab_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.pushButton_13.setCheckable(True)

        self.gridLayout_35.addWidget(self.pushButton_13, 3, 3, 1, 1)

        self.quadro_acquire_btn = QPushButton(self.tab_13)
        self.quadro_acquire_btn.setObjectName(u"quadro_acquire_btn")
        self.quadro_acquire_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_35.addWidget(self.quadro_acquire_btn, 6, 3, 1, 1)

        self.label_30 = QLabel(self.tab_13)
        self.label_30.setObjectName(u"label_30")
        font5 = QFont()
        font5.setPointSize(16)
        self.label_30.setFont(font5)

        self.gridLayout_35.addWidget(self.label_30, 1, 3, 1, 1)

        self.gridLayout_35.setColumnStretch(0, 2)
        self.gridLayout_35.setColumnStretch(1, 1)
        self.gridLayout_35.setColumnStretch(2, 1)
        self.gridLayout_35.setColumnStretch(3, 4)
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_7 = QGridLayout(self.tab_14)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.UV_power_entry = QLineEdit(self.tab_14)
        self.UV_power_entry.setObjectName(u"UV_power_entry")

        self.gridLayout_7.addWidget(self.UV_power_entry, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(350, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.pump_power_entry = QLineEdit(self.tab_14)
        self.pump_power_entry.setObjectName(u"pump_power_entry")

        self.gridLayout_7.addWidget(self.pump_power_entry, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(350, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.pump_area_entry = QLineEdit(self.tab_14)
        self.pump_area_entry.setObjectName(u"pump_area_entry")

        self.gridLayout_7.addWidget(self.pump_area_entry, 2, 2, 1, 1)

        self.pump_power_lbl = QLabel(self.tab_14)
        self.pump_power_lbl.setObjectName(u"pump_power_lbl")

        self.gridLayout_7.addWidget(self.pump_power_lbl, 1, 0, 1, 1)

        self.pump_area_lbl = QLabel(self.tab_14)
        self.pump_area_lbl.setObjectName(u"pump_area_lbl")

        self.gridLayout_7.addWidget(self.pump_area_lbl, 2, 0, 1, 1)

        self.UV_power_lbl = QLabel(self.tab_14)
        self.UV_power_lbl.setObjectName(u"UV_power_lbl")

        self.gridLayout_7.addWidget(self.UV_power_lbl, 0, 0, 1, 1)

        self.RF_phase_lbl = QLabel(self.tab_14)
        self.RF_phase_lbl.setObjectName(u"RF_phase_lbl")

        self.gridLayout_7.addWidget(self.RF_phase_lbl, 3, 0, 1, 1)

        self.RF_power_entry = QLineEdit(self.tab_14)
        self.RF_power_entry.setObjectName(u"RF_power_entry")

        self.gridLayout_7.addWidget(self.RF_power_entry, 4, 2, 1, 1)

        self.RF_power_lbl = QLabel(self.tab_14)
        self.RF_power_lbl.setObjectName(u"RF_power_lbl")

        self.gridLayout_7.addWidget(self.RF_power_lbl, 4, 0, 1, 1)

        self.notes_btn = QPushButton(self.tab_14)
        self.notes_btn.setObjectName(u"notes_btn")

        self.gridLayout_7.addWidget(self.notes_btn, 5, 0, 1, 1)

        self.RF_phase_entry = QLineEdit(self.tab_14)
        self.RF_phase_entry.setObjectName(u"RF_phase_entry")

        self.gridLayout_7.addWidget(self.RF_phase_entry, 3, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 1, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 6, 0, 1, 1)

        self.tabWidget.addTab(self.tab_14, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.tabWidget_2 = QTabWidget(self.frame_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setMovable(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_13 = QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.Pressure_lbl = QLabel(self.tab_3)
        self.Pressure_lbl.setObjectName(u"Pressure_lbl")
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(15)
        self.Pressure_lbl.setFont(font6)
        self.Pressure_lbl.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout_13.addWidget(self.Pressure_lbl, 0, 1, 1, 1)

        self.logging_PR_rbtn = QRadioButton(self.tab_3)
        self.logging_PR_rbtn.setObjectName(u"logging_PR_rbtn")

        self.gridLayout_13.addWidget(self.logging_PR_rbtn, 2, 1, 1, 1)

        self.folder_PR_btn = QPushButton(self.tab_3)
        self.folder_PR_btn.setObjectName(u"folder_PR_btn")

        self.gridLayout_13.addWidget(self.folder_PR_btn, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.pressure_plot = PlotWidget(self.tab_3)
        self.pressure_plot.setObjectName(u"pressure_plot")

        self.gridLayout_13.addWidget(self.pressure_plot, 0, 0, 4, 1)

        self.gridLayout_13.setColumnStretch(0, 6)
        self.gridLayout_13.setColumnStretch(1, 2)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Temp_RA_lbl = QLabel(self.tab_4)
        self.Temp_RA_lbl.setObjectName(u"Temp_RA_lbl")
        font7 = QFont()
        font7.setPointSize(14)
        self.Temp_RA_lbl.setFont(font7)
        self.Temp_RA_lbl.setStyleSheet(u"background-color: rgb(254, 0, 0);")

        self.gridLayout_14.addWidget(self.Temp_RA_lbl, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_3, 8, 1, 1, 1)

        self.folder_LS_btn = QPushButton(self.tab_4)
        self.folder_LS_btn.setObjectName(u"folder_LS_btn")

        self.gridLayout_14.addWidget(self.folder_LS_btn, 5, 1, 1, 1)

        self.Temp_RB_lbl = QLabel(self.tab_4)
        self.Temp_RB_lbl.setObjectName(u"Temp_RB_lbl")
        self.Temp_RB_lbl.setFont(font7)
        self.Temp_RB_lbl.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout_14.addWidget(self.Temp_RB_lbl, 3, 1, 1, 1)

        self.Delta_T_lbl = QLabel(self.tab_4)
        self.Delta_T_lbl.setObjectName(u"Delta_T_lbl")
        self.Delta_T_lbl.setFont(font7)

        self.gridLayout_14.addWidget(self.Delta_T_lbl, 4, 1, 1, 1)

        self.TempA_lbl = QLabel(self.tab_4)
        self.TempA_lbl.setObjectName(u"TempA_lbl")
        self.TempA_lbl.setFont(font7)
        self.TempA_lbl.setStyleSheet(u"background-color: rgb(254, 0, 0);")

        self.gridLayout_14.addWidget(self.TempA_lbl, 0, 1, 1, 1)

        self.logging_LS_rbtn = QRadioButton(self.tab_4)
        self.logging_LS_rbtn.setObjectName(u"logging_LS_rbtn")

        self.gridLayout_14.addWidget(self.logging_LS_rbtn, 6, 1, 1, 1)

        self.TempB_lbl = QLabel(self.tab_4)
        self.TempB_lbl.setObjectName(u"TempB_lbl")
        self.TempB_lbl.setFont(font7)
        self.TempB_lbl.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout_14.addWidget(self.TempB_lbl, 2, 1, 1, 1)

        self.temperature_plot = PlotWidget(self.tab_4)
        self.temperature_plot.setObjectName(u"temperature_plot")

        self.gridLayout_14.addWidget(self.temperature_plot, 0, 0, 9, 1)

        self.frame_11 = QFrame(self.tab_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_11)
        self.gridLayout_59.setSpacing(0)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.TempA_chkbx = QCheckBox(self.frame_11)
        self.TempA_chkbx.setObjectName(u"TempA_chkbx")
        self.TempA_chkbx.setChecked(True)

        self.gridLayout_59.addWidget(self.TempA_chkbx, 0, 0, 1, 1)

        self.TempB_chkbx = QCheckBox(self.frame_11)
        self.TempB_chkbx.setObjectName(u"TempB_chkbx")
        self.TempB_chkbx.setChecked(True)

        self.gridLayout_59.addWidget(self.TempB_chkbx, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.frame_11, 7, 1, 1, 1)

        self.gridLayout_14.setColumnStretch(0, 12)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_60 = QGridLayout(self.tab_12)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gladz_plot = PlotWidget(self.tab_12)
        self.gladz_plot.setObjectName(u"gladz_plot")

        self.gridLayout_60.addWidget(self.gladz_plot, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_5 = QGridLayout(self.tab_15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.difference_image = ImageView(self.tab_15)
        self.difference_image.setObjectName(u"difference_image")

        self.gridLayout_5.addWidget(self.difference_image, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.tab_15)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_4)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.pushButton_14 = QPushButton(self.frame_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setCheckable(True)

        self.gridLayout_61.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_4)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_61.addWidget(self.pushButton_15, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_62 = QGridLayout(self.tab_16)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.pushButton_16 = QPushButton(self.tab_16)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy12)
        self.pushButton_16.setCheckable(True)

        self.gridLayout_62.addWidget(self.pushButton_16, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_62.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.average_plot = PlotWidget(self.tab_16)
        self.average_plot.setObjectName(u"average_plot")

        self.gridLayout_62.addWidget(self.average_plot, 0, 0, 2, 1)

        self.tabWidget_2.addTab(self.tab_16, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        self.tabWidget_3 = QTabWidget(self.frame_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setMovable(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_15 = QGridLayout(self.tab_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.LTS_loadFile_btn = QPushButton(self.tab_5)
        self.LTS_loadFile_btn.setObjectName(u"LTS_loadFile_btn")

        self.gridLayout_15.addWidget(self.LTS_loadFile_btn, 6, 6, 1, 1)

        self.LTS_moveABS_btn = QPushButton(self.tab_5)
        self.LTS_moveABS_btn.setObjectName(u"LTS_moveABS_btn")

        self.gridLayout_15.addWidget(self.LTS_moveABS_btn, 8, 0, 1, 1)

        self.LTS_status_lbl = QLabel(self.tab_5)
        self.LTS_status_lbl.setObjectName(u"LTS_status_lbl")

        self.gridLayout_15.addWidget(self.LTS_status_lbl, 0, 2, 1, 1)

        self.LTS_scanStop_btn = QPushButton(self.tab_5)
        self.LTS_scanStop_btn.setObjectName(u"LTS_scanStop_btn")

        self.gridLayout_15.addWidget(self.LTS_scanStop_btn, 8, 4, 1, 1)

        self.LTS_scanStart_btn = QPushButton(self.tab_5)
        self.LTS_scanStart_btn.setObjectName(u"LTS_scanStart_btn")

        self.gridLayout_15.addWidget(self.LTS_scanStart_btn, 8, 2, 1, 1)

        self.LTS_jogSt_entry = QLineEdit(self.tab_5)
        self.LTS_jogSt_entry.setObjectName(u"LTS_jogSt_entry")
        self.LTS_jogSt_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_jogSt_entry, 6, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_6, 0, 4, 1, 3)

        self.label_14 = QLabel(self.tab_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_14, 5, 5, 1, 1)

        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_10, 3, 5, 1, 1)

        self.label_7 = QLabel(self.tab_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_7, 2, 5, 1, 1)

        self.label_13 = QLabel(self.tab_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_13, 4, 5, 1, 1)

        self.LTS_connect_btn = QPushButton(self.tab_5)
        self.LTS_connect_btn.setObjectName(u"LTS_connect_btn")
        self.LTS_connect_btn.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_15.addWidget(self.LTS_connect_btn, 0, 0, 1, 1)

        self.LTS_moveABS_entry = QLineEdit(self.tab_5)
        self.LTS_moveABS_entry.setObjectName(u"LTS_moveABS_entry")
        self.LTS_moveABS_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_moveABS_entry, 8, 1, 1, 1)

        self.LTS_disconnect_btn = QPushButton(self.tab_5)
        self.LTS_disconnect_btn.setObjectName(u"LTS_disconnect_btn")
        self.LTS_disconnect_btn.setEnabled(False)

        self.gridLayout_15.addWidget(self.LTS_disconnect_btn, 0, 1, 1, 1)

        self.LTS_scanStep_entry = QLineEdit(self.tab_5)
        self.LTS_scanStep_entry.setObjectName(u"LTS_scanStep_entry")
        self.LTS_scanStep_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_scanStep_entry, 4, 6, 1, 1)

        self.pump_on_off_chkbx = QCheckBox(self.tab_5)
        self.pump_on_off_chkbx.setObjectName(u"pump_on_off_chkbx")

        self.gridLayout_15.addWidget(self.pump_on_off_chkbx, 8, 5, 1, 1)

        self.LTS_scanFromFile_rbtn = QRadioButton(self.tab_5)
        self.LTS_scanFromFile_rbtn.setObjectName(u"LTS_scanFromFile_rbtn")

        self.gridLayout_15.addWidget(self.LTS_scanFromFile_rbtn, 7, 6, 1, 1)

        self.end_at_loop_chkbx = QCheckBox(self.tab_5)
        self.end_at_loop_chkbx.setObjectName(u"end_at_loop_chkbx")

        self.gridLayout_15.addWidget(self.end_at_loop_chkbx, 8, 6, 1, 1)

        self.LTS_scanLoop_entry = QLineEdit(self.tab_5)
        self.LTS_scanLoop_entry.setObjectName(u"LTS_scanLoop_entry")
        self.LTS_scanLoop_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_scanLoop_entry, 5, 6, 1, 1)

        self.LTS_progressbar = QProgressBar(self.tab_5)
        self.LTS_progressbar.setObjectName(u"LTS_progressbar")
        self.LTS_progressbar.setMaximum(10000)
        self.LTS_progressbar.setValue(25)

        self.gridLayout_15.addWidget(self.LTS_progressbar, 9, 0, 1, 7)

        self.LTS_jogDw_btn = QPushButton(self.tab_5)
        self.LTS_jogDw_btn.setObjectName(u"LTS_jogDw_btn")
        sizePolicy10.setHeightForWidth(self.LTS_jogDw_btn.sizePolicy().hasHeightForWidth())
        self.LTS_jogDw_btn.setSizePolicy(sizePolicy10)
        font8 = QFont()
        font8.setPointSize(31)
        self.LTS_jogDw_btn.setFont(font8)
        self.LTS_jogDw_btn.setStyleSheet(u"color: rgb(1, 175, 161);")

        self.gridLayout_15.addWidget(self.LTS_jogDw_btn, 4, 4, 2, 1)

        self.LTS_scanStop_entry = QLineEdit(self.tab_5)
        self.LTS_scanStop_entry.setObjectName(u"LTS_scanStop_entry")
        self.LTS_scanStop_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_scanStop_entry, 3, 6, 1, 1)

        self.LTS_scanStart_entry = QLineEdit(self.tab_5)
        self.LTS_scanStart_entry.setObjectName(u"LTS_scanStart_entry")
        self.LTS_scanStart_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.LTS_scanStart_entry, 2, 6, 1, 1)

        self.LTS_jogUp_btn = QPushButton(self.tab_5)
        self.LTS_jogUp_btn.setObjectName(u"LTS_jogUp_btn")
        sizePolicy10.setHeightForWidth(self.LTS_jogUp_btn.sizePolicy().hasHeightForWidth())
        self.LTS_jogUp_btn.setSizePolicy(sizePolicy10)
        font9 = QFont()
        font9.setPointSize(27)
        self.LTS_jogUp_btn.setFont(font9)
        self.LTS_jogUp_btn.setStyleSheet(u"color: rgb(1, 175, 161);")

        self.gridLayout_15.addWidget(self.LTS_jogUp_btn, 2, 4, 2, 1)

        self.t0_btn = QPushButton(self.tab_5)
        self.t0_btn.setObjectName(u"t0_btn")
        self.t0_btn.setCheckable(True)

        self.gridLayout_15.addWidget(self.t0_btn, 7, 4, 1, 1)

        self.frame_12 = QFrame(self.tab_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rbtn_800 = QRadioButton(self.frame_12)
        self.rbtn_800.setObjectName(u"rbtn_800")
        self.rbtn_800.setChecked(True)

        self.horizontalLayout_8.addWidget(self.rbtn_800)

        self.rbtn_400 = QRadioButton(self.frame_12)
        self.rbtn_400.setObjectName(u"rbtn_400")

        self.horizontalLayout_8.addWidget(self.rbtn_400)


        self.gridLayout_15.addWidget(self.frame_12, 0, 3, 1, 1)

        self.LTS_position_lbl = QLabel(self.tab_5)
        self.LTS_position_lbl.setObjectName(u"LTS_position_lbl")
        font10 = QFont()
        font10.setPointSize(50)
        font10.setBold(False)
        font10.setWeight(50)
        self.LTS_position_lbl.setFont(font10)
        self.LTS_position_lbl.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")

        self.gridLayout_15.addWidget(self.LTS_position_lbl, 2, 0, 6, 4)

        self.gridLayout_15.setColumnStretch(0, 1)
        self.gridLayout_15.setColumnStretch(1, 1)
        self.gridLayout_15.setColumnStretch(2, 1)
        self.gridLayout_15.setColumnStretch(3, 1)
        self.gridLayout_15.setColumnStretch(4, 1)
        self.gridLayout_15.setColumnStretch(5, 1)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_19 = QGridLayout(self.tab_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.LTS_connect_btn_2 = QPushButton(self.tab_8)
        self.LTS_connect_btn_2.setObjectName(u"LTS_connect_btn_2")
        self.LTS_connect_btn_2.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_19.addWidget(self.LTS_connect_btn_2, 0, 0, 1, 1)

        self.LTS_disconnect_btn_2 = QPushButton(self.tab_8)
        self.LTS_disconnect_btn_2.setObjectName(u"LTS_disconnect_btn_2")
        self.LTS_disconnect_btn_2.setEnabled(False)

        self.gridLayout_19.addWidget(self.LTS_disconnect_btn_2, 0, 1, 1, 1)

        self.LTS_status_lbl_2 = QLabel(self.tab_8)
        self.LTS_status_lbl_2.setObjectName(u"LTS_status_lbl_2")

        self.gridLayout_19.addWidget(self.LTS_status_lbl_2, 0, 2, 1, 1)

        self.LTS_position_lbl_2 = QLabel(self.tab_8)
        self.LTS_position_lbl_2.setObjectName(u"LTS_position_lbl_2")
        self.LTS_position_lbl_2.setFont(font10)
        self.LTS_position_lbl_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")

        self.gridLayout_19.addWidget(self.LTS_position_lbl_2, 1, 0, 6, 3)

        self.LTS_jogUp_btn_2 = QPushButton(self.tab_8)
        self.LTS_jogUp_btn_2.setObjectName(u"LTS_jogUp_btn_2")
        sizePolicy10.setHeightForWidth(self.LTS_jogUp_btn_2.sizePolicy().hasHeightForWidth())
        self.LTS_jogUp_btn_2.setSizePolicy(sizePolicy10)
        self.LTS_jogUp_btn_2.setFont(font9)
        self.LTS_jogUp_btn_2.setStyleSheet(u"color: rgb(1, 175, 161);")

        self.gridLayout_19.addWidget(self.LTS_jogUp_btn_2, 1, 3, 2, 1)

        self.label_29 = QLabel(self.tab_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_29, 1, 4, 1, 1)

        self.LTS_scanStart_entry_2 = QLineEdit(self.tab_8)
        self.LTS_scanStart_entry_2.setObjectName(u"LTS_scanStart_entry_2")
        self.LTS_scanStart_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_scanStart_entry_2, 1, 5, 1, 1)

        self.label_28 = QLabel(self.tab_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_28, 2, 4, 1, 1)

        self.LTS_scanStop_entry_2 = QLineEdit(self.tab_8)
        self.LTS_scanStop_entry_2.setObjectName(u"LTS_scanStop_entry_2")
        self.LTS_scanStop_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_scanStop_entry_2, 2, 5, 1, 1)

        self.LTS_jogDw_btn_2 = QPushButton(self.tab_8)
        self.LTS_jogDw_btn_2.setObjectName(u"LTS_jogDw_btn_2")
        sizePolicy10.setHeightForWidth(self.LTS_jogDw_btn_2.sizePolicy().hasHeightForWidth())
        self.LTS_jogDw_btn_2.setSizePolicy(sizePolicy10)
        self.LTS_jogDw_btn_2.setFont(font8)
        self.LTS_jogDw_btn_2.setStyleSheet(u"color: rgb(1, 175, 161);")

        self.gridLayout_19.addWidget(self.LTS_jogDw_btn_2, 3, 3, 2, 1)

        self.label_26 = QLabel(self.tab_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_26, 3, 4, 1, 1)

        self.LTS_scanStep_entry_2 = QLineEdit(self.tab_8)
        self.LTS_scanStep_entry_2.setObjectName(u"LTS_scanStep_entry_2")
        self.LTS_scanStep_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_scanStep_entry_2, 3, 5, 1, 1)

        self.label_27 = QLabel(self.tab_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_27, 4, 4, 1, 1)

        self.LTS_scanLoop_entry_2 = QLineEdit(self.tab_8)
        self.LTS_scanLoop_entry_2.setObjectName(u"LTS_scanLoop_entry_2")
        self.LTS_scanLoop_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_scanLoop_entry_2, 4, 5, 1, 1)

        self.LTS_jogSt_entry_2 = QLineEdit(self.tab_8)
        self.LTS_jogSt_entry_2.setObjectName(u"LTS_jogSt_entry_2")
        self.LTS_jogSt_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_jogSt_entry_2, 5, 3, 1, 1)

        self.LTS_loadFile_btn_2 = QPushButton(self.tab_8)
        self.LTS_loadFile_btn_2.setObjectName(u"LTS_loadFile_btn_2")

        self.gridLayout_19.addWidget(self.LTS_loadFile_btn_2, 5, 5, 1, 1)

        self.t0_btn_2 = QPushButton(self.tab_8)
        self.t0_btn_2.setObjectName(u"t0_btn_2")
        self.t0_btn_2.setCheckable(True)

        self.gridLayout_19.addWidget(self.t0_btn_2, 6, 3, 1, 1)

        self.LTS_scanFromFile_rbtn_2 = QRadioButton(self.tab_8)
        self.LTS_scanFromFile_rbtn_2.setObjectName(u"LTS_scanFromFile_rbtn_2")

        self.gridLayout_19.addWidget(self.LTS_scanFromFile_rbtn_2, 6, 5, 1, 1)

        self.LTS_moveABS_btn_2 = QPushButton(self.tab_8)
        self.LTS_moveABS_btn_2.setObjectName(u"LTS_moveABS_btn_2")

        self.gridLayout_19.addWidget(self.LTS_moveABS_btn_2, 7, 0, 1, 1)

        self.LTS_moveABS_entry_2 = QLineEdit(self.tab_8)
        self.LTS_moveABS_entry_2.setObjectName(u"LTS_moveABS_entry_2")
        self.LTS_moveABS_entry_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.LTS_moveABS_entry_2, 7, 1, 1, 1)

        self.LTS_scanStart_btn_2 = QPushButton(self.tab_8)
        self.LTS_scanStart_btn_2.setObjectName(u"LTS_scanStart_btn_2")

        self.gridLayout_19.addWidget(self.LTS_scanStart_btn_2, 7, 2, 1, 1)

        self.LTS_scanStop_btn_2 = QPushButton(self.tab_8)
        self.LTS_scanStop_btn_2.setObjectName(u"LTS_scanStop_btn_2")

        self.gridLayout_19.addWidget(self.LTS_scanStop_btn_2, 7, 3, 1, 1)

        self.pump_on_off_chkbx_2 = QCheckBox(self.tab_8)
        self.pump_on_off_chkbx_2.setObjectName(u"pump_on_off_chkbx_2")

        self.gridLayout_19.addWidget(self.pump_on_off_chkbx_2, 7, 4, 1, 1)

        self.end_at_loop_chkbx_2 = QCheckBox(self.tab_8)
        self.end_at_loop_chkbx_2.setObjectName(u"end_at_loop_chkbx_2")

        self.gridLayout_19.addWidget(self.end_at_loop_chkbx_2, 7, 5, 1, 1)

        self.LTS_progressbar_2 = QProgressBar(self.tab_8)
        self.LTS_progressbar_2.setObjectName(u"LTS_progressbar_2")
        self.LTS_progressbar_2.setMaximum(10000)
        self.LTS_progressbar_2.setValue(25)

        self.gridLayout_19.addWidget(self.LTS_progressbar_2, 8, 0, 1, 6)

        self.horizontalSpacer_9 = QSpacerItem(340, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_9, 0, 3, 1, 3)

        self.gridLayout_19.setColumnStretch(0, 1)
        self.gridLayout_19.setColumnStretch(1, 1)
        self.gridLayout_19.setColumnStretch(2, 1)
        self.gridLayout_19.setColumnStretch(3, 1)
        self.gridLayout_19.setColumnStretch(4, 1)
        self.gridLayout_19.setColumnStretch(5, 1)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_16 = QGridLayout(self.tab_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_5 = QFrame(self.tab_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.axis_x_rbtn = QRadioButton(self.frame_5)
        self.axis_x_rbtn.setObjectName(u"axis_x_rbtn")

        self.horizontalLayout_4.addWidget(self.axis_x_rbtn)

        self.axis_y_rbtn = QRadioButton(self.frame_5)
        self.axis_y_rbtn.setObjectName(u"axis_y_rbtn")

        self.horizontalLayout_4.addWidget(self.axis_y_rbtn)

        self.axis_z_rbtn = QRadioButton(self.frame_5)
        self.axis_z_rbtn.setObjectName(u"axis_z_rbtn")

        self.horizontalLayout_4.addWidget(self.axis_z_rbtn)

        self.axis_th_rbtn = QRadioButton(self.frame_5)
        self.axis_th_rbtn.setObjectName(u"axis_th_rbtn")
        self.axis_th_rbtn.setChecked(True)

        self.horizontalLayout_4.addWidget(self.axis_th_rbtn)


        self.gridLayout_16.addWidget(self.frame_5, 0, 0, 1, 3)

        self.label_4 = QLabel(self.tab_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_16.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.tab_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_16.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_15 = QLabel(self.tab_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_16.addWidget(self.label_15, 1, 2, 1, 1)

        self.scan_stop_btn = QPushButton(self.tab_6)
        self.scan_stop_btn.setObjectName(u"scan_stop_btn")

        self.gridLayout_16.addWidget(self.scan_stop_btn, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.scan_stop_entry = QLineEdit(self.tab_6)
        self.scan_stop_entry.setObjectName(u"scan_stop_entry")

        self.gridLayout_16.addWidget(self.scan_stop_entry, 2, 1, 1, 1)

        self.scan_start_btn = QPushButton(self.tab_6)
        self.scan_start_btn.setObjectName(u"scan_start_btn")

        self.gridLayout_16.addWidget(self.scan_start_btn, 3, 0, 1, 1)

        self.scan_start_entry = QLineEdit(self.tab_6)
        self.scan_start_entry.setObjectName(u"scan_start_entry")

        self.gridLayout_16.addWidget(self.scan_start_entry, 2, 0, 1, 1)

        self.scan_step_entry = QLineEdit(self.tab_6)
        self.scan_step_entry.setObjectName(u"scan_step_entry")

        self.gridLayout_16.addWidget(self.scan_step_entry, 2, 2, 1, 1)

        self.scan_act_pos = QLabel(self.tab_6)
        self.scan_act_pos.setObjectName(u"scan_act_pos")

        self.gridLayout_16.addWidget(self.scan_act_pos, 3, 2, 1, 1)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_18 = QGridLayout(self.tab_7)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_25 = QLabel(self.tab_7)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_18.addWidget(self.label_25, 5, 0, 1, 1)

        self.label_23 = QLabel(self.tab_7)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_18.addWidget(self.label_23, 4, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.FS_loops_entry = QLineEdit(self.tab_7)
        self.FS_loops_entry.setObjectName(u"FS_loops_entry")
        self.FS_loops_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_loops_entry, 5, 1, 1, 1)

        self.FS_start_btn = QPushButton(self.tab_7)
        self.FS_start_btn.setObjectName(u"FS_start_btn")

        self.gridLayout_18.addWidget(self.FS_start_btn, 6, 0, 1, 1)

        self.FS_start_entry = QLineEdit(self.tab_7)
        self.FS_start_entry.setObjectName(u"FS_start_entry")
        self.FS_start_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_start_entry, 0, 1, 1, 1)

        self.label_20 = QLabel(self.tab_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_18.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_18.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.tab_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_18.addWidget(self.label_22, 2, 0, 1, 1)

        self.FS_stop_btn = QPushButton(self.tab_7)
        self.FS_stop_btn.setObjectName(u"FS_stop_btn")

        self.gridLayout_18.addWidget(self.FS_stop_btn, 6, 1, 1, 1)

        self.FS_speed_entry = QLineEdit(self.tab_7)
        self.FS_speed_entry.setObjectName(u"FS_speed_entry")
        self.FS_speed_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_speed_entry, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 7, 1, 1, 1)

        self.FS_time_lbl = QLabel(self.tab_7)
        self.FS_time_lbl.setObjectName(u"FS_time_lbl")
        self.FS_time_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_time_lbl, 4, 1, 1, 1)

        self.FS_stop_entry = QLineEdit(self.tab_7)
        self.FS_stop_entry.setObjectName(u"FS_stop_entry")
        self.FS_stop_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_stop_entry, 1, 1, 1, 1)

        self.label_24 = QLabel(self.tab_7)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_18.addWidget(self.label_24, 3, 0, 1, 1)

        self.FS_accel_entry = QLineEdit(self.tab_7)
        self.FS_accel_entry.setObjectName(u"FS_accel_entry")
        self.FS_accel_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.FS_accel_entry, 3, 1, 1, 1)

        self.gridLayout_18.setColumnStretch(0, 1)
        self.gridLayout_18.setColumnStretch(1, 1)
        self.gridLayout_18.setColumnStretch(2, 5)
        self.tabWidget_3.addTab(self.tab_7, "")

        self.verticalLayout_2.addWidget(self.tabWidget_3)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)

        self.gridLayout.addWidget(self.frame_2, 0, 3, 2, 1)

        self.horizontal_cross_frame = QFrame(self.centralwidget)
        self.horizontal_cross_frame.setObjectName(u"horizontal_cross_frame")
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.horizontal_cross_frame.sizePolicy().hasHeightForWidth())
        self.horizontal_cross_frame.setSizePolicy(sizePolicy13)
        self.horizontal_cross_frame.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontal_cross_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontal_cross_plot = PlotWidget(self.horizontal_cross_frame)
        self.horizontal_cross_plot.setObjectName(u"horizontal_cross_plot")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.horizontal_cross_plot.sizePolicy().hasHeightForWidth())
        self.horizontal_cross_plot.setSizePolicy(sizePolicy14)
        self.horizontal_cross_plot.setMinimumSize(QSize(150, 0))
        self.horizontal_cross_plot.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.horizontal_cross_plot)


        self.gridLayout.addWidget(self.horizontal_cross_frame, 0, 0, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 7)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1396, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDetector_Settings = QMenu(self.menubar)
        self.menuDetector_Settings.setObjectName(u"menuDetector_Settings")
        self.menuExtra = QMenu(self.menubar)
        self.menuExtra.setObjectName(u"menuExtra")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDetector_Settings.menuAction())
        self.menubar.addAction(self.menuExtra.menuAction())
        self.menuDetector_Settings.addAction(self.actionDetector)
        self.menuExtra.addAction(self.actionLeak_valve)
        self.menuExtra.addAction(self.actionSOL_Heater)

        self.retranslateUi(MainWindow)
        self.exposure_slider.valueChanged.connect(self.exposure_label.setNum)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UED Control v13", None))
        self.actionDetector.setText(QCoreApplication.translate("MainWindow", u"Detector", None))
        self.actionLeak_valve.setText(QCoreApplication.translate("MainWindow", u"Leak valve", None))
        self.actionSOL_Heater.setText(QCoreApplication.translate("MainWindow", u"SOL Heater", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Live Control", None))
        self.millis_btn.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.micros_btn.setText(QCoreApplication.translate("MainWindow", u"us", None))
        self.expo200_btn.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.live_acquire_btn.setText(QCoreApplication.translate("MainWindow", u"Cont. Acquire", None))
        self.expo500_btn.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.exposure_label.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.expo1000_btn.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.live_btn.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.live_stop_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Image Info", None))
        self.autorange_btn.setText(QCoreApplication.translate("MainWindow", u"Autorange", None))
        self.fit_chkbx.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.integral_label.setText("")
        self.ROI_chkbx.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.lock_cross_chkbx.setText(QCoreApplication.translate("MainWindow", u"Lock cross", None))
        self.pixel_info_lbl.setText("")
        self.fit_label.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Difference", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Shutter control", None))
        self.shutter_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.shutter_disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.shutter_enable_btn.setText("")
        self.simstep_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.simstep_disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"X Axis", None))
        self.stop_x_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.ref_x_btn.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Act. Pos.", None))
        self.move_abs_x_btn.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rel. Stp.", None))
        self.move_rel_x_min_h_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc18", None))
        self.move_rel_x_plu_h_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc1a", None))
        self.move_rel_x_plu_btn.setText(QCoreApplication.translate("MainWindow", u"\u2bee", None))
        self.move_rel_x_min_btn.setText(QCoreApplication.translate("MainWindow", u" \u2bec ", None))
        self.pos_x_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rel_stp_x_entry.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.move_abs_x_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Y Axis", None))
        self.move_abs_y_btn.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Act. Pos.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rel. Stp.", None))
        self.move_abs_y_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pos_y_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rel_stp_y_entry.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.ref_y_btn.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.stop_y_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.move_rel_y_plu_btn.setText(QCoreApplication.translate("MainWindow", u" \u2a00 ", None))
        self.move_rel_y_plu_h_btn.setText(QCoreApplication.translate("MainWindow", u" \u2299 ", None))
        self.move_rel_y_min_h_btn.setText(QCoreApplication.translate("MainWindow", u" \u2297 ", None))
        self.move_rel_y_min_btn.setText(QCoreApplication.translate("MainWindow", u" \u2a02 ", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Z Axis", None))
        self.move_abs_z_btn.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Act. Pos.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rel. Stp.", None))
        self.move_abs_z_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pos_z_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rel_stp_z_entry.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.move_rel_z_min_btn.setText(QCoreApplication.translate("MainWindow", u" \u2bed ", None))
        self.move_rel_z_min_h_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc19", None))
        self.move_rel_z_plu_h_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc1b", None))
        self.move_rel_z_plu_btn.setText(QCoreApplication.translate("MainWindow", u"\u2bef", None))
        self.stop_z_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.ref_z_btn.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u03b8 Axis", None))
        self.move_abs_th_btn.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Act. Pos.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Rel. Stp.", None))
        self.move_abs_th_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pos_th_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rel_stp_th_entry.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.ref_th_btn.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.stop_th_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.move_rel_th_plu_btn.setText(QCoreApplication.translate("MainWindow", u"\u2b6e", None))
        self.move_rel_th_plu_h_btn.setText(QCoreApplication.translate("MainWindow", u"\u21bb", None))
        self.move_rel_th_min_h_btn.setText(QCoreApplication.translate("MainWindow", u" \u21ba ", None))
        self.move_rel_th_min_btn.setText(QCoreApplication.translate("MainWindow", u" \u2b6f ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Manipulator controls", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.jog_up_btn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.jog_down_btn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Encoder", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"RAW:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"1.0000", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Deg:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"180.00", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.freq_entry.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.volt_label.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.volt_entry.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.enable_btn.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.disable_btn_2.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.set_volt_btn.setText(QCoreApplication.translate("MainWindow", u"Set Voltage", None))
        self.freq_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.set_freq_btn.setText(QCoreApplication.translate("MainWindow", u"Set Frequency", None))
        self.cap_btn.setText(QCoreApplication.translate("MainWindow", u"Get Cap.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Attocube controls", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"SRS delay box", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"Channel 1B", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"TRIG", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"TRIG AND GATE", None))

        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Divider", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"Width", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"10e-6", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Channel 1A", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"TRIG AND GATE", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"TRIG", None))

        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Divider", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"12e-6", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Width", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"9e-6", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"Channel 1C", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"TRIG", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"TRIG AND GATE", None))

        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"Divider", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"Width", None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"4.5", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"Channel 1D", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"TRIG", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"TRIG AND GATE", None))

        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"Divider", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_46.setTitle(QCoreApplication.translate("MainWindow", u"Width", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"1e-6", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Main trigger box", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Acquire", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Use in scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Gladz-PD settings", None))
        self.folder_btn.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.quadro_init_btn.setText(QCoreApplication.translate("MainWindow", u"Initialize", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Disarm", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Disabled", None))

        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Buffer size", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Detector", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"N trigger", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"N images", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Trigger", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"EXTG", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"INTS", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"INTE", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"EXTS", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"EXTE", None))

        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Incident energy", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"N of total triggers", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"N images per file", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Count time", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Frame time", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Filewriter", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Name pattern", None))
        self.quadro_namepattern_entry.setText(QCoreApplication.translate("MainWindow", u"data_", None))
        self.quadro_namenumber_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Disabled", None))

        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"CntRate corr.", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"False", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"True", None))

        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Live EXTG", None))
        self.quadro_acquire_btn.setText(QCoreApplication.translate("MainWindow", u"Acquire", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Run number: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"QUADRO settings", None))
        self.UV_power_entry.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.pump_power_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pump_area_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pump_power_lbl.setText(QCoreApplication.translate("MainWindow", u"Pump Power [mW]", None))
        self.pump_area_lbl.setText(QCoreApplication.translate("MainWindow", u"Pump area [cm\u00b2]", None))
        self.UV_power_lbl.setText(QCoreApplication.translate("MainWindow", u"UV Power [mW]", None))
        self.RF_phase_lbl.setText(QCoreApplication.translate("MainWindow", u"RF Cavity Phase", None))
        self.RF_power_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RF_power_lbl.setText(QCoreApplication.translate("MainWindow", u"RF Cavity Power [W]", None))
        self.notes_btn.setText(QCoreApplication.translate("MainWindow", u"Notes ...", None))
        self.RF_phase_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Other parameters", None))
        self.Pressure_lbl.setText(QCoreApplication.translate("MainWindow", u"P = 1.31e-08", None))
        self.logging_PR_rbtn.setText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.folder_PR_btn.setText(QCoreApplication.translate("MainWindow", u"Folder ...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.Temp_RA_lbl.setText(QCoreApplication.translate("MainWindow", u"Rate A: 0K/min", None))
        self.folder_LS_btn.setText(QCoreApplication.translate("MainWindow", u"Folder ...", None))
        self.Temp_RB_lbl.setText(QCoreApplication.translate("MainWindow", u"Rate B: 0K/min", None))
        self.Delta_T_lbl.setText(QCoreApplication.translate("MainWindow", u"Delta T:", None))
        self.TempA_lbl.setText(QCoreApplication.translate("MainWindow", u"T A:300.42K", None))
        self.logging_LS_rbtn.setText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.TempB_lbl.setText(QCoreApplication.translate("MainWindow", u"T B:", None))
        self.TempA_chkbx.setText(QCoreApplication.translate("MainWindow", u"Temp A", None))
        self.TempB_chkbx.setText(QCoreApplication.translate("MainWindow", u"Temp B", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Temperaure", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Gladz-PD output", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Difference ON-OFF", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Autoscale", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Difference", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Diff", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Average PP", None))
        self.LTS_loadFile_btn.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.LTS_moveABS_btn.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.LTS_status_lbl.setText(QCoreApplication.translate("MainWindow", u"Idle", None))
        self.LTS_scanStop_btn.setText(QCoreApplication.translate("MainWindow", u"scan STOP", None))
        self.LTS_scanStart_btn.setText(QCoreApplication.translate("MainWindow", u"scan START", None))
        self.LTS_jogSt_entry.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Loops", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.LTS_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.LTS_moveABS_entry.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.LTS_disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.LTS_scanStep_entry.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pump_on_off_chkbx.setText(QCoreApplication.translate("MainWindow", u"ON-OFF", None))
        self.LTS_scanFromFile_rbtn.setText(QCoreApplication.translate("MainWindow", u"From File", None))
        self.end_at_loop_chkbx.setText(QCoreApplication.translate("MainWindow", u"End at loop", None))
        self.LTS_scanLoop_entry.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.LTS_progressbar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.LTS_jogDw_btn.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.LTS_scanStop_entry.setText(QCoreApplication.translate("MainWindow", u"65", None))
        self.LTS_scanStart_entry.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.LTS_jogUp_btn.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.t0_btn.setText(QCoreApplication.translate("MainWindow", u"T0", None))
        self.rbtn_800.setText(QCoreApplication.translate("MainWindow", u"800 nm", None))
        self.rbtn_400.setText(QCoreApplication.translate("MainWindow", u"400 nm", None))
        self.LTS_position_lbl.setText(QCoreApplication.translate("MainWindow", u"+123.4567\n"
"+1723.56", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"LTS_1 control", None))
        self.LTS_connect_btn_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.LTS_disconnect_btn_2.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.LTS_status_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Idle", None))
        self.LTS_position_lbl_2.setText(QCoreApplication.translate("MainWindow", u"+123.4567\n"
"+1723.56", None))
        self.LTS_jogUp_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.LTS_scanStart_entry_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.LTS_scanStop_entry_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.LTS_jogDw_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.LTS_scanStep_entry_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Loops", None))
        self.LTS_scanLoop_entry_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.LTS_jogSt_entry_2.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.LTS_loadFile_btn_2.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.t0_btn_2.setText(QCoreApplication.translate("MainWindow", u"T0", None))
        self.LTS_scanFromFile_rbtn_2.setText(QCoreApplication.translate("MainWindow", u"From File", None))
        self.LTS_moveABS_btn_2.setText(QCoreApplication.translate("MainWindow", u"Move ABS", None))
        self.LTS_moveABS_entry_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.LTS_scanStart_btn_2.setText(QCoreApplication.translate("MainWindow", u"scan START", None))
        self.LTS_scanStop_btn_2.setText(QCoreApplication.translate("MainWindow", u"scan STOP", None))
        self.pump_on_off_chkbx_2.setText(QCoreApplication.translate("MainWindow", u"ON-OFF", None))
        self.end_at_loop_chkbx_2.setText(QCoreApplication.translate("MainWindow", u"End at loop", None))
        self.LTS_progressbar_2.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"LTS_2 control", None))
        self.axis_x_rbtn.setText(QCoreApplication.translate("MainWindow", u"X Axis", None))
        self.axis_y_rbtn.setText(QCoreApplication.translate("MainWindow", u"Y Axis", None))
        self.axis_z_rbtn.setText(QCoreApplication.translate("MainWindow", u"Z Axis", None))
        self.axis_th_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u03b8 Axis", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.scan_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Scan STOP", None))
        self.scan_stop_entry.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.scan_start_btn.setText(QCoreApplication.translate("MainWindow", u"Scan START", None))
        self.scan_start_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scan_step_entry.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.scan_act_pos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"XYZT scan control", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Loops", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.FS_loops_entry.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.FS_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.FS_start_entry.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Stop ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.FS_stop_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.FS_speed_entry.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.FS_time_lbl.setText(QCoreApplication.translate("MainWindow", u"00000", None))
        self.FS_stop_entry.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None))
        self.FS_accel_entry.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Fast scan", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDetector_Settings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuExtra.setTitle(QCoreApplication.translate("MainWindow", u"Extra", None))
    # retranslateUi

