# import pyautogui
# import pyscreenshot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
from scipy import signal
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import pyqtgraph.exporters
from matplotlib.animation import FuncAnimation
import sys
import shutil
import os
import csv
import datetime
import numpy as np
import pandas as pd
import pyqtgraph.exporters
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from PyQt5 import QtCore, QtWidgets
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
import sys
import shutil
import os
import csv
import datetime
import numpy as np
import pandas as pd
import pyqtgraph.exporters
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
from scipy import signal
import matplotlib.pyplot as plt
import pyqtgraph.exporters
from matplotlib.animation import FuncAnimation
# import pyautogui ##to be able to take screen
# import pyscreenshot as ImageGrab
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red,black
from PIL import Image
from reportlab.lib import colors
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle, Indenter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

from typing import List, Tuple
import os.path

import scipy.signal

from GUI12 import Ui_MainWindow, MyMplCanvas


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.pens = [pg.mkPen('r'), pg.mkPen('g'), pg.mkPen('b')]

        self.timer_1 = QtCore.QTimer()
        self.timer_2 = QtCore.QTimer()
        self.timer_3 = QtCore.QTimer()
        self.Timers = [self.timer_1, self.timer_2, self.timer_3]

        self.GraphicsView = [self.ui.graphicsView_1, self.ui.graphicsView_2, self.ui.graphicsView_3]
        self.Spec = [self.ui.Spec_1, self.ui.Spec_2, self.ui.Spec_3]
        self.Canvas = [self.ui.canvas_1, self.ui.canvas_2, self.ui.canvas_3]
        self.Layout = [self.ui.gridLayout, self.ui.gridLayout_2, self.ui.gridLayout_3]
        self.ColorPalette = [self.ui.comboBox_ColorPalette_1, self.ui.comboBox_ColorPalette_2, self.ui.comboBox_ColorPalette_3]
        self.SpeedSlider = [self.ui.speedSlider_1, self.ui.speedSlider_2, self.ui.speedSlider_3]
        self.ComboBoxColor = [self.ui.comboBoxColor_1, self.ui.comboBoxColor_2, self.ui.comboBoxColor_3]
        self.Hide = [self.ui.hide_1, self.ui.hide_2, self.ui.hide_3]
        self.HorizontalSliders = [self.ui.horizontalSlider_1, self.ui.horizontalSlider_2, self.ui.horizontalSlider_3]
        self.VerticalSliders = [self.ui.verticalSlider_1, self.ui.verticalSlider_2, self.ui.verticalSlider_3]



        ##updae spec
        self.SpecvMaxSlider = [self.ui.SpecVMaxSlider_1, self.ui.SpecVMaxSlider_2, self.ui.SpecVMaxSlider_3]
        self.SpecvMinSlider = [self.ui.SpecVMinSlider_1, self.ui.SpecVMinSlider_2, self.ui.SpecVMinSlider_3]



        self.TabWidgets = [self.ui.tab_1, self.ui.tab_2, self.ui.tab_3]
        self.TabWidgets_Spec = [self.ui.tabSpec_1, self.ui.tabSpec_2, self.ui.tabSpec_3]





        self.amplitude = [[], [], []]
        self.time = [[], [], []]
        self.data = [[], [], []]
        self.data_line = [[], [], []]
        self.idx = [[], [], []]
        self.timeUpd = [[], [], []]
        self.amplitudeUpd = [[], [], []]
        self.pdf_check = [[], [], []]



        self.channel1 = 0
        self.channel2 = 1
        self.channel3 = 2

        ####lines resposible for getting any clicked button and operate function
        self.ui.open_1.clicked.connect(lambda: self.check_open_1(self.channel1))
        self.ui.open_2.clicked.connect(lambda: self.check_open_1(self.channel2))
        self.ui.open_3.clicked.connect(lambda: self.check_open_1(self.channel3))

        self.ui.play_1.clicked.connect(lambda: self.check_play_1(self.channel1))
        self.ui.play_2.clicked.connect(lambda: self.check_play_1(self.channel2))
        self.ui.play_3.clicked.connect(lambda: self.check_play_1(self.channel3))

        self.ui.comboBoxColor_1.currentIndexChanged.connect(lambda: self.graphColor(self.channel1))
        self.ui.comboBoxColor_2.currentIndexChanged.connect(lambda: self.graphColor(self.channel2))
        self.ui.comboBoxColor_3.currentIndexChanged.connect(lambda: self.graphColor(self.channel3))

        self.ui.comboBox_ColorPalette_1.currentIndexChanged.connect(lambda: self.plotspec(self.channel1))
        self.ui.comboBox_ColorPalette_2.currentIndexChanged.connect(lambda: self.plotspec(self.channel2))
        self.ui.comboBox_ColorPalette_3.currentIndexChanged.connect(lambda: self.plotspec(self.channel3))

        self.ui.pause_1.clicked.connect(lambda: self.check_pause_1(self.channel1))
        self.ui.pause_2.clicked.connect(lambda: self.check_pause_1(self.channel2))
        self.ui.pause_3.clicked.connect(lambda: self.check_pause_1(self.channel3))

        self.ui.zoom_in_1.clicked.connect(lambda: self.check_zoom_in_1(self.channel1))
        self.ui.zoom_in_2.clicked.connect(lambda: self.check_zoom_in_1(self.channel2))
        self.ui.zoom_in_3.clicked.connect(lambda: self.check_zoom_in_1(self.channel3))

        self.ui.zoom_out_1.clicked.connect(lambda: self.check_zoom_out_1(self.channel1))
        self.ui.zoom_out_2.clicked.connect(lambda: self.check_zoom_out_1(self.channel2))
        self.ui.zoom_out_3.clicked.connect(lambda: self.check_zoom_out_1(self.channel3))

        self.ui.actionChannel_1.triggered.connect(lambda: self.check_open_1(self.channel1))
        self.ui.actionChannel_2.triggered.connect(lambda: self.check_open_1(self.channel2))
        self.ui.actionChannel_3.triggered.connect(lambda: self.check_open_1(self.channel3))

        self.ui.hide_1.stateChanged.connect(lambda: self.hidefun_1(self.channel1))
        self.ui.hide_2.stateChanged.connect(lambda: self.hidefun_1(self.channel2))
        self.ui.hide_3.stateChanged.connect(lambda: self.hidefun_1(self.channel3))


        self.ui.actionGenerate_PDF.triggered.connect(lambda: self.GenPdf())
        self.ui.actionExit.triggered.connect(lambda: self.close())

        ##update spec
        self.ui.SpecVMaxSlider_1.valueChanged[int].connect(lambda: self.updateSpec(self.channel1))
        self.ui.SpecVMinSlider_1.valueChanged[int].connect(lambda: self.updateSpec(self.channel1))

        self.ui.SpecVMaxSlider_2.valueChanged[int].connect(lambda: self.updateSpec(self.channel2))
        self.ui.SpecVMinSlider_2.valueChanged[int].connect(lambda: self.updateSpec(self.channel2))

        self.ui.SpecVMaxSlider_3.valueChanged[int].connect(lambda: self.updateSpec(self.channel3))
        self.ui.SpecVMinSlider_3.valueChanged[int].connect(lambda: self.updateSpec(self.channel3))






        self.ui.horizontalSlider_1.valueChanged[int].connect(lambda: self.Hscroll_1(self.channel1))
        self.ui.verticalSlider_1.valueChanged[int].connect(lambda: self.Vscroll_1(self.channel1))
        self.ui.horizontalSlider_2.valueChanged[int].connect(lambda: self.Hscroll_1(self.channel2))
        self.ui.verticalSlider_2.valueChanged[int].connect(lambda: self.Vscroll_1(self.channel2))
        self.ui.horizontalSlider_3.valueChanged[int].connect(lambda: self.Hscroll_1(self.channel3))
        self.ui.verticalSlider_3.valueChanged[int].connect(lambda: self.Vscroll_1(self.channel3))



    def check_open_1(self, channel: int) -> None:
        path = QFileDialog.getOpenFileName()[0]
        filename = os.path.basename(path)
        firstname = os.path.splitext(filename)[0]
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.TabWidgets[channel]), firstname)
        self.ui.tabWidget_2.setTabText(self.ui.tabWidget_2.indexOf(self.TabWidgets_Spec[channel]), firstname)


        self.data[channel] = np.genfromtxt(path, delimiter=',')
        self.GraphicsView[channel].clear()
        self.time[channel] = list(self.data[channel][:, 0])
        self.amplitude[channel] = list(self.data[channel][:, 1])

        self.data_line[channel] = self.GraphicsView[channel].plot(
            self.time[channel], self.amplitude[channel], pen=self.pens[self.ComboBoxColor[channel].currentIndex()])

        self.GraphicsView[channel].plotItem.setLimits(
            xMin=min(self.time[channel]), xMax=max(self.time[channel]), yMin=min(self.amplitude[channel]),
            yMax=max(self.amplitude[channel]))

        self.idx[channel] = 0
        self.Timers[channel].setInterval(50)
        self.Timers[channel].timeout.connect(lambda: self.update_plot_data_1(channel))
        self.Timers[channel].start()
        self.plotspec(channel)
        self.pdf_check[channel] = 1

    def update_plot_data_1(self, channel: int) -> None:
        self.timeUpd[channel] = self.time[channel][:self.idx[channel]]
        self.amplitudeUpd[channel] = self.amplitude[channel][:self.idx[channel]]
        self.idx[channel] += self.SpeedSlider[channel].value()

        # shrink range of x-axis
        self.GraphicsView[channel].plotItem.setXRange(
            max(self.timeUpd[channel], default=0) - 1,
            max(self.timeUpd[channel], default=0))  # -1 related to distance compression or expansion of signal
        # Plot the new data
        self.data_line[channel].setData(self.timeUpd[channel], self.amplitudeUpd[channel])

    def check_play_1(self, channel: int) -> None:
        self.Timers[channel].start()
        self.GraphicsView[channel].plotItem.setLimits(
            xMin=min(self.time[channel]), xMax=max(self.time[channel]), yMin=min(self.amplitude[channel]),
            yMax=max(self.amplitude[channel]))

    def graphColor(self, channel : int) -> None:
        self.data_line[channel] = self.GraphicsView[channel].plot(
             pen=self.pens[self.ComboBoxColor[channel].currentIndex()])

    ####for button responsile for pause signal
    def check_pause_1(self, channel: int) -> None:
        self.Timers[channel].stop()
        self.GraphicsView[channel].plotItem.setLimits(
            xMax=self.time[channel][self.idx[channel]])


    def check_zoom_in_1(self, channel: int) -> None:
        self.GraphicsView[channel].plotItem.getViewBox().scaleBy((0.75, 0.75))

    ####for button responsile for zoom_out signal
    def check_zoom_out_1(self, channel: int) -> None:
        self.GraphicsView[channel].plotItem.getViewBox().scaleBy((1.25, 1.25))

    def hidefun_1(self, channel: int) -> None:
        if self.Hide[channel].isChecked() == True:
            self.GraphicsView[channel].clear()
        else:
            self.data_line[channel] = self.GraphicsView[channel].plot(
                self.time[channel], self.amplitude[channel], pen=self.pens[self.ComboBoxColor[channel].currentIndex()])

    def Hscroll_1(self, channel: int) -> None:
        self.check_pause_1(channel)
        step = self.time[channel][self.idx[channel]] / 10
        var = self.HorizontalSliders[channel].value() * step
        self.GraphicsView[channel].plotItem.setXRange(
            var - step, var)

    def Vscroll_1(self, channel: int) -> None:
        self.check_pause_1(channel)
        step = (max(self.amplitude[channel][:self.idx[channel]]) - min(
            self.amplitude[channel][:self.idx[channel]])) / 10
        var = self.VerticalSliders[channel].value() * step
        self.GraphicsView[channel].plotItem.setYRange(
            var, var + step)

    def plotspec(self, channel: int) -> None:
        self.Layout[channel].removeWidget(self.Canvas[channel])
        self.Canvas[channel] = MyMplCanvas(self.Spec[channel], width=2, height=2, dpi=100)
        self.Layout[channel].addWidget(self.Canvas[channel])

        spec, freqs, t, im = self.Canvas[channel].axes.specgram(self.amplitude[channel],
                                                         cmap=self.ui.palette[self.ColorPalette[channel].currentIndex()])

        self.Canvas[channel].figure.colorbar(im).set_label('Intensity [dB]')
        self.Canvas[channel].draw()

    def updateSpec(self, channel: int) -> None:
        self.Layout[channel].removeWidget(self.Canvas[channel])
        self.Canvas[channel] = MyMplCanvas(self.Spec[channel], width=2, height=2, dpi=100)
        self.Layout[channel].addWidget(self.Canvas[channel])

        spec, freqs, t, im = self.Canvas[channel].axes.specgram(self.amplitude[channel],
                                                                cmap=self.ui.palette[
                                                                    self.ColorPalette[channel].currentIndex()],vmax= self.SpecvMaxSlider[channel].value(),vmin= self.SpecvMinSlider[channel].value())

        self.Canvas[channel].figure.colorbar(im).set_label('Intensity [dB]')
        self.Canvas[channel].draw()


    def GenPdf(self):
        screen = QApplication.primaryScreen()
        widget = QWidget()
        self.now = datetime.now()
        self.current_time = self.now.strftime("SBME_REPORT_%Y-%m-%d_%H_%M_%S.pdf")
        self.document = SimpleDocTemplate(self.current_time, pagesize=LETTER)
        self.sequnce_of_display_data = []
        self.styles = getSampleStyleSheet()
        self.image_left = "logo_2.png"
        self.image_right = "logo_3.png"
        self.img_L_Edit = Image(self.image_left, 2 * inch, 1.6 * inch)
        self.img_R_Edit = Image(self.image_right, 1.8 * inch, 1.3 * inch)
        # self.style = getSampleStyleSheet()
        headline_style = self.styles["Heading2"]

        # Data to be stored on table
        self.data_first_line = [
            [self.img_L_Edit, Paragraph("Biological Signal Report", headline_style), self.img_R_Edit]
        ]
        # Creating the table with 6 rows
        self.table = Table(self.data_first_line, 3 * [2.7 * inch], 1 * [.7 * inch])
        # setting up style and alignments of borders and grids
        self.table.setStyle(
            TableStyle(
                [
                    ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
                ]
            )
        )
        self.sequnce_of_display_data.append(self.table)

        if (self.pdf_check[0]):
            self.data_second_line = [
                [Paragraph("Signal of Channel 1", headline_style), "", ""]
            ]
            self.place_second_line = Table(self.data_second_line, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line)

            self.picture_for_signal_1 = screen.grabWindow(self.GraphicsView[0].winId())
            self.picture_for_signal_1.save(
                r'D:\College\pdfs\signal_channel_1.png')
            self.image_signal_channel_1 = "D:\College\pdfs\signal_channel_1.png"
            self.Edit_image_signal_channel_1 = Image(self.image_signal_channel_1, 6 * inch, 1.7 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_signal_channel_1)

            self.data_second_line_spec = [
                [Paragraph("spectro of Channel 1", headline_style), "", ""]
            ]
            self.place_second_line_spec = Table(self.data_second_line_spec, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_spec)
            # self.ui.tabWidget_2.setCurrentIndex(0)
            self.picture_for_spec_1 = screen.grabWindow(self.Canvas[0].winId())
            self.picture_for_spec_1.save(
                r'D:\College\pdfs\spec_channel_1.png')
            self.image_spec_channel_1 = "D:\College\pdfs\spec_channel_1.png"
            self.Edit_image_spec_channel_1 = Image(self.image_spec_channel_1, 6 * inch, 1.8 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_spec_channel_1)

            self.data_second_line_Datastatistics = [
                [Paragraph("Data of Channel 1", headline_style), "", ""]
            ]
            self.place_second_line_Datastatistics = Table(self.data_second_line_Datastatistics, 1 * [2.4 * inch],
                                                          1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_Datastatistics)

            self.data_for_fist_table = [
                ["Mean", str(np.mean(self.amplitudeUpd[0]))],
                ["STD", str(np.std(self.amplitudeUpd[0]))],
                ["Duration", self.timeUpd[0][len(self.timeUpd[0]) - 1]],
                ["min Value", np.min(self.amplitudeUpd[0])],
                ["Max Value", np.max(self.amplitudeUpd[0])],
            ]
            self.table_1 = Table(self.data_for_fist_table, 3 * [3.0 * inch], 5 * [0.5 * inch])
            self.table_1.setStyle(
                TableStyle(
                    [
                        ("INNERGRID", (0, 0), (-1, -1), 2, black),
                        ("BOX", (0, 0), (-1, -1), 2, black),
                        ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (0, -1), 12)
                    ]
                )
            )
            self.sequnce_of_display_data.append(self.table_1)
        if (self.pdf_check[1]):
            self.ui.tabWidget_2.setCurrentIndex(1)
            self.image_left = "logo_2.png"
            self.image_right = "logo_3.png"
            self.img_L_Edit = Image(self.image_left, 2 * inch, 1.6 * inch)
            self.img_R_Edit = Image(self.image_right, 1.8 * inch, 1.3 * inch)
            # self.style = getSampleStyleSheet()
            headline_style = self.styles["Heading2"]

            # Data to be stored on table
            self.data_first_line = [
                [self.img_L_Edit, Paragraph("Biological Signal Report", headline_style), self.img_R_Edit]
            ]
            # Creating the table with 6 rows
            self.table = Table(self.data_first_line, 3 * [2.7 * inch], 1 * [.7 * inch])
            # setting up style and alignments of borders and grids
            self.table.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
                    ]
                )
            )
            self.sequnce_of_display_data.append(self.table)

            self.data_third_line = [
                [Paragraph("Signal of Channel 2", headline_style), "", ""]
            ]
            self.place_third_line = Table(self.data_third_line, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_third_line)

            self.picture_for_signal_2 = screen.grabWindow(self.GraphicsView[1].winId())
            self.picture_for_signal_2.save(
                r'D:\College\pdfs\signal_channel_2.png')
            self.image_signal_channel_2 = "D:\College\pdfs\signal_channel_2.png"
            self.Edit_image_signal_channel_2 = Image(self.image_signal_channel_2, 6 * inch, 1.7 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_signal_channel_2)

            self.data_third_line_spec = [
                [Paragraph("spectro of Channel 2", headline_style), "", ""]
            ]
            self.place_third_line_spec = Table(self.data_second_line_spec, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_spec)
            self.ui.tabWidget_2.setCurrentIndex(1)
            self.picture_for_spec_2 = screen.grabWindow(self.Canvas[1].winId())
            self.picture_for_spec_2.save(
                r'D:\College\pdfs\spec_channel_2.png')
            self.image_spec_channel_2 = "D:\College\pdfs\spec_channel_2.png"
            self.Edit_image_spec_channel_2 = Image(self.image_spec_channel_2, 6 * inch, 1.8 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_spec_channel_2)

            self.data_third_line_Datastatistics = [
                [Paragraph("Data of Channel 2", headline_style), "", ""]
            ]
            self.place_third_line_Datastatistics = Table(self.data_second_line_Datastatistics, 1 * [2.4 * inch],
                                                         1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_Datastatistics)

            self.data_for_second_table = [
                ["Mean", str(np.mean(self.amplitudeUpd[1]))],
                ["STD", str(np.std(self.amplitudeUpd[1]))],
                ["Duration", self.timeUpd[1][len(self.timeUpd[1]) - 1]],
                ["min Value", np.min(self.amplitudeUpd[1])],
                ["Max Value", np.max(self.amplitudeUpd[1])],
            ]
            self.table_2 = Table(self.data_for_second_table, 3 * [3.0 * inch], 5 * [0.5 * inch])
            self.table_2.setStyle(
                TableStyle(
                    [
                        ("INNERGRID", (0, 0), (-1, -1), 2, black),
                        ("BOX", (0, 0), (-1, -1), 2, black),
                        ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (0, -1), 12)
                    ]
                )
            )
            self.sequnce_of_display_data.append(self.table_2)
        if (self.pdf_check[2]):
            self.image_left = "logo_2.png"
            self.image_right = "logo_3.png"
            self.img_L_Edit = Image(self.image_left, 2 * inch, 1.6 * inch)
            self.img_R_Edit = Image(self.image_right, 1.8 * inch, 1.3 * inch)
            # self.style = getSampleStyleSheet()
            headline_style = self.styles["Heading2"]

            # Data to be stored on table
            self.data_first_line = [
                [self.img_L_Edit, Paragraph("Biological Signal Report", headline_style), self.img_R_Edit]
            ]
            # Creating the table with 6 rows
            self.table = Table(self.data_first_line, 3 * [2.7 * inch], 1 * [.7 * inch])
            # setting up style and alignments of borders and grids
            self.table.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (-1, -1), (-1, -1), "RIGHT"),
                    ]
                )
            )
            self.sequnce_of_display_data.append(self.table)

            self.data_fourth_line = [
                [Paragraph("Signal of Channel 3", headline_style), "", ""]
            ]
            self.place_fourth_line = Table(self.data_fourth_line, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_fourth_line)

            self.picture_for_signal_3 = screen.grabWindow(self.GraphicsView[2].winId())
            self.picture_for_signal_3.save(
                r'D:\College\pdfs\signal_channel_3.png')
            self.image_signal_channel_3 = "D:\College\pdfs\signal_channel_3.png"
            self.Edit_image_signal_channel_3 = Image(self.image_signal_channel_3, 6 * inch, 1.7 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_signal_channel_3)

            self.data_third_line_spec = [
                [Paragraph("spectro of Channel 3", headline_style), "", ""]
            ]
            self.place_third_line_spec = Table(self.data_second_line_spec, 3 * [2.5 * inch], 1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_spec)

            self.picture_for_spec_3 = screen.grabWindow(self.TabWidgets_Spec[2].winId())
            self.picture_for_spec_3.save(
                r'D:\College\pdfs\spec_channel_3.png')
            self.image_spec_channel_3 = "D:\College\pdfs\spec_channel_3.png"
            self.Edit_image_spec_channel_3 = Image(self.image_spec_channel_3, 6 * inch, 1.8 * inch)
            self.sequnce_of_display_data.append(self.Edit_image_spec_channel_3)

            self.data_third_line_Datastatistics = [
                [Paragraph("Data of Channel 3", headline_style), "", ""]
            ]
            self.place_third_line_Datastatistics = Table(self.data_second_line_Datastatistics, 1 * [2.4 * inch],
                                                         1 * [.7 * inch])
            self.sequnce_of_display_data.append(self.place_second_line_Datastatistics)

            self.data_for_third_table = [
                ["Mean", str(np.mean(self.amplitudeUpd[2]))],
                ["STD", str(np.std(self.amplitudeUpd[2]))],
                ["Duration", self.timeUpd[2][len(self.timeUpd[2]) - 1]],
                ["min Value", np.min(self.amplitudeUpd[2])],
                ["Max Value", np.max(self.amplitudeUpd[2])],
            ]
            self.table_3 = Table(self.data_for_third_table, 3 * [3.0 * inch], 5 * [0.5 * inch])
            self.table_3.setStyle(
                TableStyle(
                    [
                        ("INNERGRID", (0, 0), (-1, -1), 2, black),
                        ("BOX", (0, 0), (-1, -1), 2, black),
                        ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (0, -1), 12)
                    ]
                )
            )
            self.sequnce_of_display_data.append(self.table_3)
        if (not (self.pdf_check[0] or self.pdf_check[1] or self.pdf_check[2])):
            self.data_fifth_line = [
                ["", Paragraph("THERE No SIGNAL TO BE REPORTED", headline_style), ""]
            ]
            self.place_fifth_line = Table(self.data_fifth_line, 3 * [4 * inch], 1 * [2 * inch])
            self.sequnce_of_display_data.append(self.place_fifth_line)

        self.document.build(self.sequnce_of_display_data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

