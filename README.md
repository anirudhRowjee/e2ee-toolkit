# UE20CS101 Project - E2EE toolkit

Of late there has been a lot of concern about what End-To-End Encryption really is, and how it works. This project is intended to serve as a live demonstration of what really happens when you start talking with someone on an app that offers end-to-end-encyption, including features that allow you to see both the encrypted and decrypted text being sent across.

We will demonstrate the [Diffie-Hellman Key Exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) in a chat scenario, allowing you to simulate a chat environment of 2 users. You will be able to see both the encrypted and decrypted messages, but given that understanding of the Exchange process is required to appreciate the working of the project, we consider this project to be more of a proof of concept than anything else.

## Constraints
* You will be allowed to choose the encryption algorithm when you start a session, and all simulated messages will be encrypted with this.
* You will be able to randomly generate public and private keys, both lasting for the session and decided at the start. You will not be able to change these mid-session.
* You will be able to send messages as either user, and will be able to toggle decryption for the messages to see how it looks. 

## The current state of things
![](./UI.png)

We decided to implement the interface in `flask`.


## Python Libraries Being Used
* `tkinter`
* `random`
* `uuid`
* `math`
* `hashlib`
* `cryptography`
* `flask`

## Student Details
* Anish Cherekar (SRN `PES2UG20CS054`)
* Anurag Girish (SRN `PES2UG20CS057`)
* Anirudh Rowjee (SRN `PES2UG20CS050`)
