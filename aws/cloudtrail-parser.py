import json
import os

# ----------- CONFIG ------------
CLOUDTRAIL_LOG_PATH = "./aws/cloudtrail_sample.json"  # Replace with your file
FILTER_EVENTS = ["ConsoleLogin", "AssumeRole"]
# -------------------------------

def load_cloudtrail_log(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data.get("Records", [])

def parse_event(event):
    event_time = event.get("eventTime", "-")
    event_name = event.get("eventName", "-")
    user_identity = event.get("userIdentity", {})
    source_ip = event.get("sourceIPAddress", "-")
    result = event.get("responseElements", {})
    error_code = event.get("errorCode", "Success")

    username = user_identity.get("userName") or user_identity.get("arn") or "-"
    auth_result = "Failure" if error_code != "Success" else "Success"

    print(f"[{event_time}] - {event_name} | User: {username} | IP: {source_ip} | Result: {auth_result}")

def main():
    if not os.path.exists(CLOUDTRAIL_LOG_PATH):
        print(f"❌ File not found: {CLOUDTRAIL_LOG_PATH}")
        return

    records = load_cloudtrail_log(CLOUDTRAIL_LOG_PATH)
    print(f"🔍 Found {len(records)} events in the log")

    for record in records:
        if record.get("eventName") in FILTER_EVENTS:
            parse_event(record)

if __name__ == "__main__":
    main()

