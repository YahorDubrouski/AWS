#!/bin/bash

# Load Database credentials
SECRET_NAME="RdsCredentials"
REGION="us-east-1"
SECRET=$(aws secretsmanager get-secret-value --secret-id $SECRET_NAME --region $REGION)
DB_HOST=$(echo $SECRET | jq -r '.SecretString | fromjson | .host')
DB_PASS=$(echo $SECRET | jq -r '.SecretString | fromjson | .password')
DB_USER="admin" #TODO move to the secrets
DB_NAME="MyDb" #TODO move to the secrets

# Show database data
OUTPUT_FILE="/var/www/html/index.html"
echo "<h2>Users Data</h2><table border='1'>" >> $OUTPUT_FILE
mysql -h $DB_HOST -u $DB_USER -p$DB_PASS $DB_NAME -e "SELECT * FROM users;" | while read -r line; do
    echo "<tr><td>${line//      /</td><td>}</td></tr>" >> $OUTPUT_FILE
done
echo "</table>" >> $OUTPUT_FILE
