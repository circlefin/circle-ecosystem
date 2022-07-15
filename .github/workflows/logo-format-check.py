from PIL import Image
from svgpathtools import svg2paths2
import pathlib
import os
import sys

'''
Name: requirement
Param: 
Return:

Function: print logo constraints
Reference: https://github.com/circlefin/circle-ecosystem/blob/master/README.md#logo-constraints
'''
def requirement():
  print('================Logo Constraints=====================')
  print('1. Acceptable File Types: .jpg, .png, .svg')
  print('2. Image Size: 200 x 200 pixels')
  print('3. Aspect Ratio: 1:1 (square)')
  print('4. Max File Size: 5 MB')
  print('======================================================')

'''
Name: format_check
Param: list of paths of logos
Return:
  -1 //does not pass the check
  1  //pass the check

Function: check whether the logos meet the format requirment. 
Reference: https://github.com/circlefin/circle-ecosystem/blob/master/README.md#logo-constraints
'''
def format_check(list_of_logos):
  for logo in list_of_logos:
    path = str(logo)

    # check whether the size is smaller than 5MB
    size = os.path.getsize(path)
    if size>5*10**6:
      print('-----------------Error Message-----------------')
      print('The size of the %s is %i, which does not satisfy the requirement.'%(path,size))
      print('The logo file must be smaller than 5MB.')
      print('-----------------------------------------------')
      return -1
    
    # get the suffix
    index=path.rfind('.')
    suffix=path[index:].upper()
    
    # if the suffix is .svg, using svgpathtools.svg2paths2
    if index!=-1 and suffix == '.SVG':
      try:
        _, __, svg_attributes = svg2paths2(path)
        width,height = svg_attributes['width'],svg_attributes['height']
      except:
        # except it is not a image file
        print('-----------------Error Message-----------------')
        print('The type of the file %s cannot be identified.'%(path))
        print('-----------------------------------------------')
        return -1
      # check whether the pixels are 200x200
      if width != '200' and height != '200':
        print('-----------------Error Message-----------------')
        print('The width and height of the %s are %sx%s which do not satisfy the requirement.'%(path,width,height))
        print('The requirement is 200x200.')
        print('-----------------------------------------------')
        return -1
    
    # if the suffix is others using PIL.Image
    else:
      try:
        im = Image.open(path)
      except:
        # except it is not a image file
        print('-----------------Error Message-----------------')
        print('The type of the file %s cannot be identified.'%(path))
        print('-----------------------------------------------')
        return -1
      
      # check whether the type is one of JPG, JPEG or PNG
      im_type = im.format.upper()
      if im_type.upper() not in ["JPG","PNG","JPEG"]:
        print('-----------------Error Message-----------------')
        print('The file type of the %s does not satisfy the requirement.'%(path))
        print('The logo file type must be .jpg, .png or .svg.')
        print('-----------------------------------------------')
        return -1

      # check whether the pixels are 200x200
      width,height = im.size
      if width!=200 or height!=200:
        print('-----------------Error Message-----------------')
        print('The width and height of the %s are %ix%i which do not satisfy the requirement.'%(path,width,height))
        print('The requirement is 200x200.')
        print('-----------------------------------------------')
        return -1
      
  return 1

# Get all the files under **/logos/
config_path=pathlib.Path("catalog/")
list_of_logos=config_path.glob("**/logos/*")

# Get check result
if format_check(list_of_logos)==-1:
  requirement()
  sys.exit(-1)
else:
  print('---------------------Successful---------------------')
  print('The files under **/logos/ passed the format check.')
  print('----------------------------------------------------')
