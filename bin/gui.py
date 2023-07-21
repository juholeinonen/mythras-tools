import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QSpinBox
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QFont

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import json

HIT_LOCATION_POSITIONS = {
    "right_leg": (120, 175),
    "left_leg": (-30, 175),
    "abdomen": (5, 3),
    "chest": (5, 2),
    "right_arm": (7, 3),
    "left_arm": (2, 3),
    "head": (5, 1),
}


class NpcWindow(QWidget):
    def __init__(self, npc_data):
        super().__init__()
        self.npc_data = npc_data
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()  # This is the main layout
        self.setLayout(main_layout)

        images_layout = QHBoxLayout()  # This layout is for the images
        main_layout.addLayout(images_layout)  # Add the images layout to the main layout

        self.init_image(images_layout)  # initialize the image
        self.init_hitpoints(images_layout)  # initialize the hitpoints

        self.init_skills(main_layout)  # initialize the skills

    def init_image(self, layout):
        pixmap = QPixmap(self.npc_data['image_path'])
        if pixmap.isNull():
            print(f"Failed to load image at {self.npc_data['image_path']}")
        else:
            # Rescaled QPixmap
            scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)

            # Create QLabel with QPixmap
            lbl_img = QLabel()
            lbl_img.setPixmap(scaled_pixmap)
            layout.addWidget(lbl_img)

    def init_skills(self, layout):
        # create the grid layout
        grid_layout = QGridLayout()

        # Display NPC skills
        column_count = 3
        total_rows = 0  # this will keep track of how many rows have been added

        for skill_type in ['standard_skills', 'magic_skills', 'professional_skills', 'custom_skills', 'combat_styles']:
            lbl_skill_type = QLabel(f'{skill_type.replace("_", " ").capitalize()}:')
            grid_layout.addWidget(lbl_skill_type, total_rows, 0, 1, column_count)  # span the label across all columns
            total_rows += 1  # increment total_rows for the skill_type label

            for skill_index, (skill, value) in enumerate(self.npc_data[skill_type].items()):
                lbl_skill = QLabel(f'{skill}:')
                spin_box = QSpinBox()
                spin_box.setRange(1, 100)
                spin_box.setValue(value)

                # calculate the row and column for the grid
                row = total_rows + skill_index // column_count
                column = skill_index % column_count

                grid_layout.addWidget(lbl_skill, row, column * 2)  # label goes in even column
                grid_layout.addWidget(spin_box, row, column * 2 + 1)  # spinbox goes in odd column

            total_rows += skill_index // column_count + 1  # increment total_rows for the number of rows of skills added

        # add grid layout to the QVBoxLayout
        layout.addLayout(grid_layout)

    def init_hitpoints(self, layout):
        # create the graphics view
        view = QGraphicsView()

        # create the graphics scene
        scene = QGraphicsScene()

        pixmap = QPixmap(self.npc_data['image_path'])
        if pixmap.isNull():
            print(f"Failed to load image at {self.npc_data['image_path']}")
        else:
            # Rescaled QPixmap
            scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)

        # add the image to the scene
        scene.addPixmap(scaled_pixmap)

        # add the scene to the view
        view.setScene(scene)

        # set font for QGraphicsTextItems
        font = QFont()
        font.setPointSize(14)

        # for each hit location, add an editable QGraphicsTextItem
        for hit_location, hp in self.npc_data['hitpoints'].items():
            x, y = HIT_LOCATION_POSITIONS[hit_location]
            text_item = QGraphicsTextItem(f"{hit_location}: {hp}")
            text_item.setFont(font)
            text_item.setPos(x, y)
            text_item.setTextInteractionFlags(Qt.TextEditorInteraction)  # make the text item editable
            scene.addItem(text_item)

        layout.addWidget(view)

if __name__ == '__main__':
    with open('../data/efar.json', 'r') as f:
        npc_data = json.load(f)

    app = QApplication(sys.argv)
    ex = NpcWindow(npc_data)
    ex.show()
    sys.exit(app.exec_())
