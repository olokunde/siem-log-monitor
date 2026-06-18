import csv
from collections import defaultdict

LOG_FILE = "sample_security_logs.txt"
ALERT_FILE = "alerts.csv"

failed_attempts = defaultdict(int)
alerts = []

with open(LOG_FILE, "r") as file:
    logs = file.readlines()

for log in logs:
    parts = log.strip().split()

    if len(parts) < 4:
        continue

    event = parts[2]
    ip_address = parts[3]

    if event == "LOGIN_FAILED":
        failed_attempts[ip_address] += 1

for ip, count in failed_attempts.items():
    if count >= 3:
        alerts.append([ip, count, "Potential Brute Force Attack"])

with open(ALERT_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["IP Address", "Failed Attempts", "Alert"])
    writer.writerows(alerts)

print("\n===== SIEM SECURITY REPORT =====")

total_failed = sum(failed_attempts.values())

print(f"Unique suspicious IPs: {len(alerts)}")
print(f"Total failed logins: {total_failed}")

if alerts:
    print("\nAlerts Generated:")
    for alert in alerts:
        print(
            f"IP: {alert[0]} | Failed Attempts: {alert[1]} | {alert[2]}"
        )
else:
    print("No alerts detected.")

print(f"\nResults saved to {ALERT_FILE}")