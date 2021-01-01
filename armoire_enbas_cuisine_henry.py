import maya.cmds as cmds
cmds.file(f=True, new=True)

planche_height = 5    
planche_weigth = 0.15
planche_depth = 4
module_weight = 4
number_modules = 3

#estos dos valores deben ser iguales
number_tiroir = 3.0
tiroir = 3



#group MODULE

cmds.group(n = 'MODULE', em=True)
cmds.group(n = 'TIROIR', em=True)
cmds.group(n = 'MEUBLE_DOWN', em=True)

#tiroir


cmds.polyCube(h=(planche_height/number_tiroir), w=module_weight+planche_weigth, depth=planche_weigth * 2.0, n='tiroirporte_'+str(i))
cmds.polyBevel3(offset=0.03)

cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=planche_weigth, depth=planche_depth, n='tiroirLat1_'+str(i))
cmds.move(-module_weight/2.0+planche_weigth,0,-planche_depth/2.0)
cmds.polyBevel3(offset=0.02)

cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=planche_weigth, depth=planche_depth, n='tiroirLat2_'+str(i))
cmds.move(module_weight/2.0-planche_weigth,0,-planche_depth/2.0)
cmds.polyBevel3(offset=0.02)

cmds.polyCube(h=planche_weigth, w=module_weight, depth=planche_depth, n='tiroirBase_'+str(i))
cmds.move(0,(-planche_height/number_tiroir)/4.0,-planche_depth/2.0)
cmds.polyBevel3(offset=0.02)

cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=module_weight, depth=planche_weigth, n='tiroiratras_'+str(i))
cmds.move(0,0,-planche_depth)
cmds.polyBevel3(offset=0.02)

cmds.parent('tiroirporte_'+str(i),'tiroirLat1_'+str(i),'tiroirLat2_'+str(i),'tiroiratras_'+str(i),'tiroirBase_'+str(i),'TIROIR')
cmds.move(0,(planche_height/number_tiroir)/2.0,planche_depth/2.0, 'TIROIR')

for i in range(1, tiroir):
    cmds.duplicate('TIROIR', n='TIROIRs_'+str(i))
    cmds.move(0,i*(planche_height/number_tiroir)+(planche_height/number_tiroir)/2,planche_depth/2.0,'TIROIRs_'+str(i))
    
    cmds.parent('TIROIRs_'+str(i),'MODULE', relative=True)
    
cmds.parent('TIROIR','MODULE', relative=True)     

#laterales
for i in range(0, 2):
    cmds.polyCube(h=planche_height, w=planche_weigth, depth=planche_depth, n='planche1_'+str(i))
    cmds.polyBevel3(offset=0.02)
    cmds.move(-i*module_weight+module_weight/2.0,planche_height/2.0,0)
    cmds.parent('planche1_'+str(i),'MODULE', relative=True)
#superior - inferior
for i in range(0, 2):
    cmds.polyCube(h=planche_weigth, w=module_weight, depth=planche_depth, n='plancheupdown_'+str(i))
    cmds.polyBevel3(offset=0.02)
    cmds.move(0,i*planche_height,0)
    cmds.parent('plancheupdown_'+str(i),'MODULE', relative=True)

#respaldo
cmds.polyCube(h=planche_height, w=module_weight, depth=planche_weigth, n='respaldo_'+str(i))
cmds.polyBevel3(offset=0.02)
cmds.move(0,planche_height/2.0,-planche_depth/2.0)
cmds.parent('respaldo_'+str(i),'MODULE', relative=True)


#superior

cmds.polyCube(h=planche_weigth*2.0, w=module_weight*number_modules+planche_weigth*6.0, depth=planche_depth+1.0, n='planchesuperior_'+str(i))
cmds.polyBevel3(offset=0.02)
cmds.move((module_weight*number_modules)/2.0-(module_weight/2.0)+planche_weigth,(planche_height)+planche_weigth*2,0)
cmds.parent('planchesuperior_'+str(i),'MEUBLE_DOWN', relative=True)




for i in range(1, number_modules):
       cmds.duplicate('MODULE', n='modules_'+str(i))
       cmds.move(i*(module_weight+planche_weigth),0,0,'modules_'+str(i))
       cmds.parent('modules_'+str(i),'MEUBLE_DOWN', relative=True)

cmds.parent('MODULE','MEUBLE_DOWN', relative=True) 