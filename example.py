import maya.cmds as cmds
from functools import partial


class ColorChangeWin(object):

    def __init__(self):
        self.buildWin()

    def buildWin(self):
        self.win = cmds.window(title="ColorChange")
        self.menuLayout = cmds.menuBarLayout()
        self.menu = cmds.menu(label="Window")
        self.menuItem = cmds.menuItem(label="Close", command=partial(self.closeWin, self.win))
        self.mainlayout = cmds.columnLayout(adj=True)
        self.color = cmds.intSlider(min=0, max=2, value=0, step=1, cc=partial(self.setColor), p=self.mainlayout)  # Add self.
        self.textButton = cmds.iconTextButton(w=55, bgc=(0.467, 0.467, 0.467), p=self.mainlayout)  # Capture in variable.
        cmds.showWindow(self.win)

    def closeWin(self, window=None, arg=None):
        if cmds.window(self.win, exists=True):
            cmds.deleteUI(self.win, window=True)

    def setColor(self, color_1):  # Add self as first parameter. No need to query the slider's value, as the 2nd parameter already has it from its changeCommand.
        if color_1 == 0: 
            cmds.iconTextButton(self.textButton, e=True, bgc=(1, 1, 1))
        if color_1 == 1:
            cmds.iconTextButton(self.textButton, e=True, bgc=(0, 0, 1))
        if color_1 == 2:
            cmds.iconTextButton(self.textButton, e=True, bgc=(0.608, 0, 0.157))


ColorChangeWin()