import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
def runBed():

    # matela_Widthx = 12        
    # matela_widthz = 8
    # matela_Height = 2
    # lit_extrude_y = 0.8
    # lit_extrude_Z = 0.85
    matela_Widthx = cmds.intSliderGrp(slider1, q=True, value=True)
    matela_widthz = cmds.intSliderGrp(slider2, q=True, value=True)
    matela_Height = cmds.intSliderGrp(slider3, q=True, value=True)
    lit_extrude_y = cmds.floatSliderGrp(slider4, q=True, value=True)
    lit_extrude_Z = cmds.floatSliderGrp(slider5, q=True, value=True)
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    gName =  'lit_complete' + str(mir) + str(crazyR)
    cmds.group(n = gName, em=True)

    #matelas
    matela  = cmds.polyCube(h=matela_Height, w=matela_Widthx, depth=matela_widthz)
    cmds.polyBevel3(matela,offset=0.1)
    cmds.polySmooth(matela, divisions=3)
    cmds.parent(matela, gName, relative=True)

    #laterales
    lateralUno = cmds.polyCube(h=matela_Height, w=matela_Widthx, depth=0.4)
    cmds.move(0,-matela_Height/2.0,-matela_widthz/2.0)
    lateralInstance = cmds.instance(lateralUno)
    cmds.move(0,-matela_Height/2.0,matela_widthz/2.0)
    cmds.polyBevel3(offset=0.05)
    cmds.parent(lateralUno, gName, relative=True)
    cmds.parent(lateralInstance, gName, relative=True)


    #tete
    tete = cmds.polyCube(h=matela_Height*2.0, w=0.5, depth=matela_widthz)
    cmds.move(-matela_Widthx/2.0,0,0)
    rtete = cmds.ls(tete)  
    cmds.polyExtrudeFacet(str(rtete[0])+'.f[4]', kft=False, ls=(lit_extrude_Z, lit_extrude_y, 0))
    cmds.polyExtrudeFacet(str(rtete[0])+'.f[4]', kft=False, ltz=-0.2)
    cmds.polyBevel3(offset=0.05)
    cmds.parent(tete, gName, relative=True)


    #pieds
    pied = cmds.polyCube(h=matela_Height, w=0.4, depth=matela_widthz)
    cmds.move(matela_Widthx/2.0,-matela_Height/2.0,0)
    rpied = cmds.ls(pied)
    cmds.polyExtrudeFacet(str(rpied[0])+'.f[4]', kft=False, ls=(lit_extrude_Z, lit_extrude_y-0.2, 0))
    cmds.polyExtrudeFacet(str(rpied[0])+'.f[4]', kft=False, ltz=-0.2)
    cmds.polyBevel3(offset=0.05)
    cmds.parent(pied, gName, relative=True)


    #coussin

    coussin = cmds.polyCube(h=0.7, w=matela_widthz/3.0, depth=matela_widthz/2.0)
    cmds.move(-matela_Widthx/2.0 + 1.8,(matela_Height/2.0)+0.1,(matela_widthz/2.0)/2.0)
    cmds.polyBevel3(offset=0.3)
    cmds.polySmooth(divisions=2)
    coussinInstance = cmds.instance(coussin)
    cmds.move(-matela_Widthx/2.0 + 1.8,(matela_Height/2.0)+0.1,(-matela_widthz/2.0)/2.0)
    cmds.parent(coussin, gName, relative=True)
    cmds.parent(coussinInstance, gName, relative=True)


winName = 'Bed'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Bed', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/lit.png', label='Bed',width=mainRLWidth[1]*0.5, c=lambda:runBed())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='WIDTH X', minValue=1, maxValue=20, value=12, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH Z', minValue=1, maxValue=20, value=8, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='HEIGHT', minValue=1, maxValue=20, value=2, width=winWidth/2 )
slider4 = cmds.floatSliderGrp(field=True, label='EXTRUDE Y', minValue=0.1, maxValue=2, value=0.8, width=winWidth/2 )
slider5 = cmds.floatSliderGrp(field=True, label='EXTRUDE Z', minValue=0.1, maxValue=2, value=0.85, width=winWidth/2 )