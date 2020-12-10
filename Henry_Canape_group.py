import maya.cmds as cmds
cmds.file(f=True, new=True)

module1_height = 4
module1_weigth = 10
module1_depth = 8
module1_number = 3

cmds.group(n = 'canape', em=True)

for i in range(module1_number):
    cmds.polyCube(h=module1_height, w=module1_weigth, depth=module1_depth, n='module1_'+str(i))
    cmds.move(i*module1_weigth/1.02,0,0)
    cmds.polyBevel3(offset=0.5)
    cmds.polySmooth(divisions=2)
    cmds.parent('module1_'+str(i),'canape', relative=True)
    

#cojines encima

for i in range(module1_number):
    cmds.polyCube(h=module1_height, w=module1_weigth, depth=module1_depth, n='module2_'+str(i))
    cmds.rotate('73deg', 0, 0)
    cmds.move(i*module1_weigth/1.02,module1_depth/1.8,- module1_depth/1.5)
    cmds.polyBevel3(offset=0.5)
    cmds.polySmooth(divisions=2)
    cmds.parent('module2_'+str(i),'canape', relative=True)
    
    
cmds.polyCube(h=(module1_height+module1_depth)/1.5, w=module1_height, depth=module1_depth*1.5, n='lateral1_'+str(i))
cmds.move(-module1_weigth/2.0,0,-0.5)
b=cmds.instance('lateral1_'+str(i))
cmds.move((module1_weigth*module1_number)-(module1_weigth/2.0),0,-0.5)
cmds.polyBevel3(offset=0.5)
cmds.polySmooth(divisions=2)
cmds.parent(b,'lateral1_'+str(i),'canape', relative=True)
    
   
   