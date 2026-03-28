# 🔍 iOS Forensics & Reverse Engineering

Tools and techniques for analyzing iOS apps and devices.

## Topics
- NAND dumping and decryption (A5-A11 via checkm8)
- iOS app decryption and class dump
- Frida on iOS (with jailbreak)
- SSL pinning bypass
- Entitlements modification

## Limitations (A12+)
- No public BootROM exploit (unlike A5-A11 checkm8)
- PAC and BPR prevent many traditional bypasses
- Requires jailbreak for most analysis

## Jailbreak options
- A5-A11: checkra1n, palera1n
- A12-A15: Dopamine (15.0-15.4.1)
- A16+: No stable public jailbreak (2026)
