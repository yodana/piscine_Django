#/bin|sh
curl -v --silent $1 2>&1 | grep "Location" | cut -c 13-