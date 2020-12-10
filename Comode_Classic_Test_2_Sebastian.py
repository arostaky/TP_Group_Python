import maya.cmds as cmds 
cmds.file(f=True, new=True)

 
#Var Counter



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
    nbr_Tiroire = 3
    
    H_tirroire = 1.0
    W_Tirroire = Counter_W-2.0
    D_Tirroire = 1.0
    
    #var handle
    H_Handle= 0.2
    w_Handle= 0.5
    D_Handle= 0.2
    
    H_topCounter = 1.0
    #top counter

    cmds.polyCube(h=spt_Counter ,w= spt_Counter_W, d= spt_Counter_d , n= "Counter_support")
    cmds.polyBevel("Counter_support",segments=2,offset=0.01)   
    cmds.move ( (Counter_W/2.0 % offset) ,offset,(Counter_d/2.0 % offset))
    #counter
    
    cmds.polyCube(h=Counter_H ,w= Counter_W, d= Counter_d , n= "Counter_")
    cmds.polyBevel("Counter_",segments=2,offset=0.01)
    cmds.move ( 0,(spt_Counter/2.0+ offset )+(Counter_H/2.0),0)
    
    
    #top counter
    
    cmds.polyCube(h=H_topCounter/2 ,w= Counter_W, d= spt_Counter_d+1.5, n= "Top_counter_")
    cmds.polyBevel("Top_counter_",segments=2,offset=0.01)   
    cmds.move ( (Counter_W/2.0 % offset) ,(Counter_H)+(H_topCounter),(Counter_d/2.0 % offset))
    
    
    #group:
    cmds.group ("Top_counter_","Counter_","Counter_support", name= "Comode")
    
    #Tiroire  <=======================================La zone des loops
    for t in range(nbr_Tiroire  ):
        cmds.polyCube(h=H_tirroire ,w= W_Tirroire, d= D_Tirroire , n= "Tirroire_"+str(t))
        cmds.polyBevel("Tirroire_"+str(t),offset=0.01)
        cmds.move ((W_Tirroire/Counter_W-offset),(seperation/2.0*(t)+H_tirroire+ offset*2),(Counter_d/2.0- 0.3))
        cmds.parent('Tirroire_'+str(t),'Comode', relative=True)         #<=============================solution temporaire ?
    #Handle
    
    for f in range(nbr_Tiroire ):
        cmds.polyCube(h=H_Handle ,w= w_Handle, d= D_Handle , n= "Handle_"+str(f))
        cmds.polyBevel("Handle_"+str(f),offset=0.01)
        cmds.move ((W_Tirroire/Counter_W-offset),(seperation/2.0*(f)+H_tirroire+ offset*2),(Counter_d/2.0- 0.3+offset))
        cmds.parent('Handle_'+str(f),'Comode', relative=True)            #<=============================solution temporaire ?
    
    #cmds.group ("Tirroire_","Handle_","Top_counter_","Counter_","Counter_support", name= "Comode") <===========================ne marche pas


ram = cmds.window( "comodeGen",t = "Comode generator",)

cmds.columnLayout(adj = True)
slider1= cmds.intSliderGrp( field=True, label='Counter_H', minValue=1, maxValue=20, value=10 )
slider2= cmds.intSliderGrp( field=True, label='Counter_W', minValue=1, maxValue=20, value=10 )
slider3= cmds.intSliderGrp( field=True, label='Counter_d', minValue=1, maxValue=20, value=10 )



cmds.button(label = "Create Comode",c='comode()')
cmds.showWindow()
   


