#!/bin/bash
# app_decryptor.sh -- Decrypt iOS app binary on jailbroken device
# Requires: Frida, frida-compile
# Usage: ./app_decryptor.sh com.example.app

PKG="$1"
FRIDA_SCRIPT=$(cat <<'EOF'
var decrypted_app_found = false;
ObjC.choose(NSBundle, {
  onMatch: function(bundle) {
    console.log("Bundle: " + bundle.$ownMembers());
    decrypted_app_found = true;
  }
});
if (!decrypted_app_found) console.log("No decrypted app found");
EOF
)

echo "Dumping $PKG..."
frida -f "$PKG" -l - <<< "$FRIDA_SCRIPT"
