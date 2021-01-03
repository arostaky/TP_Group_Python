import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def armoireUp():

    #group MODULE
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    mName = 'MODULE'+ str(mir) + str(crazyR) 
    uName = 'MEUBLE_UP'+ str(mir)+ str(crazyR)
    # planche_height = 5
    # planche_width = 0.1
    # planche_depth = 2
    # module_width = 4
    # number_modules = 3
    planche_height =  cmds.intSliderGrp(slider1, q=True, value=True)
    planche_width =  cmds.floatSliderGrp(slider2, q=True, value=True)
    planche_depth =  cmds.intSliderGrp(slider3, q=True, value=True)
    module_width =  cmds.intSliderGrp(slider4, q=True, value=True)
    number_modules =  cmds.intSliderGrp(slider5, q=True, value=True)

    #group MODULE

    cmds.group(n = mName, em=True)
    cmds.group(n = uName, em=True)

    #laterales
    for i in range(0, 2):
        planche = cmds.polyCube(h=planche_height, w=planche_width, depth=planche_depth)
        cmds.polyBevel3(offset=0.02)
        cmds.move(-i*module_width+module_width/2.0,planche_height/2.0,0)
        cmds.parent(planche,mName, relative=True)
    #superior - inferior
    for i in range(0, 3):
        placheUpDown =  cmds.polyCube(h=planche_width, w=module_width, depth=planche_depth)
        cmds.polyBevel3(offset=0.02)
        cmds.move(0,i*planche_height/2.0,0)
        cmds.parent(placheUpDown, mName, relative=True)
    #puerta
    puerta = cmds.polyCube(h=planche_height+planche_width, w=module_width+planche_width, depth=planche_width * 2.0)
    cmds.polyBevel3(offset=0.03)
    cmds.move(0,planche_height/2.0,planche_depth/2.0+planche_width/2.0)
    cmds.parent(puerta, mName, relative=True)

    #respaldo
    respaldo = cmds.polyCube(h=planche_height+planche_width, w=module_width+planche_width, depth=planche_width)
    cmds.polyBevel3(offset=0.03)
    cmds.move(0,planche_height/2.0,-planche_depth/2.0+planche_width/2.0)
    cmds.parent(respaldo, mName, relative=True)

            
    for i in range(1, number_modules):
        mNameInstance = cmds.instance(mName)
        cmds.move(i*(module_width+planche_width),0,0,mNameInstance)
        cmds.parent(mNameInstance,uName, relative=True)

    cmds.parent(mName,uName, relative=True) 

winName = 'UpperCupboard'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Upper Cupboard', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduleup_cuisine.png', label='Upper Cupboard',width=mainRLWidth[1]*0.5, c=lambda:armoireUp())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEGHT', minValue=1, maxValue=20, value=5, width=winWidth/2 )
slider2 = cmds.floatSliderGrp(field=True, label='WIDTH', minValue=0.01, maxValue=2, value=0.1, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DEPTH', minValue=1, maxValue=20, value=2, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='MODULE WIDTH', minValue=1, maxValue=10, value=4, width=winWidth/2 )
slider5 = cmds.intSliderGrp(field=True, label='MODULES', minValue=1, maxValue=20, value=3, width=winWidth/2 )