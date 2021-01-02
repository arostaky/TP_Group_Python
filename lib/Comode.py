import maya.cmds as cmds 
import random
cmds.file(f=True, new=True)
sc = cmds.internalVar(userScriptDir=True)
def comode():
    
    Counter_H =  cmds.intSliderGrp(slider1, q=True, value=True)
    Counter_W =  cmds.intSliderGrp(slider2, q=True, value=True)
    Counter_d =  cmds.intSliderGrp(slider3, q=True, value=True)
    
    
    #Var Counter_support
    spt_Counter = 0.5
    spt_Counter_W = Counter_W-1.0
    spt_Counter_d = Counter_d-1.0
    offset = 0.5
    
    #Var Tirroire
    seperation = 3
    # nbr_Tiroire = 3
    nbr_Tiroire =  cmds.intSliderGrp(slider4, q=True, value=True)
    
    H_tirroire = 1.0
    W_Tirroire = Counter_W-2.0
    D_Tirroire = 1.0
    
    #var handle
    H_Handle= 0.2
    w_Handle= 0.5
    D_Handle= 0.2
    
    H_topCounter = 1.0
    #top counter

    CounterS = cmds.polyCube(h=spt_Counter ,w= spt_Counter_W, d= spt_Counter_d)
    cmds.polyBevel(CounterS,segments=2,offset=0.01)   
    cmds.move((Counter_W/2.0 % offset) ,offset,(Counter_d/2.0 % offset))
    #counter
    
    Counter = cmds.polyCube(h=Counter_H ,w= Counter_W, d= Counter_d)
    cmds.polyBevel(Counter,segments=2,offset=0.01)
    cmds.move (0,(spt_Counter/2.0+ offset )+(Counter_H/2.0),0)
    
    
    #top counter
    
    TopCounter = cmds.polyCube(h=H_topCounter/2 ,w= Counter_W, d= spt_Counter_d+1.5)
    cmds.polyBevel(TopCounter,segments=2,offset=0.01)   
    cmds.move((Counter_W/2.0 % offset),(Counter_H)+(H_topCounter),(Counter_d/2.0 % offset))
    
    
    #group:
    mir = random.randint(0, 19)
    crazyR = random.randint(0,1000)
    gName = 'Comode'+ str(mir) + str(crazyR)
    cmds.group (CounterS, Counter, TopCounter, n=gName)
    
    #Tiroire  <=======================================La zone des loops
    for t in range(nbr_Tiroire):
        Tirroire = cmds.polyCube(h=H_tirroire ,w= W_Tirroire, d= D_Tirroire)
        cmds.polyBevel(offset=0.01)
        cmds.move((W_Tirroire/Counter_W-offset),(seperation/2.0*(t)+H_tirroire+ offset*2),(Counter_d/2.0- 0.3))
        cmds.parent(Tirroire,gName, relative=True)         #<=============================solution temporaire ?
    
    #Handle
    
    for f in range(nbr_Tiroire):
        Handle = cmds.polyCube(h=H_Handle ,w= w_Handle, d= D_Handle)
        cmds.polyBevel(offset=0.01)
        cmds.move((W_Tirroire/Counter_W-offset),(seperation/2.0*(f)+H_tirroire+ offset*2),(Counter_d/2.0- 0.3+offset))
        cmds.parent(Handle,gName, relative=True)            #<=============================solution temporaire ?
    

winName = 'Comode'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 600 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Comode', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth*0.4, winWidth*0.8]
mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))

cmds.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
# cmds.button(label='runFirst', width=mainRLWidth[1]*0.95, height=70, c='buildVariables()')
cmds.iconTextButton(style='iconAndTextVertical', image1=sc + '/icons/2x/comode.png', label=' Comode',width=mainRLWidth[1]*0.5, c=lambda:comode())
cmds.setParent('..') # this will exit the rowLayout back to the mainRL, same as cmds.setParent(mainRL)

cmds.columnLayout(width=mainRLWidth[1]) # start another vertical layout
slider1 = cmds.intSliderGrp(field=True, label='HEGHT', minValue=1, maxValue=20, value=10, width=winWidth/2 )
slider2 = cmds.intSliderGrp(field=True, label='WIDTH', minValue=1, maxValue=20, value=10, width=winWidth/2 )
slider3 = cmds.intSliderGrp(field=True, label='DISTANCE', minValue=1, maxValue=20, value=3, width=winWidth/2 )
slider4 = cmds.intSliderGrp(field=True, label='DRAWS #', minValue=1, maxValue=20, value=3, width=winWidth/2 )