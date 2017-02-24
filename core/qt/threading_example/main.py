from Slider import Slider_Dialog
from Progress import ProgressBar_Dialog
from loop import Loop

import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sd = Slider_Dialog()
    pb = ProgressBar_Dialog()

    loop = Loop()

    pb.make_connection(loop)

    loop.start()
    sys.exit(app.exec_())