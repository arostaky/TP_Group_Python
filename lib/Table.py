import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
def table():
 
    tablewidthz = cmds.intSliderGrp(slider1, q=True, value=True)
    tableWidthx = cmds.intSliderGrp(slider2, q=True, value=True)
    tableHeight = cmds.intSliderGrp(slider3, q=True, value=True)
    #Roundness = cmds.intSliderGrp(slider4, q=True, value=True)
   
    
    #mesa
    cmds.polyCube(h=0.7, w=tableWidthx, depth=tablewidthz, n='table')
    cmds.move(0,tableHeight/2.0-0.3,0)
    cmds.select('table.e[4:5]')
    cmds.select('table.e[8:9]', add=True)
    cmds.polyBevel3(offset=1, segments=3)
    cmds.polyBevel3('table', offset=0.1)
    
    
    #patas
    
    i=1
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table1_')
    cmds.move(-tableWidthx/2.0 + 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table2_')
    cmds.move(tableWidthx/2.0 - 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table3_')
    cmds.move(tableWidthx/2.0 - 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table4_')
    cmds.move(-tableWidthx/2.0 + 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.group('table','p_table1_','p_table2_','p_table3_','p_table4_', n='Table1_'+str(i))

winName = 'Table'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Table', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/table.png', label='Table',width=mainRLWidth[1]*0.5, c=lambda:table())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='TABLE WIDTH Y', minValue=4, maxValue=20, value=10, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='TABLE WIDTH X', minValue=2, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='TABLE HEIGHT', minValue=2, maxValue=20, value=6, width=winWidth/2 )

