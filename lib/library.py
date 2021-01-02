import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
def runLibrary():

    # planche_height = 0.5
    # planche_weigth = 10
    # planche_depth = 3
    # planche_number = 6
    # heigh_between_planches = 2
    planche_height = cmds.floatSliderGrp(slider1, q=True, value=True)
    planche_weigth = cmds.intSliderGrp(slider2, q=True, value=True)
    planche_depth  = cmds.intSliderGrp(slider3, q=True, value=True)
    planche_number =  cmds.intSliderGrp(slider4, q=True, value=True)
    heigh_between_planches = cmds.intSliderGrp(slider5, q=True, value=True)

    #group:
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    gName =  'biblioteque' + str(mir) + str(crazyR)
    cmds.group(n = gName, em=True)

    for i in range(planche_number):
        planche = cmds.polyCube(h=planche_height, w=planche_weigth, depth=planche_depth)
        cmds.polyBevel3(offset=0.05)
        cmds.move(0,i*heigh_between_planches,0)
        cmds.parent(planche,gName, relative=True)
        
    #laterales

    for i in range(0,3):
        planchalateral = cmds.polyCube(h=planche_height, w=planche_number*heigh_between_planches-heigh_between_planches+planche_height, depth=planche_depth)
        cmds.rotate(0,0,'-90deg')
        cmds.move(i*planche_weigth/2-planche_weigth/2.0,((planche_number*heigh_between_planches-heigh_between_planches)-planche_height/2)/2.0,0)
        cmds.polyBevel3(offset=0.05)
        cmds.parent(planchalateral, gName, relative=True)

    #Back    
    back = cmds.polyCube(h=planche_number*heigh_between_planches-heigh_between_planches+planche_height, w=planche_weigth, depth=planche_height, n='back')
    cmds.move(0,((planche_number*heigh_between_planches-heigh_between_planches)-planche_height/2)/2.0,(-planche_depth/2.0)+(planche_height/2.0))
    cmds.polyBevel3(offset=0.05)
    cmds.parent(back, gName, relative=True)

winName = 'Library'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Library', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/biblioteque.png', label='Library',width=mainRLWidth[1]*0.5, c=lambda:runLibrary())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.floatSliderGrp(field=True, label='HEIGHT', minValue=0.1, maxValue=2, value=0.5, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=2, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DEPTH', minValue=2, maxValue=20, value=3, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='PLANCHE #', minValue=2, maxValue=20, value=6, width=winWidth/2 )
slider5 = cmds.intSliderGrp(field=True, label='HEIGHT BTW PLANCES', minValue=2, maxValue=20, value=2, width=winWidth/2 )