import maya.cmds as cmds

def runCanape():

    # default values:
    # module1_height = 4
    # module1_weigth = 10
    # module1_depth = 8
    # module1_number = 3

    module1_height = cmds.intSliderGrp(slider1, q=True, value=True)
    module1_weigth = cmds.intSliderGrp(slider2, q=True, value=True)
    module1_depth = cmds.intSliderGrp(slider3, q=True, value=True)
    module1_number = cmds.intSliderGrp(slider4, q=True, value=True)

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

def open():

    winName = 'Canape'
    winWidth = 600 # set a target width and reference this when you specify width
    mainRLWidth = [winWidth*0.4, winWidth*0.4]
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName)
    cmds.window(winName, width=winWidth, title='CANAPE GENERATOR', bgc=(40.0/255.0,35.0/255.0,39.0/255.0))
    cmds.columnLayout()
    cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/2x/canape.png', label='Canape',width=mainRLWidth[1]*0.2, c=lambda:runCanape())
    slider1= cmds.intSliderGrp( field=True, label='HEIGHT', minValue=1, maxValue=20, value=4 )
    slider2= cmds.intSliderGrp( field=True, label='WIDTH', minValue=1, maxValue=20, value=10 )
    slider3= cmds.intSliderGrp( field=True, label='DEPTH', minValue=1, maxValue=20, value=8 )
    slider4= cmds.intSliderGrp( field=True, label='MODULE #', minValue=4, maxValue=6, value=4 )


    #slider8= cmds.intSliderGrp( field=True, label='Base', minValue=-10, maxValue=10, value=-5 )
    cmds.separator(style='none', h=10, w=10)
    cmds.showWindow(winName) 
   