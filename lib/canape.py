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



winName = 'Canape'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Canape', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/2x/canape.png', label='Canape',width=mainRLWidth[1]*0.5, c=lambda:runCanape())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEIGHT', minValue=1, maxValue=20, value=4, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=1, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DEPTH', minValue=1, maxValue=20, value=8, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='MODULE #', minValue=1, maxValue=20, value=3, width=winWidth/2 )