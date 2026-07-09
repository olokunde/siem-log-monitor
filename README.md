# SIEM Log Monitor

A Python tool that analyzes authentication logs, detects brute-force login
patterns, and exports security alerts to CSV — a miniature version of what
SIEM platforms like Splunk do at scale.

## Why I built this

I'm a security-minded IT professional building a portfolio of security tooling.
Log analysis is the daily bread of security operations, so I built my own
detector from scratch to understand what tools like Splunk automate: parsing
raw logs, tracking events per source, and turning thresholds into alerts.

## Features

- Parses authentication logs (`LOGIN_SUCCESS` / `LOGIN_FAILED` events)
- Tracks failed login attempts per IP address
- Flags any IP with 3 or more failures as a potential brute-force attack
- Prints a security report: unique suspicious IPs and total failed logins
- Exports alerts to `alerts.csv` for further analysis
- Ships with sample logs — clone and run, no setup needed

## How it works

1. Reads `sample_security_logs.txt` line by line
2. Counts `LOGIN_FAILED` events per IP address
3. Any IP crossing the 3-failure threshold generates an alert
4. Results print to the terminal and save to `alerts.csv`

Log format expected:

```text
2026-06-18 08:01:45 LOGIN_FAILED 192.168.1.15
```

## Example alert

```text
IP: 192.168.1.15 | Failed Attempts: 3 | Potential Brute Force Attack
```

## Tech stack

- Python 3 (standard library only — no dependencies)
- CSV output via the `csv` module

## How to run

```bash
python siem_monitor.py
```

## What I'd improve next

- Make the log file path and failure threshold configurable via command-line arguments
- Add time-window detection (5 failures within 2 minutes is more suspicious than 5 across a day)
- Store alerts in SQLite to integrate with my threat-intelligence-dashboard project