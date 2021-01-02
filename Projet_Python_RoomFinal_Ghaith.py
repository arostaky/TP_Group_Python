import maya.cmds as cmds

#Room_Size

WidhSurface = 150
HeightSurface = 3
DepthSurface = 200

#Wall_Size
HeightWall = 50
DepthWall = 5

#Wall_inside_Posirion
Wall_In_1 = 60
Wall_In_2 = 10
Wall_In_3 = 0

#Room_Numbre

RoomNumber = 3

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
                           
                      