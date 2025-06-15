# When you run the script now, expected output

Found 3 events in the log

[2025-06-12T14:22:01Z] - ConsoleLogin | User: johndoe | IP: 198.51.100.23 | Result: Success
[2025-06-12T14:45:34Z] - AssumeRole | User: arn:aws:sts::123456789012:assumed-role/Admin/johndoe | IP: 203.0.113.5 | Result: Success
[2025-06-12T15:00:01Z] - ConsoleLogin | User: malicious_user | IP: 144.202.14.12 | Result: Failure
