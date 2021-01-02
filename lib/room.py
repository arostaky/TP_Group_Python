import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
def runRoom():
    #Room_Size

    # WidhSurface = 150
    # HeightSurface = 3
    # DepthSurface = 200
    WidhSurface = cmds.intSliderGrp(slider1, q=True, value=True)
    HeightSurface = cmds.floatSliderGrp(slider2, q=True, value=True)
    DepthSurface = cmds.intSliderGrp(slider3, q=True, value=True)
    #Wall_Size
    # HeightWall = 50
    # DepthWall = 5
    HeightWall = cmds.intSliderGrp(slider4, q=True, value=True)
    DepthWall = cmds.floatSliderGrp(slider5, q=True, value=True)
    #Wall_inside_Posirion
    # Wall_In_1 = 60
    # Wall_In_2 = 10
    # Wall_In_3 = 0
    Wall_In_1 = cmds.intSliderGrp(slider7, q=True, value=True)
    Wall_In_2 = cmds.intSliderGrp(slider8, q=True, value=True)
    Wall_In_3 = cmds.intSliderGrp(slider9, q=True, value=True)
    #Room_Numbre

    # RoomNumber = 3
    RoomNumber = cmds.intSliderGrp(slider6, q=True, value=True)
    #Optimization
    Wall1_Op_01 = ((HeightWall/2.0)+(HeightSurface/2.0))
    Wall1_Op_02 = (DepthSurface/2.0)-(DepthWall/2.0)
    Wall3_Op_01 = (WidhSurface/2.0)-(DepthWall/2.0)
    Wall4_Op_01 = ((HeightWall/2.0)+(HeightSurface/2.0))


    a =  Wall1_Op_02*-1
    b =  Wall1_Op_02
    c =  Wall1_Op_02*-1
    d =  Wall3_Op_01


    if RoomNumber == 0:
        cmds.polyCube(sx=15, sz=15, h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
        cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
        cmds.move(0,Wall1_Op_01,Wall1_Op_02 ,'Wall1')
        cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
        cmds.move(0,Wall1_Op_01,Wall1_Op_02*-1.0 ,'Wall2')
        cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
        cmds.move(Wall3_Op_01,Wall1_Op_01,0 ,'Wall3')
        cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
        cmds.move(Wall3_Op_01*-1.0,Wall4_Op_01,0 ,'Wall4')
        cmds.group( 'Cube1', 'Wall1', 'Wall2', 'Wall3', 'Wall4', n='Room' )
    elif RoomNumber == 1:
        if Wall_In_1 > a and Wall_In_1 < b and Wall_In_2 > c and Wall_In_2 < d :
            cmds.polyCube(sx=15, sz=15, h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02 ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move(Wall3_Op_01,Wall1_Op_01,0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(Wall3_Op_01*-1.0,Wall4_Op_01,0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= Wall3_Op_01-Wall_In_2, d= DepthWall, name="Wall5" )
            cmds.move(((Wall3_Op_01-Wall_In_2)-DepthWall)/2.0+Wall_In_2,Wall4_Op_01,Wall_In_1,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ( Wall1_Op_02 + Wall_In_1 )-DepthWall, name="Wall6" )
            cmds.move(Wall_In_2,Wall4_Op_01,((Wall1_Op_02*-1)+ Wall_In_1)/2.0 ,'Wall6')
            cmds.group( 'Cube1', 'Wall1', 'Wall2', 'Wall3', 'Wall4', 'Wall5', 'Wall6', n='Room' )                         
    elif RoomNumber == 2: 
        if Wall_In_1 > a and Wall_In_1 < b and Wall_In_2 > c and Wall_In_2 < d :
            cmds.polyCube(sx=15, sz=15, h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" )
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02 ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move(Wall3_Op_01,Wall1_Op_01,0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(Wall3_Op_01*-1.0,Wall4_Op_01,0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= Wall3_Op_01-Wall_In_2, d= DepthWall, name="Wall5" )
            cmds.move(((Wall3_Op_01-Wall_In_2)-DepthWall)/2.0+Wall_In_2,Wall4_Op_01,Wall_In_1,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ( Wall1_Op_02 + Wall_In_1 )-DepthWall, name="Wall6" )
            cmds.move(Wall_In_2,Wall4_Op_01,((Wall1_Op_02*-1)+ Wall_In_1)/2.0 ,'Wall6')                     
            cmds.polyCube(h= HeightWall, w= DepthWall, d= (DepthSurface-(Wall1_Op_02+Wall_In_1)-DepthWall)-(DepthWall), name="Wall7" )
            cmds.move(Wall_In_2,Wall4_Op_01 ,(Wall1_Op_02+Wall_In_1)/2.0 ,'Wall7')
            cmds.group( 'Cube1', 'Wall1', 'Wall2', 'Wall3', 'Wall4', 'Wall5', 'Wall6','Wall7', n='Room' )                         
    elif RoomNumber == 3: 
        if Wall_In_1 > a and Wall_In_1 < b and Wall_In_2 > c and Wall_In_2 < d and Wall_In_3 > a and Wall_In_3 < b :
            cmds.polyCube(sx=15, sz=15, h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" )
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02 ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,Wall1_Op_01,Wall1_Op_02*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move(Wall3_Op_01,Wall1_Op_01,0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(Wall3_Op_01*-1.0,Wall4_Op_01,0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= Wall3_Op_01-Wall_In_2, d= DepthWall, name="Wall5" )
            cmds.move(((Wall3_Op_01-Wall_In_2)-DepthWall)/2.0+Wall_In_2,Wall4_Op_01,Wall_In_1,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ( Wall1_Op_02 + Wall_In_1 )-DepthWall, name="Wall6" )
            cmds.move(Wall_In_2,Wall4_Op_01,((Wall1_Op_02*-1)+ Wall_In_1)/2.0 ,'Wall6')                        
            cmds.polyCube(h= HeightWall, w= DepthWall, d= (DepthSurface-(Wall1_Op_02+Wall_In_1)-DepthWall)-(DepthWall), name="Wall7" )
            cmds.move(Wall_In_2,Wall4_Op_01 ,(Wall1_Op_02+Wall_In_1)/2.0 ,'Wall7')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(Wall3_Op_01-Wall_In_2))-(DepthWall*2), d= DepthWall, name="Wall8" )
            cmds.move(((Wall3_Op_01*-1.0)+Wall_In_2)/2.0,Wall4_Op_01,Wall_In_3,'Wall8')
            cmds.group( 'Cube1', 'Wall1', 'Wall2', 'Wall3', 'Wall4', 'Wall5', 'Wall6','Wall7', 'Wall8', n='Room' )  

winName = 'Room'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Room', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/biblioteque.png', label='Room',width=mainRLWidth[1]*0.5, c=lambda:runRoom())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='WIDTH SURFACE', minValue=1, maxValue=300, value=150, width=winWidth/2 )
slider2 = cmds.floatSliderGrp(field=True, label='HEIGHT SURFACE', minValue=1, maxValue=20, value=3, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='HEIGHT', minValue=1, maxValue=400, value=200, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='EXTRUDE Y', minValue=1, maxValue=100, value=50, width=winWidth/2 )
slider5 = cmds.floatSliderGrp(field=True, label='EXTRUDE Z', minValue=0.1, maxValue=10, value=5, width=winWidth/2 )

slider6 = cmds.intSliderGrp(field=True, label='ROOM #', minValue=0, maxValue=3, value=2, width=winWidth/2 ) 
cmds.text(label='Walls Inside Position', font='boldLabelFont')
cmds.text(label='')
slider7 = cmds.intSliderGrp(field=True, label='Room # 1: ', minValue=0, maxValue=120, value=60, width=winWidth/2 ) 
slider8 = cmds.intSliderGrp(field=True, label='Room # 2: ', minValue=0, maxValue=120, value=10, width=winWidth/2 ) 
slider9 = cmds.intSliderGrp(field=True, label='Room # 3: ', minValue=0, maxValue=120, value=5, width=winWidth/2 ) 