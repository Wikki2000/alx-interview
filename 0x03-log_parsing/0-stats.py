#!/usr/bin/python3
"""
0-stats.py
"""
import sys
import re
from signal import signal, SIGINT

# Define a regex pattern to match the input line format
pattern = re.compile(r'^(?P<ip>\S+) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$')

# Initialize variables to hold metrics
total_size = 0
status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def handle_interrupt(signal_received, frame):
    """Handles the keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the keyboard interrupt handler
signal(SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        # Strip whitespace and try matching the line with the pattern
        line = line.strip()
        match = pattern.match(line)
        
        if match:
            # Extract status code and file size, then update metrics
            status_code = match.group('status')
            file_size = int(match.group('size'))
            
            # Update total file size
            total_size += file_size
            
            # Update status code count if it's in our predefined list
            if status_code in status_counts:
                status_counts[status_code] += 1
            
            # Increment line count
            line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()
    
    # Print final statistics after reading all lines
    print_stats()

except Exception as e:
    print(f"Error processing input: {e}", file=sys.stderr)

