import maya.cmds as cmds
cmds.file(f=True, new=True)

planche_height = 0.5
planche_weigth = 10
planche_depth = 3
planche_number = 6
heigh_between_planches = 2

#group:
cmds.group(n = 'biblioteque', em=True)

for i in range(planche_number):
    cmds.polyCube(h=planche_height, w=planche_weigth, depth=planche_depth, n='planche1_'+str(i))
    cmds.polyBevel3(offset=0.05)
    cmds.move(0,i*heigh_between_planches,0)
    cmds.parent('planche1_'+str(i),'biblioteque', relative=True)
    
#laterales

for i in range(0,3):
    cmds.polyCube(h=planche_height, w=planche_number*heigh_between_planches-heigh_between_planches+planche_height, depth=planche_depth, n='planchelateral_'+str(i))
    cmds.rotate(0,0,'-90deg')
    cmds.move(i*planche_weigth/2-planche_weigth/2.0,((planche_number*heigh_between_planches-heigh_between_planches)-planche_height/2)/2.0,0)
    cmds.polyBevel3(offset=0.05)
    cmds.parent('planchelateral_'+str(i),'biblioteque', relative=True)

#Back    
cmds.polyCube(h=planche_number*heigh_between_planches-heigh_between_planches+planche_height, w=planche_weigth, depth=planche_height, n='back')
cmds.move(0,((planche_number*heigh_between_planches-heigh_between_planches)-planche_height/2)/2.0,(-planche_depth/2.0)+(planche_height/2.0))
cmds.polyBevel3(offset=0.05)
cmds.parent('back','biblioteque', relative=True)