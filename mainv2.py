#doesn't work!
import maya.cmds as mc
import TableChaise
from functools import partial
mc.file(f=True, new=True)


winName = 'myWindow'
winWidth = 1024 # set a target width and reference this when you specify width


class GUI(object):
    
    def __init__(self):
        self.buildWin()
        tablewidthz = cmds.intSliderGrp(self.slider1, q=True, value=True)
        tableWidthx = cmds.intSliderGrp(self.slider2, q=True, value=True)
        tableHeight = cmds.intSliderGrp(self.slider3, q=True, value=True)
        Chaisewidthz = cmds.intSliderGrp(self.slider4, q=True, value=True)
        ChaiseWidthx = cmds.intSliderGrp(self.slider5, q=True, value=True)
        ChaiseHeight = cmds.intSliderGrp(self.slider6, q=True, value=True)
        Distance = cmds.intSliderGrp(self.slider7, q=True, value=True)
        #def variables?
        # def initVars():
        #     self.tablewidthz = cmds.intSliderGrp(self.slider1, q=True, value=True)
        #     self.tableWidthx = cmds.intSliderGrp(self.slider2, q=True, value=True)
        #     self.tableHeight = cmds.intSliderGrp(self.slider3, q=True, value=True)
        #     self.Chaisewidthz = cmds.intSliderGrp(self.slider4, q=True, value=True)
        #     self.ChaiseWidthx = cmds.intSliderGrp(self.slider5, q=True, value=True)
        #     self.ChaiseHeight = cmds.intSliderGrp(self.slider6, q=True, value=True)
        #     self.Distance = cmds.intSliderGrp(self.slider7, q=True, value=True)
    def buildWin(self):
        if mc.window(winName, exists=True):
            mc.deleteUI(winName)
        mc.window(winName, width=winWidth, title='Forniture Generator')
        #reference to the main columnLayout
        self.mainCL = mc.columnLayout() 
        self.mainRLWidth = [winWidth*0.6, winWidth*0.4]
        self.mainRL = mc.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=self.mainRLWidth, rowAttach=(2, 'top', 0))

        mc.columnLayout(w=self.mainRLWidth[0]) # create a columnLayout under the first row of mainRL
        mc.text(label='Table', font='boldLabelFont')
        mc.text(label='')
        self.slider1 = mc.intSliderGrp(field=True, label='tablewidthz', minValue=4, maxValue=20, value=10, width=winWidth/2 )
        self.slider2 = mc.intSliderGrp(field=True, label='tableWidthx', minValue=2, maxValue=20, value=10, width=winWidth/2 )
        self.slider3 = mc.intSliderGrp(field=True, label='tableHeight', minValue=2, maxValue=20, value=6, width=winWidth/2 )
        #-------------------------------------------------------------------------------------------------------------------
        mc.text(label='')
        mc.text(label='Chaise:', font='boldLabelFont')
        self.slider4 = mc.intSliderGrp(field=True, label='Chaisewidthz', minValue=4, maxValue=6, value=4, width=winWidth/2 )
        self.slider5 = mc.intSliderGrp(field=True, label='ChaiseWidthx', minValue=2, maxValue=6, value=5, width=winWidth/2 )
        self.slider6 = mc.intSliderGrp(field=True, label='ChaiseHeight', minValue=2, maxValue=10, value=4, width=winWidth/2 )
        self.slider7 = mc.intSliderGrp(field=True, label='Distance', minValue=-10, maxValue=10, value=-5, width=winWidth/2 )

        mc.setParent('..') # this will exit the rowLayout back to the mainRL, same as mc.setParent(mainRL)

        mc.columnLayout(width=self.mainRLWidth[1]) # start another vertical layout
        mc.text(label='Table', font='boldLabelFont')
        mc.text(label='')
        mc.button(label='runFirst', width=self.mainRLWidth[1]*0.95, height=70, c='variablesTopass()')
        mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Generate Table',width=self.mainRLWidth[1]*0.95, c='TableChaise.table(tablewidthz, tableWidthx, tableHeight)')
        mc.text(label='Chaise', font='boldLabelFont')
        mc.text(label='')
        mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Generate Chaise',width=self.mainRLWidth[1]*0.95, c='TableChaise.Chaise(Chaisewidthz, ChaiseWidthx, ChaiseHeight, Distance)')
        #mc.button(label='button', width=mainRLWidth[1]*0.95, height=70)

        #   mc.setParent(mainCL) # set UI pointer back under the main columnLayout
        #   mc.text(label='')
        #   mc.button(label='full window width button', width=winWidth, height=40)

        mc.showWindow(winName)
        mc.window(winName, e=True, width=winWidth, height=1)

GUI()
