import maya.cmds as cmds
import random
sc = cmds.internalVar(userScriptDir=True)
def tableChaise():
 
    tablewidthz = cmds.intSliderGrp(slider1, q=True, value=True)
    tableWidthx = cmds.intSliderGrp(slider2, q=True, value=True)
    tableHeight = cmds.intSliderGrp(slider3, q=True, value=True)
    #Roundness = cmds.intSliderGrp(slider4, q=True, value=True)
   
    
    #mesa
    table = cmds.polyCube(h=0.7, w=tableWidthx, depth=tablewidthz)
    rtable = cmds.ls(table[0])
    print(rtable)
    cmds.move(0,tableHeight/2.0-0.3,0)
    cmds.select(str(rtable[0])+'.e[4:5]')
    cmds.select(str(rtable[0])+'.e[8:9]', add=True)
    # cmds.select('table.e[4:5]')
    # cmds.select('table.e[8:9]', add=True)
    cmds.polyBevel3(offset=1, segments=3)
    cmds.polyBevel3(rtable[0], offset=0.1)
    
    
    #patas
    
    pataUno = cmds.polyCube(h=tableHeight, w=1, depth=1)
    cmds.move(-tableWidthx/2.0 + 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    pataDos = cmds.polyCube(h=tableHeight, w=1, depth=1)
    cmds.move(tableWidthx/2.0 - 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    pataTres = cmds.polyCube(h=tableHeight, w=1, depth=1)
    cmds.move(tableWidthx/2.0 - 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    
    pataCuatro = cmds.polyCube(h=tableHeight, w=1, depth=1)
    cmds.move(-tableWidthx/2.0 + 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    tName = 'Table'+ str(mir) + str(crazyR)
    cmds.group(table,pataUno, pataDos, pataTres, pataCuatro, n=tName)
    
    Chaisewidthz = cmds.intSliderGrp(slider4, q=True, value=True)
    ChaiseWidthx = cmds.intSliderGrp(slider5, q=True, value=True)
    ChaiseHeight = cmds.intSliderGrp(slider6, q=True, value=True)
    Distance = cmds.intSliderGrp(slider7, q=True, value=True)
    
    mainC = cmds.polyCube(h=1, w=ChaiseWidthx, depth=Chaisewidthz)
    cmds.move(0,ChaiseHeight/2.0-0.3,0)
    cmds.polyBevel(offset=0.2)
    cmds.polySmooth (dv=1)
    
    
    #patas
    
    pataUno = cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7)
    cmds.move(-ChaiseWidthx/2.0 + 0.5,0,Chaisewidthz/2.0 - 0.5)
    cmds.rotate(-4,0,-4)
    cmds.polyBevel(offset=0.1)
    
    pataDos = cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7)
    cmds.move(ChaiseWidthx/2.0 - 0.5,0,Chaisewidthz/2.0 - 0.5)
    cmds.rotate(-4,0,4)
    cmds.polyBevel(offset=0.1)
    
    pataTres = cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7)
    cmds.move(ChaiseWidthx/2.0 - 0.5,0,-Chaisewidthz/2.0 + 0.5)
    cmds.rotate(4,0,4)
    cmds.polyBevel(offset=0.1)
    
    pataCuatro = cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7)
    cmds.move(-ChaiseWidthx/2.0 + 0.5,0,-Chaisewidthz/2.0 + 0.5)
    cmds.rotate(4,0,-4)
    cmds.polyBevel(offset=0.1)
    
    #espaldar
    
    e_uno = cmds.polyCube(h=ChaiseHeight, w=0.5, depth=0.5)
    cmds.move(-ChaiseWidthx/2.0 + 0.2,ChaiseHeight,Chaisewidthz/2.0 - 1)
    cmds.rotate(0,0,7)    
    cmds.polyBevel(offset=0.1)
    
    e_dos = cmds.polyCube(h=ChaiseHeight, w=0.5, depth=0.5)
    cmds.move(-ChaiseWidthx/2.0 + 0.2,ChaiseHeight,-Chaisewidthz/2.0 + 1)
    cmds.rotate(0,0,7) 
    cmds.polyBevel(offset=0.1)
    
    e_tres = cmds.polyCube(h=2.5, w=1, depth=Chaisewidthz)
    cmds.move(-ChaiseWidthx/2.0 + 0.5,ChaiseHeight*1.4,0)
    cmds.rotate(0,0,7)
    cmds.polyBevel(offset=0.2)
    cmds.polySmooth (dv=1)
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    rName = 'Chair'+ str(mir) + str(crazyR)
    cmds.group(mainC,pataUno, pataDos, pataTres, pataCuatro, e_uno, e_dos, e_tres, n=rName)


    cmds.select(rName)
    cmds.move(Distance,-1,0)
    cmds.duplicate(rName)
    cmds.move(-Distance,-1,0)
    cmds.rotate(0,-180,0)
    
    cmds.select(rName)
    cmds.duplicate(rName)
    cmds.move(0,-1,-Distance)
    cmds.rotate(0,90,0)
    
    cmds.select(rName)
    cmds.duplicate(rName)
    cmds.move(0,-1,Distance)
    cmds.rotate(0,-90,0)
    


# def buildVariables():
#     #def variables?
#     tablewidthz = cmds.intSliderGrp("slider1", q=True, value=True)
#     tableWidthx = cmds.intSliderGrp("slider2", q=True, value=True)
#     tableHeight = cmds.intSliderGrp("slider3", q=True, value=True)
#     Chaisewidthz = cmds.intSliderGrp("slider4", q=True, value=True)
#     ChaiseWidthx = cmds.intSliderGrp("slider5", q=True, value=True)
#     ChaiseHeight = cmds.intSliderGrp("slider6", q=True, value=True)
#     Distance = cmds.intSliderGrp("slider7", q=True, value=True)
#     print tablewidthz, tableWidthx, tableHeight, Chaisewidthz, ChaiseWidthx, ChaiseHeight, Distance

winName = 'TableChaise'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Table and Chair', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/table_chaise.png', label='Table and Chair',width=mainRLWidth[1]*0.5, c=lambda:tableChaise())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
cmds.text(label='Table', font='boldLabelFont')
cmds.text(label='')
slider1 = cmds.intSliderGrp(field=True, label='TABLE WIDTH Y', minValue=4, maxValue=20, value=10, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='TABLE WIDTH X', minValue=2, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='TABLE HEIGHT', minValue=2, maxValue=20, value=6, width=winWidth/2 )
#-------------------------------------------------------------------------------------------------------------------
cmds.text(label='')
cmds.text(label='Chaise:', font='boldLabelFont')
slider4 = cmds.intSliderGrp(field=True, label='CHAISE WIDTH Z', minValue=4, maxValue=6, value=4, width=winWidth/2 )
slider5 = cmds.intSliderGrp(field=True, label='CHAISE WIDTH X', minValue=2, maxValue=6, value=5, width=winWidth/2 )
slider6 = cmds.intSliderGrp(field=True, label='CHAISE HEIGHT', minValue=2, maxValue=10, value=4, width=winWidth/2 )
slider7 = cmds.intSliderGrp(field=True, label='DISTANCE', minValue=-10, maxValue=10, value=-5, width=winWidth/2 )
