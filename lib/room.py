import maya.cmds as cmds
sc = cmds.internalVar(userScriptDir=True)
def runRoom():

    #Room_Size

    # WidhSurface = 15
    # HeightSurface = 0.3
    # DepthSurface = 20
    WidhSurface = cmds.intSliderGrp(slider1, q=True, value=True)
    HeightSurface = cmds.floatSliderGrp(slider2, q=True, value=True)
    DepthSurface = cmds.intSliderGrp(slider3, q=True, value=True)

    #Wall_Size
    # HeightWall = 5
    # DepthWall = 0.5
    HeightWall = cmds.intSliderGrp(slider4, q=True, value=True)
    DepthWall = cmds.floatSliderGrp(slider5, q=True, value=True)

    #Wall_inside_Posirion
    # i =7
    # y = 1
    # x = -3
    i = cmds.intSliderGrp(slider7, q=True, value=True)
    y = cmds.intSliderGrp(slider8, q=True, value=True)
    x = cmds.intSliderGrp(slider9, q=True, value=True)

    #Room_Numbre

    # RoomNumber = 3
    RoomNumber = cmds.intSliderGrp(slider6, q=True, value=True)


    a = ((DepthSurface/2.0)-(DepthWall/2.0))*-1
    b = (DepthSurface/2.0)-(DepthWall/2.0)
    c = ((WidhSurface/2.0)-(DepthWall/2.0))*-1
    d = (WidhSurface/2.0)-(DepthWall/2.0)

    if RoomNumber == 0:
        cmds.polyCube(h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
        cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
        cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),(DepthSurface/2.0)-(DepthWall/2.0) ,'Wall1')
        cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
        cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),((DepthSurface/2.0)-DepthWall/2.0)*-1.0 ,'Wall2')
        cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
        cmds.move((WidhSurface/2.0)-(DepthWall/2.0),((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall3')
        cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
        cmds.move(((WidhSurface/2.0)-(DepthWall/2.0))*-1.0,((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall4')
    elif RoomNumber == 1:
        if i > a and i < b and y > c and y < d :
            cmds.polyCube(h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),(DepthSurface/2.0)-(DepthWall/2.0) ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),((DepthSurface/2.0)-DepthWall/2.0)*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move((WidhSurface/2.0)-(DepthWall/2.0),((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(((WidhSurface/2.0)-(DepthWall/2.0))*-1.0,((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= ((WidhSurface/2.0)-(DepthWall/2.0))-y, d= DepthWall, name="Wall5" )
            cmds.move(((((WidhSurface/2.0)-(DepthWall/2.0))-y)-DepthWall)/2.0+y,((HeightWall/2.0)+(HeightSurface/2.0)),i,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ((DepthSurface/2.0)-(DepthWall/2.0)+i)-DepthWall, name="Wall6" )
            cmds.move(y,((HeightWall/2.0)+(HeightSurface/2.0)),((((DepthSurface/2.0)-(DepthWall/2.0))*-1)+i)/2.0 ,'Wall6')
                                    
    elif RoomNumber == 2: 
        if i > a and i < b and y > c and y < d :
            cmds.polyCube(h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),(DepthSurface/2.0)-(DepthWall/2.0) ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),((DepthSurface/2.0)-DepthWall/2.0)*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move((WidhSurface/2.0)-(DepthWall/2.0),((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(((WidhSurface/2.0)-(DepthWall/2.0))*-1.0,((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= ((WidhSurface/2.0)-(DepthWall/2.0))-y, d= DepthWall, name="Wall5" )
            cmds.move(((((WidhSurface/2.0)-(DepthWall/2.0))-y)-DepthWall)/2.0+y,((HeightWall/2.0)+(HeightSurface/2.0)),i,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ((DepthSurface/2.0)-(DepthWall/2.0)+i)-DepthWall, name="Wall6" )
            cmds.move(y,((HeightWall/2.0)+(HeightSurface/2.0)),((((DepthSurface/2.0)-(DepthWall/2.0))*-1)+i)/2.0 ,'Wall6')                           
            cmds.polyCube(h= HeightWall, w= DepthWall, d= (DepthSurface-((DepthSurface/2.0)-(DepthWall/2.0)+i)-DepthWall)-(DepthWall), name="Wall7" )
            cmds.move(y,((HeightWall/2.0)+(HeightSurface/2.0)),((((DepthSurface/2.0)-(DepthWall/2.0)))+i)/2.0 ,'Wall7')
    elif RoomNumber == 3: 
        if i > a and i < b and y > c and y < d :
            cmds.polyCube(h= HeightSurface, w= WidhSurface, d=DepthSurface, name="Cube1" ) 
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall1" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),(DepthSurface/2.0)-(DepthWall/2.0) ,'Wall1')
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(DepthWall*2)), d= DepthWall, name="Wall2" )
            cmds.move(0,((HeightWall/2.0)+(HeightSurface/2.0)),((DepthSurface/2.0)-DepthWall/2.0)*-1.0 ,'Wall2')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall3" )
            cmds.move((WidhSurface/2.0)-(DepthWall/2.0),((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall3')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= DepthSurface, name="Wall4" )
            cmds.move(((WidhSurface/2.0)-(DepthWall/2.0))*-1.0,((HeightWall/2.0)+(HeightSurface/2.0)),0 ,'Wall4')
            cmds.polyCube(h= HeightWall, w= ((WidhSurface/2.0)-(DepthWall/2.0))-y, d= DepthWall, name="Wall5" )
            cmds.move(((((WidhSurface/2.0)-(DepthWall/2.0))-y)-DepthWall)/2.0+y,((HeightWall/2.0)+(HeightSurface/2.0)),i,'Wall5')
            cmds.polyCube(h= HeightWall, w= DepthWall, d= ((DepthSurface/2.0)-(DepthWall/2.0)+i)-DepthWall, name="Wall6" )
            cmds.move(y,((HeightWall/2.0)+(HeightSurface/2.0)),((((DepthSurface/2.0)-(DepthWall/2.0))*-1)+i)/2.0 ,'Wall6')                           
            cmds.polyCube(h= HeightWall, w= DepthWall, d= (DepthSurface-((DepthSurface/2.0)-(DepthWall/2.0)+i)-DepthWall)-(DepthWall), name="Wall7" )
            cmds.move(y,((HeightWall/2.0)+(HeightSurface/2.0)),((((DepthSurface/2.0)-(DepthWall/2.0)))+i)/2.0 ,'Wall7')  
            cmds.polyCube(h= HeightWall, w= (WidhSurface-(((WidhSurface/2.0)-(DepthWall/2.0))-y))-(DepthWall*2), d= DepthWall, name="Wall8" )
            cmds.move(((((WidhSurface/2.0)-(DepthWall/2.0))*-1.0)+y)/2.0,((HeightWall/2.0)+(HeightSurface/2.0)),x,'Wall8')


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
slider1 = cmds.intSliderGrp(field=True, label='WIDTH SURFACE', minValue=1, maxValue=20, value=15, width=winWidth/2 )
slider2 = cmds.floatSliderGrp(field=True, label='HEIGHT SURFACE', minValue=0.1, maxValue=20, value=0.3, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='HEIGHT', minValue=1, maxValue=20, value=20, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='EXTRUDE Y', minValue=1, maxValue=2, value=5, width=winWidth/2 )
slider5 = cmds.floatSliderGrp(field=True, label='EXTRUDE Z', minValue=0.1, maxValue=2, value=0.5, width=winWidth/2 )
slider6 = cmds.intSliderGrp(field=True, label='ROOM #', minValue=0, maxValue=3, value=2, width=winWidth/2 ) 
cmds.text(label='Wall Inside Position', font='boldLabelFont')
cmds.text(label='')
slider7 = cmds.intSliderGrp(field=True, label='I #', minValue=0, maxValue=20, value=7, width=winWidth/2 ) 
slider8 = cmds.intSliderGrp(field=True, label='Y #', minValue=0, maxValue=10, value=1, width=winWidth/2 ) 
slider9 = cmds.intSliderGrp(field=True, label='X #', minValue=-10, maxValue=3, value=-3, width=winWidth/2 ) 