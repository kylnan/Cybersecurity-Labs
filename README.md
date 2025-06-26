# Cybersecurity Labs Portfolio

This repository showcases hands-on cybersecurity labs I've completed to strengthen my understanding of common vulnerabilities, cryptographic techniques, and network-based attacks. Each lab demonstrates a practical application of cybersecurity principles using tools like Wireshark, Python, and Linux-based utilities.

---

## Labs Overview

### Lab 1 – Secret-Key Encryption
- Explored symmetric encryption concepts including cipher modes (ECB, CBC), padding schemes, and the role of Initialization Vectors (IVs).
- Demonstrated how improper implementation can weaken encryption (e.g., static IVs, poor padding).
- Tools: Python (PyCrypto or cryptography), hex editors

### Lab 2 – Buffer Overflow Attack
- Demonstrated memory corruption through buffer overflow on vulnerable C programs.
- Overwrote the EIP register to gain code execution using controlled payloads.
- Tools: gdb, objdump, Python, Linux

### Lab 3 – Cross-Site Scripting (XSS)
- Performed reflected and stored XSS attacks by injecting malicious JavaScript into web forms.
- Discussed real-world XSS impacts, including cookie theft and session hijacking.
- Tools: Burp Suite, browser dev tools, JavaScript

### Lab 4 – TCP-Based Attacks
- Conducted SYN flood and TCP reset attacks to disrupt client-server connections.
- Executed session hijacking attacks to gain shell access via TCP injection.
- Tools: Wireshark, hping3, Scapy, TCPDump

---

## What You'll Find in This Repo
Each lab folder contains:
- A detailed lab report or writeup (e.g., `HW*_Report.docx`)
- Screenshots or packet captures (where applicable)
- Scripts and example payloads
- Tools used and key takeaways

---

## Additional Resources
- [101Labs Security+ Practice](https://www.101labs.net/comptia-security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
