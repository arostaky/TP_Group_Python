import maya.cmds as cmds
cmds.file(f=True, new=True)

planche_height = 5
planche_weigth = 0.1
planche_depth = 2
module_weight = 4
number_modules = 3


#group MODULE

cmds.group(n = 'MODULE', em=True)
cmds.group(n = 'MEUBLE_UP', em=True)

#laterales
for i in range(0, 2):
    cmds.polyCube(h=planche_height, w=planche_weigth, depth=planche_depth, n='planche1_'+str(i))
    cmds.polyBevel3(offset=0.02)
    cmds.move(-i*module_weight+module_weight/2.0,planche_height/2.0,0)
    cmds.parent('planche1_'+str(i),'MODULE', relative=True)
#superior - inferior
for i in range(0, 3):
    cmds.polyCube(h=planche_weigth, w=module_weight, depth=planche_depth, n='plancheupdown_'+str(i))
    cmds.polyBevel3(offset=0.02)
    cmds.move(0,i*planche_height/2.0,0)
    cmds.parent('plancheupdown_'+str(i),'MODULE', relative=True)
#puerta
cmds.polyCube(h=planche_height+planche_weigth, w=module_weight+planche_weigth, depth=planche_weigth * 2.0, n='puerta_'+str(i))
cmds.polyBevel3(offset=0.03)
cmds.move(0,planche_height/2.0,planche_depth/2.0+planche_weigth/2.0)
cmds.parent('puerta_'+str(i),'MODULE', relative=True)

#respaldo
cmds.polyCube(h=planche_height+planche_weigth, w=module_weight+planche_weigth, depth=planche_weigth, n='respaldo_'+str(i))
cmds.polyBevel3(offset=0.03)
cmds.move(0,planche_height/2.0,-planche_depth/2.0+planche_weigth/2.0)
cmds.parent('respaldo_'+str(i),'MODULE', relative=True)

         
for i in range(1, number_modules):
       cmds.duplicate('MODULE', n='modules_'+str(i))
       cmds.move(i*(module_weight+planche_weigth),0,0,'modules_'+str(i))
       cmds.parent('modules_'+str(i),'MEUBLE_UP', relative=True)

cmds.parent('MODULE','MEUBLE_UP', relative=True) 