import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def four():

    #group MODULE
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    oven = 'Oven'+ str(mir) + str(crazyR) 
    cmds.group(n = oven, em=True)
    base_heigh = cmds.intSliderGrp(slider1, q=True, value=True)
    base_width = cmds.intSliderGrp(slider2, q=True, value=True)
    base_depth = cmds.intSliderGrp(slider3, q=True, value=True)

    #base:
    base = cmds.polyCube(h=base_heigh, w=base_width, depth=base_depth)
    cmds.polyBevel3(base,offset=0.1)
    door = cmds.polyCube(h=base_heigh - base_heigh/2, w=base_width - base_width/2, depth=0.2)
    cmds.move(0,-base_heigh/20.0,-base_width/2.0)
    cmds.parent(base, door, oven)
    #swiches:
    sdoor = cmds.ls(door)
    for i in range(3):
        switch =  cmds.polySphere(sx=5, sy=5, r=0.2)
        cmds.move(-base_width/4.0 + i -0.2*i,base_heigh/2.5,-base_width/2.1)
        cmds.parent(switch, oven)
    for i in range(2):
        heatersOne =  cmds.polyCylinder(sx=7, sy=7, h=0.2, r=base_width/1000)
        cmds.move(-base_width/6.0 + i,base_heigh/2.0,-base_width/3.5)
        cmds.parent(heatersOne, oven)
    for i in range(2):
        heaterTwo =  cmds.polyCylinder(sx=7, sy=7, h=0.2, r=base_width/1000)
        cmds.move(-base_width/6.0 + i,base_heigh/2.0,base_width/3.5)
        cmds.parent(heaterTwo, oven)
winName = 'Oven'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Oven', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduledown_cuisine.png', label='Oven',width=mainRLWidth[1]*0.5, c=lambda:four())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEGHT', minValue=1, maxValue=10, value=3, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=1, maxValue=10, value=3, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DEPTH', minValue=1, maxValue=10, value=3, width=winWidth/2 )
# slider4 = cmds.intSliderGrp(field=True, label='MODULE WIDTH', minValue=1, maxValue=10, value=4, width=winWidth/2 )
# slider5 = cmds.intSliderGrp(field=True, label='MODULES', minValue=1, maxValue=20, value=3, width=winWidth/2 )