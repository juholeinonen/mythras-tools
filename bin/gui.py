import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QSpinBox
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

        # Display NPC skills
        for skill_type in ['standard_skills', 'magic_skills', 'professional_skills', 'custom_skills', 'combat_styles']:
            lbl_skill_type = QLabel(f'{skill_type.replace("_", " ").capitalize()}: ')
            layout.addWidget(lbl_skill_type)
            for skill, value in self.npc_data[skill_type].items():
                lbl_skill = QLabel(f'    {skill}: ')
                spin_box = QSpinBox()
                spin_box.setRange(1, 100)
                spin_box.setValue(value)
                layout.addWidget(lbl_skill)
                layout.addWidget(spin_box)

        self.setLayout(layout)


if __name__ == '__main__':
    with open('../data/efar.json', 'r') as f:
        npc_data = json.load(f)

    app = QApplication(sys.argv)
    ex = NpcWindow(npc_data)
    ex.show()
    sys.exit(app.exec_())
