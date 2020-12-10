import maya.cmds as cmds

#Room_Size

WidhSurface = 15
HeightSurface = 0.3
DepthSurface = 20

#Wall_Size
HeightWall = 5
DepthWall = 0.5

#Wall_inside_Posirion
i =7
y = 1
x = -3


#Room_Numbre

RoomNumber = 3


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
                           
                      