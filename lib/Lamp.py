import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def lamp():
    
    # height_lamp = 10    
    # radius_lamp = 4
    # Thickness_lamp = 0.1
    height_lamp = cmds.intSliderGrp(slider1, q=True, value=True)
    radius_lamp = cmds.intSliderGrp(slider2, q=True, value=True)
    Thickness_lamp =  cmds.floatSliderGrp(slider3, q=True, value=True)
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    topLamp = 'TOP_LAMP'+ str(mir) +  str(crazyR)
    lamp = 'LAMP'+ str(mir) +  str(crazyR)
    cmds.group(n=topLamp, em=True)
    cmds.group(n=lamp, em=True)

    # TOP_LAMP
    tLamp = cmds.polyPipe(h=height_lamp, r=radius_lamp, thickness=Thickness_lamp, sh=10, sa=40)

    soporteCentroArriba = cmds.polyCylinder(r=radius_lamp/3.0, h=0.30)

    traversoCentro = cmds.polyCylinder(r=0.08, h=(radius_lamp*2.0)-Thickness_lamp)
    cmds.rotate( 0, 0, '90deg', r=True )
    traversoCentroD = cmds.duplicate(traversoCentro)
    cmds.rotate( 0, '90deg', 0, r=True )

    cmds.parent(tLamp, soporteCentroArriba, traversoCentro, traversoCentroD, topLamp, relative=True )

    cmds.select(topLamp)
    cmds.move(0,height_lamp/5.0,0)

    # CENTRO Y BASE

    soporteCentral = cmds.polyCylinder(r=radius_lamp/12.0, h=height_lamp/1.5)

    soporteBase = cmds.polyCylinder(r=radius_lamp, h=radius_lamp/5.0, sa=40)
    rSoporteBase = cmds.ls(soporteBase)
    cmds.move(0,-height_lamp/3.0,0)
    cmds.polyBevel3(rSoporteBase[0]+'.e[40:79]', rSoporteBase[0]+'.e[0:39]', offset=0.02, segments=3)
    cmds.polySmooth (dv=1)

    decor = cmds.polySphere(r=radius_lamp/12.0)
    cmds.move(0,height_lamp/3.0,0)

    #cmds.parent('TOP_LAMP', 'soportecentral_'+str(i), 'soporteBase', 'decor', 'LAMP', relative=True)
    cmds.parent(topLamp, soporteCentral, soporteBase, decor, lamp, relative=True)   

    

winName = 'Lamp'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Lamp', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/lamp.png', label=' Lamp',width=mainRLWidth[1]*0.5, c=lambda:lamp())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEGHT', minValue=1, maxValue=20, value=10, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=1, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.floatSliderGrp(field=True, label='THICKNESS', minValue=0.1, maxValue=2, value=0.1, width=winWidth/2 )