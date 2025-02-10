# DecodingCaesarCipher_2020
Old science fair project from 7th grade I thought was cute (it was my first time learning python!)

Christina Htay, Ms. Law, 7th Grade Science
March 9th, 2020

### Cracking Caesars Cipher: With Brute Force or Frequency Analysis?
### Abstract
Substitution ciphers were used throughout history and date back as far as the Roman
Empire when Julius Caesar shifted his messages by three to keep his messages secretive. The
objective of this project is to determine which method is more efficient, Brute-Force, or
Frequency Analysis in decrypting substitution ciphers. I hypothesized that the Frequency
Analysis method would be more efficient as it would take less time to process information.
Finding a better method would make decrypting substitution ciphers easier by finding out one of
the simple methods. First, I created a program that runs 20 times testing both methods on time
needed to successfully decrypt text and attempts needed until the text they decrypted was correct.
The results showed that out of the 20 times the Frequency Analysis was run, it spent less time
decrypting each text than the time it took for the Brute-Force program. Also, it took the
Frequency Analysis fewer attempts until correct than the Brute Force method. The results
supported my hypothesis, stating that the Frequency Analysis program is more accurate and
takes less time to decrypt each text, contrasting the Brute-Force method. In conclusion, the
Frequency Analysis method is better at decrypting substitution ciphers than the Brute-Force
method.

### Question
Which decryption method is more efficient in decoding ciphertext accurately, Frequency
Analysis, or Brute-Force?

### Variables
Independent Variables: Sample Text used to Encrypt and then Decrypt
Dependent Variable: Time Taken Until Text is Decrypted Correctly, Number of Attempts Needed

### Hypothesis
Frequency Analysis is a better way to decode Caesar’s Text against the Brute-Force
method because it is less time consuming and pinpoints which letters are most likely to be used.

### Background Research
The famous code known as the Caesar Cipher, created by Julius Caesar, is an example of
a substitution cipher that shifts letters in a sentence (or word) by “three” steps. In this project, I
am comparing the efficiency of the methods Frequency Analysis and Brute-Force to tackle
decrypting the Caesar Cipher code. Frequency Analysis predicts the probability of a letter being
chosen based on the frequency of a letter used in a sentence/word. For example, if the message
contains one letter that appears more than the rest, it is safe to assume that the letter is “E” since
it is the most frequently used letter in English. The research recorded and analyzed determines
which method is more efficient for decoding encryptions. The importance of these decryption
methods is to see whether Frequency Analysis is essential in decrypting Caesar’s Cipher
compare to the Brute-Force method. This information can inform others (and me) which method
can be more accurate in decrypting other substitution ciphers.

My research question, Which decryption method is more efficient in decoding ciphertext
accurately, Frequency Analysis, or Brute-Force? Frequency Analysis asks for a real-world
connection for more accurate decoding. It can relate to real statistics, due to the Frequency
Analysis’s ability to scan for the most used letter in the encrypted text and ability to relate it to
the most popular used letter in the alphabet. Therefore, it is more likely to be able to pinpoint the
sentence. I hypothesize that Frequency Analysis is a better way to decode Caesar’s Text against
the Brute-Force method because it is less time consuming and pinpoints which letters are most
likely to be used.

During my experiment, I will create two different programs using Python that each
encrypts and decrypts text. One program tests the method “Frequency Analysis,” while the other
test the method “Brute-Force.” My objective is to create a program with both methods to test
which one is more accurate and which one takes less time to decrypt texts. I could later modify
my programs to fit other substitution ciphers better.

### Materials List
● Computer
● Python 3.7.4
### Procedure
1. Create a function that checks whether the decrypted text is English
2. Run Frequency Analysis Program
3. Initialized the counter for Frequency Analysis attempt to zero
4. Start Timer and End Timer using timing function
5. If the text is incorrect increase counter by one
6. When the function has decrypted text successfully stop the timer, store time in list (computer
memory)
7. When the function has decrypted text successfully, store number in counter as attempts in list
(computer memory)
8. Run Brute-Force Program
9. Initialized the counter for Brute-Force attempts to zero
10. Start Timer and End Timer using Time function
11. If the text is incorrect increase count by one
12. When the function has decrypted text successfully stop the timer, store time in list (computer
memory)
13. When the function has decrypted text successfully, store number in counter as attempts in list
(computer memory)
14. Compare the lists, see which method took less time to decrypt text, see which method needed
fewer attempts until correct

### Conclusion
The results for Brute-Force meant that more attempts were needed until their decrypted
text was correct/English. The Frequency Analysis program, however, needed only up to eight
attempts at most until accurate out of the twenty sample sentences needed to be decrypted. I
assume this is because the Brute-Force method is a hundred percent dependent on the key. It
takes six attempts if the key is six, whereas when the key is twenty-five, it takes twenty-five
attempts until accurate. With Frequency Analysis, it's prone to fewer attempts as it detects the
"key" and patterns in encrypted text. Therefore, it is not "key" dependent, making it decrypt text
faster and needs fewer attempts, making Frequency Analysis the superior method in solving
substitution ciphers. However, when decrypting text if the “key” is a minimal number the Brute-Force
program may be faster. For example, in Attempt 12 of the graph Number of Attempts Needed to
Decrypt Correctly vs Test Cases the “key” was two. This the Brute-Force method needs only two
attempts because it is key correlated. However, the Freq Analysis method had to find the most
used letter in the encrypted text and find the key. When replacing the encrypted text with the
most common letters it was revealed in the original text the most common letter in the original
text was O the 4th most common letter to appear. So , while it took four attempts for the
Frequency Analysis it took only two for the Brute-Force method.
