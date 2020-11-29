import maya.cmds as mc
mc.file(f=True, new=True)
def buildUI():
  winName = 'myWindow'
  winWidth = 1024 # set a target width and reference this when you specify width
  if mc.window(winName, exists=True):
      mc.deleteUI(winName)
  mc.window(winName, width=winWidth, title='Forniture Generator')
  # i always have keep a reference to the main columnLayout
  mainCL = mc.columnLayout() 
  mainRLWidth = [winWidth*0.8, winWidth*0.6]
  mainRL = mc.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, 'top', 0))
  mc.columnLayout(w=mainRLWidth[0]) # create a columnLayout under the first row of mainRL
  mc.text(label='Title column 1', font='boldLabelFont')
  mc.text(label='')
  mc.text(label='text row 1')

  # tmpRowWidth controls the width of my columns in the rowLayout
  # with reference to winWidth
  tmpRowWidth = [mainRLWidth[0]*0.3, mainRLWidth[0]*0.7]
  mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  # at this point our UI pointer is under the rowLayout
  #mc.text(label='text column1', align='center', width=tmpRowWidth[0])
  mc.intSliderGrp( field=True, label='tablewidthz', minValue=4, maxValue=20, value=10, width=tmpRowWidth[0] )
  mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Lamp', width=tmpRowWidth[1])
  #mc.button(label='column 2', width=tmpRowWidth[1])
  # we've used up number of children components, if you add 1 more, 
  # Maya will throw an error
  # now to move our pointer back up the hierarchy, 
  # which is our main rowLayout, mainRL
  mc.setParent('..') # also can use mc.setParent(mainRL)

  # tmpRowWidth = [mainRLWidth[0]*0.5, mainRLWidth[0]*0.5]
  # mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  # mc.text(label='row column1', align='center', width=tmpRowWidth[0])
  # #mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Lamp')
  # #mc.button(label='column 2', width=tmpRowWidth[1])
  # mc.setParent('..')

  # tmpRowWidth = [mainRLWidth[0]*0.7, mainRLWidth[0]*0.3]
  # mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  # mc.text(label='row column1', align='center', width=tmpRowWidth[0])
  # mc.iconTextButton(style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Lamp', width=tmpRowWidth[1])
  # #mc.button(label='column 2', width=tmpRowWidth[1])
  # mc.setParent('..')

  # mc.text(label='text row 3')
  # tmpWidth = [mainRLWidth[0]*0.3, mainRLWidth[0]*0.5, mainRLWidth[0]*0.2]
  # #mc.textFieldButtonGrp(label='txt field', w=mainRLWidth[0], columnWidth3=tmpWidth, buttonLabel='okay')
  # mc.button('full row width button', width=mainRLWidth[0])
  # mc.setParent('..') # this will exit the rowLayout back to the mainRL, same as mc.setParent(mainRL)

  mc.columnLayout(width=mainRLWidth[1]) # start another vertical layout
  mc.text(label='mainRL column 2', font='boldLabelFont')
  mc.text(label='')
  mc.text(label='text row 1')
  mc.button(label='button', width=mainRLWidth[1]*0.95, height=70)

  mc.setParent(mainCL) # set UI pointer back under the main columnLayout
  mc.text(label='')
  mc.button(label='full window width button', width=winWidth, height=40)

  mc.showWindow(winName)
  mc.window(winName, e=True, width=winWidth, height=1)
  return
buildUI()





# window = cmds.window()
# cmds.columnLayout( adjustableColumn=True )
# cmds.iconTextButton( style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Table_chaise_icon-01.png', label='Lamp'  )
# cmds.iconTextButton( style='iconAndTextVertical', image1='/home/fullarostaky/maya/2020/scripts/icons/Lamp-01.png', label='Table'  )
# cmds.showWindow( window )