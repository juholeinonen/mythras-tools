import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QSpinBox
from PyQt5.QtWidgets import QGridLayout

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import json


class NpcWindow(QWidget):
    def __init__(self, npc_data):
        super().__init__()
        self.npc_data = npc_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

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

        self.setLayout(layout)

if __name__ == '__main__':
    with open('../data/efar.json', 'r') as f:
        npc_data = json.load(f)

    app = QApplication(sys.argv)
    ex = NpcWindow(npc_data)
    ex.show()
    sys.exit(app.exec_())
