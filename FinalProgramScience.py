def encrypt(orginal_text,k):
   cipher_text = ''
   for letter in orginal_text:
        #Conditional Statements
        #Shift to xyz from abc


        #Shift 1
        if (int(k)) == 1:
            if (ord(letter) == 90):
                new_letter = chr(ord(letter)- 25)
                cipher_text =  cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
                
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 1)
                cipher_text = cipher_text + new_letter
    #Returning function
    


   #Shift 2
        if (int(k)) == 2:
            if (89 == ord(letter) or 90 == ord(letter)):
                new_letter = chr(ord(letter)- 24)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 2)
                cipher_text = cipher_text + new_letter
    #Returning function
    


        #shift 3
        if (int(k)) == 3:
            if (88 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)- 23)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 3)
                cipher_text = cipher_text + new_letter
    #Returning function
   




        #Shift 4
        if (int(k)) == 4:
            if (87 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)- 22)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 4)
                cipher_text = cipher_text + new_letter
    #Returning function
    



        #Shift 5
        if (int(k)) == 5:
            if (86 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-21)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 5)
                cipher_text = cipher_text + new_letter
    #Returning function
   


        #Shift 6
        if (int(k)) == 6:
            if (85 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-20)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 6)
                cipher_text = cipher_text + new_letter
    #Returning function
    



        #Shift 7
        if (int(k)) == 7:
            if (84 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-19)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 7)
                cipher_text = cipher_text + new_letter
    #Returning function
   



        #Shift 8
        if (int(k)) == 8:
            if (83 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-18)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 8)
                cipher_text = cipher_text + new_letter
    #Returning function
    



    
        #Shift 9
        if (int(k)) == 9:
            if (82 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-17)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 9)
                cipher_text = cipher_text + new_letter
    #Returning function
   





        #Shift 10
        if (int(k)) == 10:
            if (81 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-16)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 10)
                cipher_text = cipher_text + new_letter
    #Returning function
    





        #Shift 11
        if (int(k)) == 11:
            if (80 <= ord(letter) <= 90):
                new_letter = chr(ord(letter) - 15)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 11)
                cipher_text = cipher_text + new_letter
    #Returning function
   





        #Shift 12
        if (int(k)) == 12:
             if (79 <= ord(letter) <= 90):
                new_letter = chr(ord(letter) - 14)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
             elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
             else:
                new_letter = chr(ord(letter) + 12)
                cipher_text = cipher_text + new_letter
    #Returning function
    




        #Shift 13
        if (int(k)) == 13:
            if (78 <= ord(letter) <= 90):
                new_letter = chr(ord(letter) - 13)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 13)
                cipher_text = cipher_text + new_letter
    #Returning function
    





        #Shift 14
        if (int(k)) == 14:
            if (77 <= ord(letter) <= 90):
                new_letter = chr(ord(letter) - 12)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 14)
                cipher_text = cipher_text + new_letter
    #Returning function
   





        #Shift 15
        if (int(k)) == 15:
            if (76 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-11)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 15)
                cipher_text = cipher_text + new_letter
    #Returning function
    





        #Shift 16
        if (int(k)) == 16:
            if (75 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-10)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 16)
                cipher_text = cipher_text + new_letter
    #Returning function
    




        
        #Shift 17
        if (int(k)) == 17:
             if (74 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-9)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
             elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
             else:
                new_letter = chr(ord(letter) + 17)
                cipher_text = cipher_text + new_letter
    #Returning function
    







        #Shift 18
        if (int(k)) == 18:
            if (73 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-8)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 18)
                cipher_text = cipher_text + new_letter
    #Returning function
   








        #Shift 19
        if (int(k)) == 19:
            if (72 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-7)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 19)
                cipher_text = cipher_text + new_letter
    #Returning function
  









        #Shift 20
        if (int(k)) == 20:
            if (71 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-6)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 20)
                cipher_text = cipher_text + new_letter
    #Returning function
    








        #Shift 21
        if (int(k)) == 21:
            if (70 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-5)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 21)
                cipher_text = cipher_text + new_letter
    #Returning function
   






    

        #Shift 22
        if (int(k)) == 22:
            if (69 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-4)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 22)
                cipher_text = cipher_text + new_letter
    #Returning function
    






        #Shift 23
        if (int(k)) == 23:
            if (68 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-3)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 23)
                cipher_text = cipher_text + new_letter
    #Returning function
   







        #Shift 24
        if (int(k)) == 24:
            if (67 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)- 2)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 24)
                cipher_text = cipher_text + new_letter
    #Returning function
  







        #Shift 25
        if (int(k))  == 25:
            if (66 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-1)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 25)
                cipher_text = cipher_text + new_letter
    #Returning function
  





        #Shift 26
        if (int(k)) == 26:
            if (65 <= ord(letter) <= 90):
                new_letter = chr(ord(letter)-0)
                cipher_text = cipher_text + new_letter
           
        #Leave symbols and space keyeys alone 
            elif (32 <= ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) == 126 or ord(letter) == 127):
                new_letter = chr(ord(letter))
                cipher_text = cipher_text + new_letter
        #Any other letter shifts 3 normally
            else:
                new_letter = chr(ord(letter) + 26)
                cipher_text = cipher_text + new_letter
    #Returning function
   

   return cipher_text



def count_letter_freq(cipher_text):
    count_letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for n in cipher_text:
       if n in Letters:
          count_letters[n] += 1
    #print(count_letters)
    return count_letters


    
def conversion(count_letters,cipher_text):

  keys = []
  max_val = max(count_letters.values())
  max_letters = [k for k,v in count_letters.items() if v == max_val] 
  print(max_letters) 
  found_max = False;
  for n in cipher_text:
    for max_value in max_letters:     
        if n == max_value:
            for l in ETAOIN:
                key = (ord(max_value)- ord(l))
                if key > 0:
                  keys.append(key)   
                else:
                  key = key + 26
                  keys.append(key)
            found_max = True;
            break
        if found_max == True:
            break
    if found_max == True:
        break
    
            

  #print(keys)               
  return keys   
         
         
   
   
def decryption(cipher_text,key):
   #print(key)
   new_text = ''
   for num in range (0,26):
      for k in cipher_text:
            if (int(key)) == 1:
                if (ord(k) == 65):
                    new_letter = chr(ord(k) + 25)
                    new_text = new_text + new_letter
                    
        #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text = new_text + new_letter
                    new_text
        #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 1)
                    new_text = new_text+ new_letter
    #Returning function
    


   #Shift 2
            if (int(key)) == 2:
                if (65 == ord(k) or 66 == ord(k)):
                    new_letter = chr(ord(k)+ 24)
                    new_text= new_text+ new_letter
           
        #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
        #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 2)
                    new_text= new_text+ new_letter
    #Returning function
    



        #shift 3
            if (int(key)) == 3:
                if (65 <= ord(k) <= 67):
                    new_letter = chr(ord(k)+ 23)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 3)
                    new_text= new_text+ new_letter
        #Returning function
       




            #Shift 4
            if (int(key)) == 4:
                if (65 <= ord(k) <= 68):
                    new_letter = chr(ord(k)+ 22)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 4)
                    new_text= new_text+ new_letter
        #Returning function
        



            #Shift 5
            if (int(key)) == 5:
                if (65 <= ord(k) <= 69):
                    new_letter = chr(ord(k)+21)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 5)
                    new_text= new_text+ new_letter
        #Returning function
       


            #Shift 6
            if (int(key)) == 6:
                if (65 <= ord(k) <= 70):
                    new_letter = chr(ord(k)+20)
                    new_text= new_text + new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text + new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 6)
                    new_text= new_text+ new_letter
        #Returning function
        



            #Shift 7
            if (int(key)) == 7:
                if (65 <= ord(k) <= 71):
                    new_letter = chr(ord(k)+19)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 7)
                    new_text= new_text+ new_letter
        #Returning function
       



            #Shift 8
            if (int(key)) == 8:
                if (65 <= ord(k) <= 72):
                    new_letter = chr(ord(k)+18)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 8)
                    new_text= new_text+ new_letter
        #Returning function
        



        
            #Shift 9
            if (int(key)) == 9:
                if (65 <= ord(k) <= 73):
                    new_letter = chr(ord(k)+17)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 9)
                    new_text= new_text+ new_letter
        #Returning function
       





            #Shift 10
            if (int(key)) == 10:
                if (65 <= ord(k) <= 74):
                    new_letter = chr(ord(k)+16)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 10)
                    new_text= new_text+ new_letter
        #Returning function
        





            #Shift 11
            if (int(key)) == 11:
                if (65 <= ord(k) <= 75):
                    new_letter = chr(ord(k) + 15)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 11)
                    new_text= new_text+ new_letter
        #Returning function
       





            #Shift 12
            if (int(key)) == 12:
                 if (65 <= ord(k) <= 76):
                    new_letter = chr(ord(k) + 14)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                 elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                 else:
                    new_letter = chr(ord(k) - 12)
                    new_text= new_text+ new_letter
        #Returning function
        




            #Shift 13
            if (int(key)) == 13:
                if (65 <= ord(k) <= 77):
                    new_letter = chr(ord(k) + 13)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 13)
                    new_text= new_text+ new_letter
        #Returning function
        





            #Shift 14
            if (int(key)) == 14:
                if (65 <= ord(k) <= 78):
                    new_letter = chr(ord(k) + 12)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 14)
                    new_text= new_text+ new_letter
        #Returning function
       





            #Shift 15
            if (int(key)) == 15:
                if (65 <= ord(k) <= 79):
                    new_letter = chr(ord(k)+11)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 15)
                    new_text= new_text+ new_letter
        #Returning function
        





            #Shift 16
            if (int(key)) == 16:
                if (65 <= ord(k) <= 80):
                    new_letter = chr(ord(k)+10)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 16)
                    new_text= new_text+ new_letter
        #Returning function
        




            
            #Shift 17
            if (int(key)) == 17:
                 if (65 <= ord(k) <= 81):
                    new_letter = chr(ord(k)+9)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                 elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                 else:
                    new_letter = chr(ord(k) - 17)
                    new_text= new_text+ new_letter
        #Returning function
        







            #Shift 18
            if (int(key)) == 18:
                if (65 <= ord(k) <= 82):
                    new_letter = chr(ord(k)+8)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 18)
                    new_text= new_text+ new_letter
        #Returning function
       








            #Shift 19
            if (int(key)) == 19:
                if (65 <= ord(k) <= 83):
                    new_letter = chr(ord(k)+7)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 19)
                    new_text= new_text+ new_letter
        #Returning function
      









            #Shift 20
            if (int(key)) == 20:
                if (65 <= ord(k) <= 84):
                    new_letter = chr(ord(k)+6)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 20)
                    new_text = new_text+ new_letter
        #Returning function
        








            #Shift 21
            if (int(key)) == 21:
                if (65 <= ord(k) <= 85):
                    new_letter = chr(ord(k)+5)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k)- 21)
                    new_text= new_text+ new_letter
        #Returning function
       






        

            #Shift 22
            if (int(key)) == 22:
                if (65 <= ord(k) <= 86):
                    new_letter = chr(ord(k)+4)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 22)
                    new_text= new_text+ new_letter
        #Returning function
        






            #Shift 23
            if (int(key)) == 23:
                if (65 <= ord(k) <= 87):
                    new_letter = chr(ord(k)+ 3)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 23)
                    new_text= new_text+ new_letter
        #Returning function
       







            #Shift 24
            if (int(key)) == 24:
                if (65 <= ord(k) <= 88):
                    new_letter = chr(ord(k) + 2)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 24)
                    new_text= new_text+ new_letter
        #Returning function
      







            #Shift 25
            if (int(key))  == 25:
                if (65 <= ord(k) <= 89):
                    new_letter = chr(ord(k)+1)
                    new_text= new_text+ new_letter
               
            #Leave symbols and space keyeys alone 
                elif (32 <= ord(k) <= 64 or 91 <= ord(k) <= 96 or ord(k) == 126 or ord(k) == 127):
                    new_letter = chr(ord(k))
                    new_text= new_text+ new_letter
            #Any other letter shifts 3 normally
                else:
                    new_letter = chr(ord(k) - 25)
                    new_text= new_text+ new_letter
        #Returning function
      


      return new_text
      

def check_english(text):
  d = SpellChecker("en_US")
  d.set_text(text)
  errors = [err.word for err in d]
 
  return False if ((len(errors) > 0) or len(text.split()) < 1) else True
  
 # for err in d:
  #   return False
  #return True

   
   

   
import time
import random
from enchant.checker import SpellChecker



#user_input = input("Enter Plain Text (Do not enter symbols like ? ] etc.):")
ETAOIN = "ETAOINSHRDLCUMWFGYPVBKJXQZ"
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

i = 0;
max_try_F = []
max_try_B = []

time_F = []
time_B = []
while i < 1:

   user_input = input("Enter Plain Text (Do not enter symbols like ? ] etc.):")
   random_num = random.randint(1,25)
   #random_num = 25
   count_letters = {}
   print("Number of shifts %s" % random_num)



   
   user_input_caps = user_input.upper()
   cipher_text = encrypt(user_input_caps,random_num)
   #print("Random Key %s" %  random_num)
   print(cipher_text)







   #Now Do Freq analysis

   analysis = count_letter_freq(cipher_text)
   list_conversion = conversion(analysis,cipher_text)
   #print(list_conversion)
   start_freq = time.process_time()

   max_try_freq = 1
   for keys in list_conversion:
      decrypt_text = decryption(cipher_text,keys)
      #d = enchant.Dict("en_US")
     
   
      #error = d.check(decrypt_text)
      error = check_english(decrypt_text)
      #print(keys)
      print(decrypt_text)
      #print("Max Try  : %s " % error) 
   
      if error == True :
         break
      else:
         max_try_freq = max_try_freq + 1
      
   #print("Max Try  : %s " % max_try_freq)  
   
   
   


   end_freq = time.process_time()
   used_time_freq = float(end_freq - start_freq) 
   max_try_F.append(max_try_freq)
   time_F.append(used_time_freq)
   #print("Max Try  : %s " % max_try)
   #print("Time taken for Freq program %s" % float(used_time))





   #print('This is the Brute Force decrypted code')

   start = time.process_time()

   max_try = 1
   #Calling orginal text using 
   for num in range(1,26):
       #print("This is %s shift" % (num))
       new_text = decryption(cipher_text,num)
       error = check_english(new_text)
   
       print("DEcrypt Text : %s " % decrypt_text)
      #print("Error  : %s " % error)
   
       if error == True :
          break
       else:
          max_try = max_try + 1
  

   

   #print("Max Try  : %s " % max_try)


   
   end = time.process_time()
   used_time  = float(end - start) 
   max_try_B.append(max_try)
   time_B.append(used_time)
   i = i +1


print("Time taken for Freq program %s" % time_F)
print("Time taken for Brute  program %s" % time_B)
print("Max Try Brute  : %s " % max_try_B)
print("Max Try F %s" % max_try_F)


