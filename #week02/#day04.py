#-------------------------------------------SETTER GETTER-------------------------------------------------------------


class year_graduated:
   def __init__(self, year=32):
      self.year = year

   @property
   def Aboutyear(self):
      return self.year

   @Aboutyear.setter
   def Aboutyear(self, a):
      self.year = a

grad_obj = year_graduated()
print(grad_obj.year)

grad_obj.year = 2018
print(grad_obj.year)