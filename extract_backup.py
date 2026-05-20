#!/usr/bin/env python3
"""Extract and analyze iOS device backup forensics"""
import os, plistlib, sqlite3, json

def extract_ios_backup(backup_path):
    """Parse iOS backup directory structure"""
    results = {'messages': [], 'contacts': [], 'locations': []}
    
    # Domains typically contain per-app data
    domain_dirs = os.listdir(backup_path) if os.path.isdir(backup_path) else []
    
    # SMS/iMessage (com.apple.mobilesms)
    sms_db = os.path.join(backup_path, 'HomeDomain', 'Library/SMS/sms.db')
    if os.path.exists(sms_db):
        conn = sqlite3.connect(sms_db)
        cur = conn.cursor()
        cur.execute("SELECT date, text, address FROM message LIMIT 100")
        for row in cur.fetchall():
            results['messages'].append({'date': row[0], 'text': row[1], 'from': row[2]})
        conn.close()
    
    # Contacts (com.apple.contacts)
    contacts_db = os.path.join(backup_path, 'HomeDomain', 'Library/AddressBook/AddressBook.sqlitedb')
    if os.path.exists(contacts_db):
        conn = sqlite3.connect(contacts_db)
        cur = conn.cursor()
        cur.execute("SELECT ZFIRSTNAME, ZLASTNAME FROM ZABCDCONTACT LIMIT 50")
        for row in cur.fetchall():
            results['contacts'].append({'name': f"{row[0]} {row[1]}"})
        conn.close()
    
    # Location history (com.apple.maps)
    loc_db = os.path.join(backup_path, 'HomeDomain', 'Library/Maps/History.db')
    if os.path.exists(loc_db):
        conn = sqlite3.connect(loc_db)
        cur = conn.cursor()
        cur.execute("SELECT latitude, longitude FROM history LIMIT 50")
        for row in cur.fetchall():
            results['locations'].append({'lat': row[0], 'lon': row[1]})
        conn.close()
    
    return results

if __name__ == '__main__':
    import sys
    backup_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    data = extract_ios_backup(backup_path)
    print(json.dumps(data, indent=2))
