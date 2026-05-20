#!/usr/bin/env python3
"""Extract and parse iOS device backup — read plist files, extract messages, contacts"""
import os, plistlib, sys

if len(sys.argv) < 2:
    print("Usage: python3 extract_backup.py <backup_path>")
    sys.exit(1)

backup = sys.argv[1]
if not os.path.isdir(backup):
    print(f"Backup directory not found: {backup}")
    sys.exit(1)

# Try to find plist files (common in iOS backups)
plists = []
for root, dirs, files in os.walk(backup):
    for f in files:
        if f.endswith('.plist'):
            plists.append(os.path.join(root, f))

print(f"Found {len(plists)} plist files:")
for plist_path in plists[:10]:
    try:
        with open(plist_path, 'rb') as f:
            data = plistlib.load(f)
        print(f"  {plist_path}: {type(data).__name__}")
    except Exception as e:
        print(f"  {plist_path}: ERROR - {e}")
