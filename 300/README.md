The file contains Python code (partially) implementing a Diffie-Hellman key agreement.
One gets a generator `g`, a prime number `p` and two values `ga` and `gb`, as well as an AES-CBC ciphertext. The goal is to compute the missing value `g^(ab)` that can then be fed into the hash function to derive the AES key required to decrypt the flag.

For this, one is forced to compute a discrete logarithm in a Diffie-Hellman group having a size of more than 2048 bits. This is possible if one knows the full factorization of the group order `p-1`. In that case, the order of the group is the product of about 130 small 16-bit primes.

Applying the Pohlig-Hellman algorithm (cf. [Wikipedia](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm)) allows to compute the discrete logarithm modulo each small prime, and then to reconstruct the value modulo `p-1` using the
Chinese remainder theorem (explaining the few strings in Chinese). 
