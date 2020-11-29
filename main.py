#this is not working...

import maya.cmds as mc
import TableChaise
from functools import partial
mc.file(f=True, new=True)


winName = 'myWindow'
winWidth = 1024 # set a target width and reference this when you specify width
if mc.window(winName, exists=True):
    mc.deleteUI(winName)
mc.window(winName, width=winWidth, title='Forniture Generator')
#reference to the main columnLayout
mainCL = mc.columnLayout() 
mainRLWidth = [winWidth*0.6, winWidth*0.4]
mainRL = mc.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

#def variables?

tablewidthz = cmds.intSliderGrp("slider1", q=True, value=True)
tableWidthx = cmds.intSliderGrp(slider2, q=True, value=True)
tableHeight = cmds.intSliderGrp(slider3, q=True, value=True)
Chaisewidthz = cmds.intSliderGrp(slider4, q=True, value=True)
ChaiseWidthx = cmds.intSliderGrp(slider5, q=True, value=True)
ChaiseHeight = cmds.intSliderGrp(slider6, q=True, value=True)
Distance = cmds.intSliderGrp(slider7, q=True, value=True)

mc.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
mc.text(label='Table', font='boldLabelFont')
mc.text(label='')
mc.intSliderGrp("slider1", field=True, label='tablewidthz', minValue=4, maxValue=20, value=10, width=winWidth/2 )
mc.intSliderGrp("slider2", field=True, label='tableWidthx', minValue=2, maxValue=20, value=10, width=winWidth/2 )
mc.intSliderGrp("slider3", field=True, label='tableHeight', minValue=2, maxValue=20, value=6, width=winWidth/2 )
#-------------------------------------------------------------------------------------------------------------------
mc.text(label='')
mc.text(label='Chaise:', font='boldLabelFont')
mc.intSliderGrp("slider4", field=True, label='Chaisewidthz', minValue=4, maxValue=6, value=4, width=winWidth/2 )
mc.intSliderGrp("slider5", field=True, label='ChaiseWidthx', minValue=2, maxValue=6, value=5, width=winWidth/2 )
mc.intSliderGrp("slider6", field=True, label='ChaiseHeight', minValue=2, maxValue=10, value=4, width=winWidth/2 )
mc.intSliderGrp("slider7", field=True, label='Distance', minValue=-10, maxValue=10, value=-5, width=winWidth/2 )

mc.setParent('..') # this will exit the rowLayout back to the mainRL, same as mc.setParent(mainRL)

mc.columnLayout(width=mainRLWidth[1]) # start another vertical layout
mc.text(label='Table', font='boldLabelFont')
mc.text(label='')
mc.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='variablesTopass()')
mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Generate Table',width=mainRLWidth[1]*0.95, c='TableChaise.table(tablewidthz, tableWidthx, tableHeight)')
mc.text(label='Chaise', font='boldLabelFont')
mc.text(label='')
mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Generate Chaise',width=mainRLWidth[1]*0.95, c='TableChaise.Chaise(Chaisewidthz, ChaiseWidthx, ChaiseHeight, Distance)')
#mc.button(label='button', width=mainRLWidth[1]*0.95, height=70)

#   mc.setParent(mainCL) # set UI pointer back under the main columnLayout
#   mc.text(label='')
#   mc.button(label='full window width button', width=winWidth, height=40)

mc.showWindow(winName)
mc.window(winName, e=True, width=winWidth, height=1)