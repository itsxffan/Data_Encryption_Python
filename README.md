# Project - Python_DataEncryption_3-Levels

---

#### Language - Python

#### Author - Saffan Ahmed

---

Based upon Caaser Cipher encryption. Each program implements the encryption stages further.

1. Program 1 - EncrpytionProgram1:

- Encryption program involves taking users input to then encode each character of users input based on
  a set numeric value within range (1-25). Each character would then be shifted by the numerical value.
  I.e. If numerical encode was set to Encrypt and shift value was 2. Then for input e.g. "abcdefg" output will be "cdefghi".

2. Program 2 - EncryptionProgram2:

- Similar to initial program instead will shift users input based on keyword. The keyword will be converted into its numeric equivalent then based on numeric position each character will shift by that value.
  Example:
  Input -> "Hello"
  Mode -> "Encrypt"
  Keyword -> "key"
  Output -> "sjkwt"

3. Program 3 - EncryptionProgram3:

- This encrpytion program further builds up on previous encryption level. As it uses an additional keyword. So users input is encoded by the 2 keywords once they are converted to thier numerical equivalent then each input character is shifted based on the sum of these numerical equivalents. Also program enables text to be encoded / decoded from file. Also write-read to file.
  Example:
  Input -> "Hello"
  Mode -> "Encrypt"
  Keyword1 -> "united"
  Keyword2 -> "kingdom"
  Output -> "nbimx"

Note: For each program their counterparts for Decryption follows same principles but instead input values will be inversely shifted.
