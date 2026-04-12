def palindrome(str):
      rev = ""
      for i in range(len(str)-1 , -1 , -1):
            rev = rev + str[i]
      if rev == str:
       print("palindrome")
      else:
          print("not palindrome")

#palindrome("arora")
name = str(input("enter name"))
palindrome(name)


