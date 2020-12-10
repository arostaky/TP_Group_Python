import maya.cmds as cmds

winName = 'Main_Window'
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Forniture Generator')
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.5, winWidth*0.5]
cmds.rowColumnLayout(w=winWidth, numberOfColumns=4, columnWidth=[(1, 140), (2, 140), (3, 140), (4, 140)], rowAttach=(2, 'top', 0))
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate Room',width=mainRLWidth[1]*0.6, c='table()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Generate Chaise',width=mainRLWidth[1]*0.6, c='table()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Lamp-01.png', label='Generate Lamp',width=mainRLWidth[1]*0.6, c='lamp()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comode_icon-01.png', label='Generate Comodore',width=mainRLWidth[1]*0.6, c='table()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/tirroire_icon.png', label='Generate Torroire',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate Bed',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate Gay',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Degenerated People',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate Woman',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate 1',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate 2',width=mainRLWidth[1]*0.6, c='Chaise()')
cmds.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Comin_soon4.png', label='Generate 3',width=mainRLWidth[1]*0.6, c='Chaise()')

cmds.showWindow(winName)
cmds.window(winName, e=True, width=winWidth, height=500)
