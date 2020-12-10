import maya.cmds as cmds

cmds.file(f=True, new=True)

matela_Widthx = 12        
matela_widthz = 8
matela_Height = 2
lit_extrude_y = 0.8
lit_extrude_Z = 0.85

cmds.group(n = 'lit_complete', em=True)

#matelas
cmds.polyCube(h=matela_Height, w=matela_Widthx, depth=matela_widthz, n='matela')
cmds.polyBevel3('matela',offset=0.1)
cmds.polySmooth('matela', divisions=3)
cmds.parent('matela','lit_complete', relative=True)

#laterales
cmds.polyCube(h=matela_Height, w=matela_Widthx, depth=0.4, n='lateral_lit1_'+str(i))
cmds.move(0,-matela_Height/2.0,-matela_widthz/2.0)
cmds.instance('lateral_lit1_'+str(i))
cmds.move(0,-matela_Height/2.0,matela_widthz/2.0)
cmds.polyBevel3(offset=0.05)
cmds.parent('lateral_lit1_'+str(i),'lit_complete', relative=True)


#tete
cmds.polyCube(h=matela_Height*2.0, w=0.5, depth=matela_widthz, n='tete_lit1')
cmds.move(-matela_Widthx/2.0,0,0)
cmds.polyExtrudeFacet('tete_lit1.f[4]', kft=False, ls=(lit_extrude_Z, lit_extrude_y, 0))
cmds.polyExtrudeFacet('tete_lit1.f[4]', kft=False, ltz=-0.2)
cmds.polyBevel3(offset=0.05)
cmds.parent('tete_lit1','lit_complete', relative=True)


#pieds
cmds.polyCube(h=matela_Height, w=0.4, depth=matela_widthz, n='pieds_lit1')
cmds.move(matela_Widthx/2.0,-matela_Height/2.0,0)
cmds.polyExtrudeFacet('pieds_lit1.f[4]', kft=False, ls=(lit_extrude_Z, lit_extrude_y-0.2, 0))
cmds.polyExtrudeFacet('pieds_lit1.f[4]', kft=False, ltz=-0.2)
cmds.polyBevel3(offset=0.05)
cmds.parent(b,'pieds_lit1','lit_complete', relative=True)


#coussin

cmds.polyCube(h=0.7, w=matela_widthz/3.0, depth=matela_widthz/2.0, n='coussin')
cmds.move(-matela_Widthx/2.0 + 1.8,(matela_Height/2.0)+0.1,(matela_widthz/2.0)/2.0)
cmds.polyBevel3(offset=0.3)
cmds.polySmooth(divisions=2)
cmds.instance('coussin')
cmds.move(-matela_Widthx/2.0 + 1.8,(matela_Height/2.0)+0.1,(-matela_widthz/2.0)/2.0)
cmds.parent('coussin','lit_complete', relative=True)


