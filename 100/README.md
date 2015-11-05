To solve this challenge, one must simply extract a ciphertext that
is wrapped into 1+17 successive base64 encoding operations.

The filename was a reference to Giovan Battista Bellaso (cf. [Wikipedia](https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso)).
This guy is known to have (probably) invented Vigenère's cipher,
hence the reference to Stigler's law of eponymy (cf. [Wikipedia](https://en.wikipedia.org/wiki/Stigler's_law_of_eponymy)).

By having a look at the ciphertext, one can notice that the string "CyberSec15" is repeated
many times, as when one encrypts null bytes using a Vigenère cipher. The group law used to
combine the plaintext and the key was an XOR. 
