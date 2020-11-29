import maya.cmds as mc
def buildUI():
  winName = 'myWindow'
  winWidth = 1024 # set a target width and reference this when you specify width
  if mc.window(winName, exists=True):
      mc.deleteUI(winName)
  mc.window(winName, width=winWidth, title='Test Window')
  # i always have keep a reference to the main columnLayout
  mainCL = mc.columnLayout() 
  mc.text(label='text row 1')

  # tmpRowWidth controls the width of my columns in the rowLayout
  # with reference to winWidth
  tmpRowWidth = [winWidth*0.5, winWidth*0.5]
  mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  # at this point our UI pointer is under the rowLayout
  mc.text(label='row column1', align='center', width=tmpRowWidth[0])
  mc.button(label='column 2', width=tmpRowWidth[1])
  # we've used up number of children components, if you add 1 more, 
  # Maya will throw an error
  # now to move our pointer back up the hierarchy, 
  # which is our main columnLayout, mainCL
  mc.setParent('..') # also can use mc.setParent(mainCL)

  tmpRowWidth = [winWidth*0.5, winWidth*0.5]
  mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  mc.text(label='row column1', align='center', width=tmpRowWidth[0])
  mc.button(label='column 2', width=tmpRowWidth[1])
  mc.setParent('..')

  tmpRowWidth = [winWidth*0.7, winWidth*0.3]
  mc.rowLayout(numberOfColumns=2, columnWidth2=tmpRowWidth)
  mc.text(label='row column1', align='center', width=tmpRowWidth[0])
  mc.button(label='column 2', width=tmpRowWidth[1])
  mc.setParent('..')

  mc.text(label='text row 3')

  tmpWidth = [winWidth*0.3, winWidth*0.5, winWidth*0.2]
  mc.textFieldButtonGrp(label='txt field', w=winWidth, columnWidth3=tmpWidth, buttonLabel='okay')
  mc.button('full width button', width=winWidth)

  mc.showWindow(winName)
  mc.window(winName, e=True, width=winWidth, height=1)
  return
buildUI()