import re


class BasePasswordManager:
    passwords = ["Ascd","Abcd12"]
    def old_passwords(self,Pass):
        self.passwords.append(Pass)
    def get_password(self):
        return self.passwords[-1]
    def is_correct(self,Pass):
        return Pass == self.get_password()

class PasswordManager(BasePasswordManager):
    
    def set_password(self,Pass):
        oldpass = BasePasswordManager.get_password(self)
        oldlevel = self.get_level(oldpass)
        newlevel = self.get_level(Pass)
        if newlevel==2 and len(Pass)>=6:
            BasePasswordManager.old_passwords(self,Pass)
            return True
        elif newlevel>oldlevel and len(Pass)>=6:
            BasePasswordManager.old_passwords(self,Pass)
            return True
        else:
            return False
    def get_level(self,Pass):
        level=0
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        regex1 = re.compile("[a-zA-Z]")
        if Pass.isnumeric() or Pass.isalpha():
            level = 0
        elif Pass.isalnum():
            level = 1
        elif re.search(r'\d',Pass)!=None and regex.search(Pass)!=None and regex1.search(Pass)!=None:
            level = 2
        elif regex.search(Pass)!=None and regex1.search(Pass)!=None:
          level = 1
        elif regex.search(Pass)!=None and re.search(r'\d',Pass)!=None:
          level = 1
        return level

    
Manager = PasswordManager()
Pass = ""
opt = ""
flag = False
for i in range(0,3):
  Pass = input("Enter The Password : ")
  if Manager.is_correct(Pass):
    flag = True
    break
  else :
    print("Worng Password")
if flag:
  while True:
    print("Choose 1: For Change Password")
    print("Choose 2: To get Security Level of Current Password")
    print("Choose 3: To Exit")
    opt = input("Enter the Option : ")
    if opt == "1":
      newPass = input("Enter The New Password : ")
      if Manager.set_password(newPass):
        print("Password Changed Successfully")
      else:
        print("Security Level of current Password is lower than Pervious Password Or Length is less than 6")
    if opt == "2":
      print("Level : ",Manager.get_level(Manager.get_password()))
    if opt == "3":
      print("Terminated Successfully")
      break
if flag == False:
  print("You Have Entered Worng Password 3 Times Please Try Agin After Some Time")


  
