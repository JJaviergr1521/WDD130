""" A manufacturing company needs a program that will help its employees pack manufactured 
items into boxes for shipping. Write a Python program named boxes.py that asks the user for 
two integers:  1) the number of manufactured items and 2) the number of items that the user 
will pack per box. Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes. """



"""this part defines the prompting part of the program and calling the other function 
that computes the quantity of boxes"""

import math
def Prompt():
  Items = int(input("Enter the number of items:"))
  Iperbox = int(input("Enter the number of items per box:"))
  TotalAmount = BoxpItem(Items,Iperbox)
  return TotalAmount

"""this part of the program computes the quantity and use the math.ceil() built in function to return
the correct value of boxes"""


def BoxpItem(IExist,Iinbox):
    Boxes = math.ceil(IExist / Iinbox)
    print ("For " + str(IExist) + " items, packing " + str(Iinbox) +  " items in each box, you will need "+ str(Boxes) +" boxes.")



Prompt()

