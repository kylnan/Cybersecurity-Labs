# Cybersecurity-Labs
Some cybersecurity labs that review things like encryption algorithms, buffer overflows, and tcp-based attacks

## Lab 1
 **Secret-Key Encryption Lab**
 -  The learning objective of this lab is for students to get familiar with the concepts in the secret-key encryption
 and some common attacks on encryption. From this lab, students will gain a first-hand experience on
 encryption algorithms, encryption modes, paddings, and initial vector (IV). Moreover, students will be able
 to use tools and write programs to encrypt/decrypt messages.
 Many common mistakes have been made by developers in using the encryption algorithms and modes.
 These mistakes weaken the strength of the encryption, and eventually lead to vulnerabilities.
---
 ## Lab 2
 **Buffer Overflow Attack**
 - See Lab 2 Report
 - A Buffer Overflow occurs when a programmer implements a buffer/variable with a fixed input size. An attack will attempt to provide an input larger than the buffer can handle so that the data beyond the buffer size will overwrite other memory locations.
---
## Lab 3
**Cross Site Scripting (XSS)**
- See Lab 3 Report
- An XSS attack takes advantage of HTML and JavaScript vulnerabilities in a web application's code. Typically an attacker will look for vulnerable inputs, or boxes where input is mishandled and inject their own JavaScript that could impact the integrity and availability of the web server.
---
## Lab 4
**TCP based Attacks**
- A TCP SYN Flood Attack occurs when an attacker will manipulate packets being sent from a client to a server. It leverages the vulnerability of the TCP 3-way handshake, where the server will be left waiting for an SYN/ACK packet causeing it to become overloaded. This kind of attack is particularly useful when attempting a Denial-Of-Service (DOS) attack.
- We also observe TCP reset attacks and session hijacking to invoke a revserse shell.
---
**Feel free to go through these labs and try some of them yourself!**

**Some good resources that walkthrough some of these attacks can be found [here](https://www.101labs.net/comptia-security/)**
