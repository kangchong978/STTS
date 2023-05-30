import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QFrame,
    QScrollArea,
    QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QPainterPath, QPalette, QColor
class EnrollWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Set dialog title
        self.setWindowTitle("Dialog with Sections")

        # Create the main layout for the dialog
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Create the left section layout
        left_layout = QVBoxLayout()
        left_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)

         # Create a QLabel for the picture
        picture_label = QLabel(self)
        picture_label.setStyleSheet("border-radius: 4px;")
        
        # Load the image
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get("https://static-prod.adweek.com/wp-content/uploads/2018/06/Events.jpg.webp").content)  # Assuming you have the `requests` library imported
        # Check if the pixmap height is non-zero
        if pixmap.height() != 0:
            # Calculate the desired height and width based on the desired height and aspect ratio
            desired_height = 160
            aspect_ratio = pixmap.width()  / pixmap.height()
            desired_width = int(desired_height * aspect_ratio)

            # Scale the image to the desired size while maintaining the aspect ratio
            scaled_pixmap = pixmap.scaled(
                desired_width,
                desired_height, 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )

            # Create a mask for the rounded rectangle
            mask_bitmap = QBitmap(scaled_pixmap.size())
            mask_bitmap.fill(Qt.color0)  # Fill the mask with transparent color

            # Create a QPainter and set the mask
            painter = QPainter(mask_bitmap)
            painter.setRenderHint(QPainter.Antialiasing, True)  # Enable anti-aliasing for smooth edges

            # Create a QPainterPath for the rounded rectangle
            rounded_rect = QPainterPath()
            rounded_rect.addRoundedRect(
                scaled_pixmap.rect().x(),
                scaled_pixmap.rect().y(),
                scaled_pixmap.rect().width(),
                scaled_pixmap.rect().height(),
                8,
                8
            )

            # Draw the rounded rectangle on the mask
            painter.setBrush(Qt.color1)  # Fill color1 (white) for the rounded rectangle
            painter.setPen(Qt.NoPen)  # No outline
            painter.drawPath(rounded_rect)

            # Set the mask on the scaled pixmap
            scaled_pixmap.setMask(mask_bitmap)

            # Clean up the QPainter
            painter.end()

            # Set the scaled pixmap as the background image for the label
            picture_label.setPixmap(scaled_pixmap)
            # picture_label.setScaledContents(True)  # Scale the image to fit the label

        else:
            # Handle the case where the height is zero
            # Display a placeholder image or show an error message
            pass
         # Add the picture label to the card layout
        # Create the left section layout
        left_layout = QVBoxLayout()

        # Set a fixed width of 180 pixels for the left section
        left_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        left_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setFixedWidth(200)

        # Add the picture label to the left layout
        left_layout.addWidget(picture_label)

        # Create a QLabel for the title of the card
        title_label = QLabel("Title", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setWordWrap(True)  # Enable wrapping for long titles
        title_label.setMaximumHeight(48)  # Limit the maximum height to show up to 3 lines
        left_layout.addWidget(title_label)

        # Create a QLabel for the subtitle of the card
        subtitle_label = QLabel("Subtitfjsaklfjskajflksajfklsajfklas;jflsajflksajfkldsjlkfjaslfjask;djf;lksajflsdjflksajfklsdajfkldsjfkldsjfklajsdklfjadsdsafl;j;afdsjk;ljfkldsajfkldjfklajfklsdajflksjdlle", self)
        subtitle_label.setStyleSheet("font-size: 14px; color: #808080;")
        subtitle_label.setWordWrap(True)  # Enable wrapping for long subtitles
        subtitle_label.setFixedHeight(50)  # Limit the maximum height to show up to 3 lines
        subtitle_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        left_layout.addWidget(subtitle_label)

        # Add the left section to the main layout
        main_layout.addWidget(left_widget)
       
        # Create the right section layout
        right_layout = QVBoxLayout()

        # Add "Application form" label to the right section
        form_label = QLabel("Application form")
        right_layout.addWidget(form_label)

        # Add "Submit" button to the right section
        submit_button = QPushButton("Submit")
        right_layout.addWidget(submit_button)

        # Add the right section to the main layout
        main_layout.addLayout(right_layout)
        