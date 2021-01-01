import maya.cmds as cmds
cmds.file(f=True, new=True)

height_lamp = 10    
radius_lamp = 4
Thickness_lamp = 0.1


cmds.group(n = 'TOP_LAMP', em=True)
cmds.group(n = 'LAMP', em=True)

# TOP_LAMP
cmds.polyPipe(h=height_lamp, r=radius_lamp, thickness=Thickness_lamp, sh=10, sa=40, n='lamp_'+str(i))

cmds.polyCylinder(r=radius_lamp/3.0, h=0.30, n='soportecentroarriba_'+str(i))

cmds.polyCylinder(r=0.08, h=(radius_lamp*2.0)-Thickness_lamp, n='traversocentro1')
cmds.rotate( 0, 0, '90deg', r=True )
cmds.duplicate('traversocentro1', n='traversos_'+str(i))
cmds.rotate( 0, '90deg', 0, r=True )

cmds.parent('lamp_' +str(i), 'soportecentroarriba_'+str(i),'traversocentro1', 'traversos_'+str(i), 'TOP_LAMP', relative=True )

cmds.select('TOP_LAMP')
cmds.move(0,height_lamp/5.0,0)

# CENTRO Y BASE

cmds.polyCylinder(r=radius_lamp/12.0, h=height_lamp/1.5, n='soportecentral_'+str(i))

cmds.polyCylinder(r=radius_lamp, h=radius_lamp/5.0, sa=40, n='soporteBase')
cmds.move(0,-height_lamp/3.0,0)
cmds.polyBevel3('soporteBase.e[40:79]', 'soporteBase.e[0:39]', offset=0.02, segments=3)
cmds.polySmooth (dv=1)

cmds.polySphere(r=radius_lamp/12.0, n='decor')
cmds.move(0,height_lamp/3.0,0)

cmds.parent('TOP_LAMP', 'soportecentral_'+str(i), 'soporteBase', 'decor', 'LAMP', relative=True)   

#, 'lamp.e[720:759]', 'lamp.e[640:679]','lamp.e[560:599]','lamp.e[480:519]' )