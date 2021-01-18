# encrypt
This is a project that can automatically generate keys for Ceaser encryption. It can also use the keys to encrypt and decrypt messages and txt files.
It takes in 3 parameters and one optional parameter. The parameters are seperated by dashes The first one tells the program what you want to do. 
The options are newkey, encrypt, and decrypt. If you use the newkey command, the second parameter will what you want to name the key, whcih will be saved as a txt file.
(Do not add .txt to the end) If you use the encrypt command, The second parrameter will be the message you want to encrypt, and for the decrypt command, 
it will be what you want to decrypt. For the third parameter, if you use the newkey command, it will be an integer repersenting how long you want each code to be.
Ex. if you use 3, then the code for all charecters, will be three characters long. If you are useing the encrypt or decrypt command,
the third parameter will be what key you want to use to encrypt/decrypt the message. You can add 'file' as a fourth parameter, if you want to encrypt/decrypt a hole file,
in which case the second parameter will be the name of the file. (Only txt files supported).

Note: Do not include the extension of a file whenever it is being used, that is automatic.
Note: Using a dash any of the commands might glitch out the program since dashes are used as seperators
