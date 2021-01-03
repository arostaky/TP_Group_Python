import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def tv():

    #group MODULE
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    tvBase = 'TvBase'+ str(mir) + str(crazyR) 
    tv = 'Tv'+ str(mir) + str(crazyR)
    cmds.group(n = tvBase, em=True)
    cmds.group(n = tv, em=True)
    base_heigh = 0.5 
    base_width = 4
    stick_height = 2
    tv_width = cmds.intSliderGrp(slider4, q=True, value=True)

    #base:
    base = cmds.polyCube(h=base_heigh, w=base_width, depth=2)
    cmds.polyBevel3(base,offset=0.1)
    stick = cmds.polyCube(h=stick_height, w=base_width/2, depth=0.5)
    # cmds.move(0,base_heigh/2,base_width/4)
    cmds.select(base, stick)
    cmds.align(x='mid',y='dist', atl=True)
    cmds.parent(base, stick, tvBase)
    #tv screen:
    screen = cmds.polyCube(h=tv_width/2, w=tv_width, depth=0.2)
    cmds.polyBevel3(screen,offset=0.02)
    cmds.select(base, screen)
    cmds.align(y='stack',  atl=True)
    cmds.select(stick, screen)
    cmds.align(y='stack',  atl=True)
    # cmds.move(0,-base_heigh/20.0,-base_width/10.0)
    cmds.parent(tvBase, screen, tv)
winName = 'TV'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='TV', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduledown_cuisine.png', label='tv',width=mainRLWidth[1]*0.5, c=lambda:tv())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
# slider1 = cmds.intSliderGrp(field=True, label='BASE HEGHT', minValue=1, maxValue=10, value=3, width=winWidth/2 )
# slider2 = cmds.intSliderGrp(field=True, label='BASE WIDTH', minValue=1, maxValue=10, value=3, width=winWidth/2 )
# slider3 = cmds.intSliderGrp(field=True, label='STICK HEIGHT', minValue=1, maxValue=10, value=2, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='TV SIZE', minValue=5, maxValue=20, value=10, width=winWidth/2 )
# slider4 = cmds.intSliderGrp(field=True, label='MODULE WIDTH', minValue=1, maxValue=10, value=4, width=winWidth/2 )
# slider5 = cmds.intSliderGrp(field=True, label='MODULES', minValue=1, maxValue=20, value=3, width=winWidth/2 )