import maya.cmds as cmds

def table(f_tablewidthz, f_tableWidthx, f_tableHeight):

    
    tablewidthz = f_tablewidthz
    tableWidthx = f_tableWidthx
    tableHeight = f_tableHeight
    #Roundness = cmds.intSliderGrp(slider4, q=True, value=True)
   
    
    #mesa
    cmds.polyCube(h=0.7, w=tableWidthx, depth=tablewidthz, n='table')
    cmds.move(0,tableHeight/2.0-0.3,0)
    cmds.select('table.e[4:5]')
    cmds.select('table.e[8:9]', add=True)
    cmds.polyBevel3(offset=1, segments=3)
    cmds.polyBevel3('table', offset=0.1)
    
    
    #patas
    
    i=1
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table1_')
    cmds.move(-tableWidthx/2.0 + 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table2_')
    cmds.move(tableWidthx/2.0 - 1,0,tablewidthz/2.0 - 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table3_')
    cmds.move(tableWidthx/2.0 - 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=tableHeight, w=1, depth=1, n='p_table4_')
    cmds.move(-tableWidthx/2.0 + 1,0,-tablewidthz/2.0 + 1)
    cmds.polyBevel(offset=0.1)
    
    cmds.group('table','p_table1_','p_table2_','p_table3_','p_table4_', n='Table1_'+str(i))
    

def Chaise(f_Chaisewidthz, f_ChaiseWidthx, f_ChaiseHeight, f_Distance):
    
    
    Chaisewidthz = f_Chaisewidthz
    ChaiseWidthx = f_ChaiseWidthx
    ChaiseHeight = f_ChaiseHeight
    Distance = f_Distance
    
    #mesa
    cmds.polyCube(h=1, w=ChaiseWidthx, depth=Chaisewidthz, n='Chaise')
    cmds.move(0,ChaiseHeight/2.0-0.3,0)
    cmds.polyBevel(offset=0.2)
    cmds.polySmooth (dv=1)
    
    
    #patas
    
    cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7, n='pata1')
    cmds.move(-ChaiseWidthx/2.0 + 0.5,0,Chaisewidthz/2.0 - 0.5)
    cmds.rotate(-4,0,-4)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7, n='pata2')
    cmds.move(ChaiseWidthx/2.0 - 0.5,0,Chaisewidthz/2.0 - 0.5)
    cmds.rotate(-4,0,4)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7, n='pata3')
    cmds.move(ChaiseWidthx/2.0 - 0.5,0,-Chaisewidthz/2.0 + 0.5)
    cmds.rotate(4,0,4)
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=ChaiseHeight, w=0.7, depth=0.7, n='pata4')
    cmds.move(-ChaiseWidthx/2.0 + 0.5,0,-Chaisewidthz/2.0 + 0.5)
    cmds.rotate(4,0,-4)
    cmds.polyBevel(offset=0.1)
    
    #espaldar
    
    cmds.polyCube(h=ChaiseHeight, w=0.5, depth=0.5, n='Espaldar_1')
    cmds.move(-ChaiseWidthx/2.0 + 0.2,ChaiseHeight,Chaisewidthz/2.0 - 1)
    cmds.rotate(0,0,7)    
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=ChaiseHeight, w=0.5, depth=0.5, n='Espaldar_2')
    cmds.move(-ChaiseWidthx/2.0 + 0.2,ChaiseHeight,-Chaisewidthz/2.0 + 1)
    cmds.rotate(0,0,7) 
    cmds.polyBevel(offset=0.1)
    
    cmds.polyCube(h=2.5, w=1, depth=Chaisewidthz, n='Espaldar_3')
    cmds.move(-ChaiseWidthx/2.0 + 0.5,ChaiseHeight*1.4,0)
    cmds.rotate(0,0,7)
    cmds.polyBevel(offset=0.2)
    cmds.polySmooth (dv=1)
    cmds.group('Chaise','pata1','pata2','pata3','pata4', 'Espaldar_1','Espaldar_2','Espaldar_3', n='Chaise1')


    cmds.select('Chaise1')
    cmds.move(Distance,-1,0)
    cmds.duplicate('Chaise1')
    cmds.move(-Distance,-1,0)
    cmds.rotate(0,-180,0)
    
    cmds.select('Chaise1')
    cmds.duplicate('Chaise1')
    cmds.move(0,-1,-Distance)
    cmds.rotate(0,90,0)
    
    cmds.select('Chaise1')
    cmds.duplicate('Chaise1')
    cmds.move(0,-1,Distance)
    cmds.rotate(0,-90,0)
    
#def Base():
    
    #Base = cmds.intSliderGrp(slider8, q=True, value=True)

    #Base
    #cmds.polyCube(h=1, w=tableWidthx*2, depth=tablewidthz*2, n='Base')
    #cmds.move(0,-tableHeight/2.0-0.3,0)
    #cmds.select('Base.e[4:5]')
    #cmds.select('Base.e[8:9]', add=True)
    #cmds.polyBevel3(offset=1, segments=3)
    #cmds.polyBevel3('Base', offset=0.1)
    
    
    
# cmds.window(title = 'table')
# cmds.columnLayout()
# slider1= cmds.intSliderGrp( field=True, label='tablewidthz', minValue=4, maxValue=20, value=10 )
# slider2= cmds.intSliderGrp( field=True, label='tableWidthx', minValue=2, maxValue=20, value=10 )
# slider3= cmds.intSliderGrp( field=True, label='tableHeight', minValue=2, maxValue=20, value=6 )

# slider4= cmds.intSliderGrp( field=True, label='Chaisewidthz', minValue=4, maxValue=6, value=4 )
# slider5= cmds.intSliderGrp( field=True, label='ChaiseWidthx', minValue=2, maxValue=6, value=5 )
# slider6= cmds.intSliderGrp( field=True, label='ChaiseHeight', minValue=2, maxValue=10, value=4 )
# slider7= cmds.intSliderGrp( field=True, label='Distance', minValue=-10, maxValue=10, value=-5 )

# #slider8= cmds.intSliderGrp( field=True, label='Base', minValue=-10, maxValue=10, value=-5 )



# cmds.button(label = 'Create Table', c='table()')
# cmds.button(label = 'Create Chaise', c='Chaise()')
# cmds.button(label = 'Base', c='Base()')
# cmds.separator(style='none', h=10, w=10)
# cmds.showWindow() 