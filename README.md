# SIEM Log Monitor

## Overview

A Python-based Security Information and Event Management (SIEM) log monitoring tool that analyzes security logs, detects suspicious login activity, and generates security alerts.

## Features

- Log file analysis
- Failed login detection
- Brute force attack identification
- CSV alert reporting
- Security event monitoring

## Technologies Used

- Python
- CSV
- File Handling
- Dictionaries
- Security Monitoring Concepts

## How It Works

The application:

1. Reads security logs
2. Tracks failed login attempts
3. Identifies IP addresses with 3 or more failures
4. Generates security alerts
5. Exports results to CSV

## Example Alert

IP: 193.165.1.15
Failed Attempts: 3
Alert: Potential Brute Force Attack

## Future Improvements

- Real-time log monitoring
- Email notifications
- Dashboard reporting
- Threat scoring
- SQLite database integration

## How to Run

python siem_monitor.py