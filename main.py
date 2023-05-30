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
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QPainterPath, QPalette, QColor
# Add the import statement for QtCore
from PyQt5 import QtCore

from extraWindows import EnrollWindow



class LabelsWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a horizontal layout for the labels
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignLeft)

        # Add three label widgets to the horizontal layout
        label1 = QLabel("Programs", self)
        label1.setStyleSheet("font-weight: bold; font-size: 24px;")
        label1.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        label2 = QLabel("Users", self)
        label2.setStyleSheet("font-weight: bold; font-size: 24px; color: #c0c0c0;")
        label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        label3 = QLabel("Admin", self)
        label3.setStyleSheet("font-weight: bold; font-size: 24px; color: #c0c0c0;")
        label3.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addItem(spacer)
        layout.addWidget(label3)

        self.setLayout(layout)


class InputWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a horizontal layout for the text field and button
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        layout.setAlignment(Qt.AlignLeft)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Create a QLineEdit (text field) and set maximum width
        text_field = QLineEdit(self)
        text_field.setStyleSheet("font-size: 18px;")
        text_field.setPlaceholderText("Enter text...")
        text_field.setStyleSheet("QLineEdit { padding: 4px; border-radius: 8px; }")
        text_field.setMaximumWidth(200)  # Set maximum width to 200 pixels
        text_field.setFocusPolicy(Qt.ClickFocus)
        text_field.setFixedSize(200, 36)

        # Create a QPushButton (button) with background color and border radius
        button = QPushButton("Submit", self)
        button.setStyleSheet(
            "font-size: 18px; border-radius: 12px; background-color: #CB1919; color: white;"
        )
        button.setFixedSize(110, 36)

        layout.addItem(spacer)
        layout.addWidget(button)
        layout.addWidget(text_field)

        self.setLayout(layout)
class ClickableContainer(QFrame):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.rect().contains(event.pos()):
            self.clicked.emit()  # Emit the clicked signal if the release event occurred within the container


class CardItem(QFrame):
    def __init__(self, title, subtitle, image_url):
        super().__init__()

        self.setObjectName("CardItem")
        self.setStyleSheet(
            """
            #CardItem {
                background-color: #FFFFFF;
                border-radius: 15px;
                border: 1px solid #f0f0f0;
                padding: 8px;
            }
            """
        )

        self.setMouseTracking(True)  # Enable mouse tracking to receive hover events
        
        # Create a QVBoxLayout for the content inside the card item
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Align items to the top

        # Create a QLabel for the picture
        picture_label = QLabel(self)
        picture_label.setStyleSheet("background-color: #ffffff; border-radius: 4px;")

        # Load the image
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)  # Assuming you have the `requests` library imported

        # Check if the pixmap height is non-zero
        if pixmap.height() != 0:
            # Calculate the desired height and width based on the desired height and aspect ratio
            desired_height = 200
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
            picture_label.setScaledContents(True)  # Scale the image to fit the label

        else:
            # Handle the case where the height is zero
            # Display a placeholder image or show an error message
            pass
       
        # Add the picture label to the card layout
        layout.addWidget(picture_label)

        # Create a QLabel for the title of the card
        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setWordWrap(True)  # Enable wrapping for long titles
        title_label.setMaximumHeight(48)  # Limit the maximum height to show up to 3 lines

        # Create a QLabel for the subtitle of the card
        subtitle_label = QLabel(subtitle, self)
        subtitle_label.setStyleSheet("font-size: 14px; color: #808080;")
        subtitle_label.setWordWrap(True)  # Enable wrapping for long subtitles
        subtitle_label.setFixedHeight(50)  # Limit the maximum height to show up to 3 lines
        subtitle_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Create a ClickableContainer for the "Enroll now" text
        enroll_container = ClickableContainer(self)
        enroll_container.setObjectName("EnrollContainer")
        enroll_container.setStyleSheet(
            """
            #EnrollContainer {
                background: qlineargradient(x1:0, y1:0, x2:2, y2:1, stop:0 #FFABAB, stop:1 #FFDA83);
                border-radius: 7px;
            }
            
            #EnrollContainer:hover {
                background-color: #FFABAB;
                border-radius: 7px;
            }
            """
        )
        enroll_container.clicked.connect(self.handleEnrollClicked)
        
        # Create a QLabel for the "Enroll now" text
        enroll_label = QLabel("Enroll now", enroll_container)
        enroll_label.setObjectName("EnrollLabel")
        enroll_label.setStyleSheet(
            """
            #EnrollLabel {
                font-size: 16px;
                color: white;
                font-weight: bold;
                padding: 4px;
            }
            """
        )
        enroll_label.setAlignment(Qt.AlignCenter)

        # Add the enroll label to the enroll container
        enroll_container_layout = QVBoxLayout()
        enroll_container_layout.addWidget(enroll_label)
        enroll_container.setLayout(enroll_container_layout)

        # Add the picture placeholder, title, subtitle, and enroll container to the card layout
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(enroll_container)

        # Set the layout for the card frame
        self.setLayout(layout)
        
    def handleEnrollClicked(self):
        enroll_window = EnrollWindow()
        enroll_window.exec_()

        print("Enroll now clicked!")



class ScrollableContentWidget(QWidget):
    def __init__(self, data):
        super().__init__()

        # Create a vertical layout for the scrollable content
        layout = QVBoxLayout()

        # Create a QLabel for the "Enrolled" label
        enrolled_label = QLabel("Available", self)
        enrolled_label.setStyleSheet(
            "font-weight: bold; font-size: 24px; color: #c0c0c0;"
        )
        enrolled_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        layout.addWidget(enrolled_label)

        # Create a QGridLayout to hold the card-like items
        self.cards_layout = QGridLayout()
        self.cards_layout.setAlignment(Qt.AlignTop)
        self.cards_layout.setSpacing(10)  # Adjust spacing as needed

        # Add card-like items to the layout
        self.cards = []
        for i, item_data in enumerate(data):
            
            
            try:
                title=item_data['title']
            except (KeyError, TypeError):
                title = '<Undefined>'
            
            try:
                subtitle = item_data['subtitle']
            except (KeyError, TypeError):
                subtitle = 'There is no information about this event'
            
            try:
                image_url = item_data['thumbnail_url']
            except (KeyError, TypeError):
                image_url = 'https://static-prod.adweek.com/wp-content/uploads/2018/06/Events.jpg.webp'

            # Create a CardItem with sample data
            card = CardItem(
                title=title,
                subtitle=subtitle,
                image_url= image_url)
            
            self.cards.append(card)

            # Add the card to the grid layout at the initial position
            self.cards_layout.addWidget(card, i // 4, i % 4)

        # Create a QWidget to hold the grid layout
        cards_container = QWidget()
        cards_container.setLayout(self.cards_layout)

        # Create a QScrollArea to make the content scrollable
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(cards_container)

        # Set the frame shape of the scroll area widget to NoFrame
        scroll_area.setFrameShape(QFrame.NoFrame)

        layout.addWidget(scroll_area)

        self.setLayout(layout)
        
    def resizeEvent(self, event):
        # Calculate the new number of cards per row based on the program window width
        card_width = 200  # Adjust this value to fit your card width
        spacing = 10  # Adjust spacing as needed
        window_width = self.width() - 400
        num_cards_per_row = max(1, (window_width - spacing) // (card_width + spacing))

        # Update the cards layout
        for i, card in enumerate(self.cards):
            row = i // num_cards_per_row
            col = i % num_cards_per_row
            self.cards_layout.addWidget(card, row, col)

        super().resizeEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create a palette with the desired background color
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor("#FFFFFF"))  # Replace #FFFFFF with your desired color

        # Set the window title and size
        self.setWindowTitle("Program Enrollments")
        # self.resize(800, 600)

        # Create a central widget for the main window
        central_widget = QWidget(self)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Set margins to add spacing

        # Create and add the LabelsWidget to the layout
        labels_widget = LabelsWidget()
        layout.addWidget(labels_widget)

        # Create and add the InputWidget to the layout
        input_widget = InputWidget()
        layout.addWidget(input_widget)

        # Create and add the ScrollableContentWidget to the layout
        scrollable_widget = ScrollableContentWidget(data=[
            {'title': 'Title 1', 'subtitle': 'Subtitle 1','thumbnail_url':'https://blog.vantagecircle.com/content/images/2019/06/company-event.png'},
            { },
            {'title': 'Title 3', 'subtitle': 'Subtitle 3'},
            {'title': 'Title 4', 'subtitle': 'Subtitle 4'},
          
        ])
        layout.addWidget(scrollable_widget)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
