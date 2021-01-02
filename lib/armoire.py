import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def armoire():
    
    # planche_height = 5    
    # planche_width = 0.15
    # planche_depth = 4
    # module_width = 4
    # number_modules = 3
    planche_height =  cmds.intSliderGrp(slider1, q=True, value=True)
    planche_width =  cmds.floatSliderGrp(slider2, q=True, value=True)
    planche_depth =  cmds.intSliderGrp(slider3, q=True, value=True)
    module_width =  cmds.intSliderGrp(slider4, q=True, value=True)
    number_modules =  cmds.intSliderGrp(slider5, q=True, value=True)

    #estos dos valores deben ser iguales
    number_tiroir = 3.0
    tiroir = 3



    #group MODULE
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    mName = 'MODULE'+ str(mir) + str(crazyR) 
    tName = 'TIROIR'+ str(mir) + str(crazyR)
    dName = 'MEUBLE_DOWN'+ str(mir)+ str(crazyR)
    cmds.group(n = mName, em=True)
    cmds.group(n = tName, em=True)
    cmds.group(n = dName, em=True)

    #tiroir


    tiroirPorte = cmds.polyCube(h=(planche_height/number_tiroir), w=module_width+planche_width, depth=planche_width * 2.0)
    cmds.polyBevel3(offset=0.03)

    tiroirLat = cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=planche_width, depth=planche_depth)
    cmds.move(-module_width/2.0+planche_width,0,-planche_depth/2.0)
    cmds.polyBevel3(offset=0.02)

    tiroirLatDos = cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=planche_width, depth=planche_depth)
    cmds.move(module_width/2.0-planche_width,0,-planche_depth/2.0)
    cmds.polyBevel3(offset=0.02)

    tiroirBase =  cmds.polyCube(h=planche_width, w=module_width, depth=planche_depth)
    cmds.move(0,(-planche_height/number_tiroir)/4.0,-planche_depth/2.0)
    cmds.polyBevel3(offset=0.02)

    tiroirAtras = cmds.polyCube(h=(planche_height/number_tiroir)/1.5, w=module_width, depth=planche_width)
    cmds.move(0,0,-planche_depth)
    cmds.polyBevel3(offset=0.02)

    # cmds.parent('tiroirporte_'+str(i),'tiroirLat1_'+str(i),'tiroirLat2_'+str(i),'tiroiratras_'+str(i),'tiroirBase_'+str(i),'TIROIR')
    cmds.parent(tiroirPorte, tiroirLat, tiroirLatDos, tiroirAtras, tiroirBase, tName)
    cmds.move(0,(planche_height/number_tiroir)/2.0,planche_depth/2.0, tName)

    for i in range(1, tiroir):
        tNameD = cmds.instance(tName)
        cmds.move(0,i*(planche_height/number_tiroir)+(planche_height/number_tiroir)/2,planche_depth/2.0,tNameD)
        # cmds.parent(tNameD[i],mName, relative=True)
        
    cmds.parent(tName,mName, relative=True)     

    #laterales
    for i in range(0, 2):
        planche = cmds.polyCube(h=planche_height, w=planche_width, depth=planche_depth)
        cmds.polyBevel3(offset=0.02)
        cmds.move(-i*module_width+module_width/2.0,planche_height/2.0,0)
        cmds.parent(planche, mName, relative=True)
    #superior - inferior
    for i in range(0, 2):
        placheUpDown = cmds.polyCube(h=planche_width, w=module_width, depth=planche_depth)
        cmds.polyBevel3(offset=0.02)
        cmds.move(0,i*planche_height,0)
        cmds.parent(placheUpDown,mName, relative=True)

    #respaldo
    respaldo = cmds.polyCube(h=planche_height, w=module_width, depth=planche_width)
    cmds.polyBevel3(offset=0.02)
    cmds.move(0,planche_height/2.0,-planche_depth/2.0)
    cmds.parent(respaldo,mName, relative=True)


    #superior

    plancheSuperior = cmds.polyCube(h=planche_width*2.0, w=module_width*number_modules+planche_width*6.0, depth=planche_depth+1.0)
    cmds.polyBevel3(offset=0.02)
    cmds.move((module_width*number_modules)/2.0-(module_width/2.0)+planche_width,(planche_height)+planche_width*2,0)
    cmds.parent(plancheSuperior,dName, relative=True)




    for i in range(1, number_modules):
        modulesDuplicate = cmds.instance(mName)
        cmds.move(i*(module_width+planche_width),0,0,modulesDuplicate)
        cmds.parent(modulesDuplicate,dName, relative=True)
    
    cmds.parent(mName,dName, relative=True) 

winName = 'Armoire'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Armoire Couisine', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/1x/moduledown_cuisine.png', label=' Armoire',width=mainRLWidth[1]*0.5, c=lambda:armoire())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEGHT', minValue=1, maxValue=20, value=5, width=winWidth/2 )
slider2 = cmds.floatSliderGrp(field=True, label='WIDTH', minValue=0.01, maxValue=2, value=0.15, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DEPTH', minValue=1, maxValue=20, value=4, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=1, maxValue=10, value=4, width=winWidth/2 )
slider5 = cmds.intSliderGrp(field=True, label='MODULES', minValue=1, maxValue=20, value=3, width=winWidth/2 )