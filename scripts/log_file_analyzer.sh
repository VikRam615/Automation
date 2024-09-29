#!/bin/bash

# file configuration
LOG_FILE="webserver.log"
REPORT_FILE="log_analysis_report.txt"

# Checking if the log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file does not exist: $LOG_FILE"
    exit 1
fi

# Clear the report file
echo "Log Analysis Report" > $REPORT_FILE
echo "===================" >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Count 404 errors
ERROR_404_COUNT=$(grep -c ' 404 ' "$LOG_FILE")
echo "Number of 404 Errors: $ERROR_404_COUNT" >> $REPORT_FILE

# Most requested pages
echo "Most Requested Pages:" >> $REPORT_FILE
awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 10 >> $REPORT_FILE

# Most requests by IP addresses
echo "" >> $REPORT_FILE
echo "IP Addresses with Most Requests:" >> $REPORT_FILE
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 10 >> $REPORT_FILE

# Completion message
echo "Log analysis completed. Check $REPORT_FILE for the summary."
