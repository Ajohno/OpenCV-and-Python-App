import sys
from pathlib import Path

# Qt has many modules. QtCore contains non-visual Qt tools, while QtWidgets
# contains the building blocks for normal desktop windows.
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


# A QMainWindow is a standard top-level app window. It gives you a title bar,
# resizing, menus/toolbars if you add them later, and one central widget area.
class ImageRectangleWindow(QMainWindow):
    def __init__(self):
        # super() runs QMainWindow's setup before we add our own widgets.
        super().__init__()

        # Basic window settings.
        self.setWindowTitle("PySide Image Rectangle Demo")
        self.resize(520, 620)

        # QLabel displays read-only text.
        self.title = QLabel("Draw a Rectangle")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 22px; font-weight: 600;")

        # QLabel can also display images when you give it a QPixmap.
        self.image = QLabel()
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setMinimumHeight(360)

        # Build the image path from this file's folder, not the terminal's
        # current folder. That makes the path more reliable.
        image_path = Path(__file__).with_name("image.jpg")
        pixmap = QPixmap(str(image_path))

        if pixmap.isNull():
            self.image.setText("Could not load image.jpg")
            self.base_pixmap = QPixmap(480, 360)
            self.base_pixmap.fill(Qt.white)
        else:
            # Keep the image visible without stretching it out of proportion.
            self.base_pixmap = pixmap.scaled(
                480,
                360,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

        self.image.setPixmap(self.base_pixmap)

        # These spin boxes let the user enter rectangle coordinates.
        # x and y are the top-left corner of the rectangle.
        # width and height control how large the rectangle is.
        self.x_input = self.make_spin_box(0, self.base_pixmap.width() - 1, 30)
        self.y_input = self.make_spin_box(0, self.base_pixmap.height() - 1, 30)
        self.width_input = self.make_spin_box(1, self.base_pixmap.width(), 160)
        self.height_input = self.make_spin_box(1, self.base_pixmap.height(), 100)

        input_form = QFormLayout()
        input_form.addRow("X", self.x_input)
        input_form.addRow("Y", self.y_input)
        input_form.addRow("Width", self.width_input)
        input_form.addRow("Height", self.height_input)

        # QPushButton emits a clicked signal when the user presses it.
        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.draw_rectangle)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_image)

        button_row = QHBoxLayout()
        button_row.addWidget(self.draw_button)
        button_row.addWidget(self.reset_button)

        self.status = QLabel(
            f"Displayed image size: {self.base_pixmap.width()} x "
            f"{self.base_pixmap.height()} pixels"
        )
        self.status.setAlignment(Qt.AlignCenter)

        # QVBoxLayout arranges widgets top-to-bottom.
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.image)
        layout.addLayout(input_form)
        layout.addLayout(button_row)
        layout.addWidget(self.status)

        # QMainWindow needs a central widget. Layouts cannot be set directly on
        # QMainWindow, so we put the layout inside a plain QWidget first.
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def make_spin_box(self, minimum, maximum, value):
        spin_box = QSpinBox()
        spin_box.setRange(minimum, maximum)
        spin_box.setValue(value)
        return spin_box

    def draw_rectangle(self):
        # Work on a copy so pressing Draw does not stack rectangles on top of
        # older ones.
        pixmap_with_rectangle = QPixmap(self.base_pixmap)

        # QPainter is Qt's drawing tool. It can draw lines, rectangles, text,
        # and other shapes onto a QPixmap.
        painter = QPainter(pixmap_with_rectangle)
        pen = QPen(QColor("red"))
        pen.setWidth(4)
        painter.setPen(pen)

        x = self.x_input.value()
        y = self.y_input.value()
        width = self.width_input.value()
        height = self.height_input.value()

        painter.drawRect(x, y, width, height)
        painter.end()

        self.image.setPixmap(pixmap_with_rectangle)
        self.status.setText(f"Rectangle drawn at x={x}, y={y}, w={width}, h={height}")

    def reset_image(self):
        self.image.setPixmap(self.base_pixmap)
        self.status.setText(
            f"Displayed image size: {self.base_pixmap.width()} x "
            f"{self.base_pixmap.height()} pixels"
        )


def main():
    # QApplication owns the Qt event loop. Every PySide app needs exactly one.
    app = QApplication(sys.argv)

    # Build and show our custom window.
    window = ImageRectangleWindow()
    window.show()

    # app.exec() starts the event loop. The program stays here until the
    # window is closed.
    sys.exit(app.exec())


# This keeps the app from launching if another file imports this one.
if __name__ == "__main__":
    main()
