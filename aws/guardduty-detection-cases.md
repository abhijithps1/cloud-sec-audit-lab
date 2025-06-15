# 🛡️ AWS GuardDuty Detection Cases

This document highlights and explains different AWS GuardDuty alerts triggered in a sample AWS environment.  
Each case includes:
- 📌 Alert name & description
- 🎯 What caused it (test/simulation)
- 📊 Severity level
- 🔍 How to investigate
- ✅ Recommended response

---

## 🔔 Detection Case 1: UnauthorizedAccess:IAMUser/ConsoleLogin

- **Description**: A successful login was made using valid IAM credentials from an unusual location.
- **Test Method**: Logged in from a different region/IP using a test IAM user.
- **Severity**: 🟡 Medium
- **Why Triggered**: Login came from an IP range not previously associated with this user.
- **Investigation**:
  - Review CloudTrail event: `ConsoleLogin`
  - Check IP reputation using threat intel tools
- **Response**:
  - Verify with user
  - Enable MFA
  - Rotate credentials if suspicious

---

## 🔔 Detection Case 2: Recon:EC2/PortProbeUnprotectedPort

- **Description**: GuardDuty detected a port scan targeting an EC2 instance.
- **Test Method**: Used `nmap` from a public IP to scan open ports.
- **Severity**: 🔴 High
- **Why Triggered**: The instance had open ports (e.g., 22, 3389) exposed to the internet.
- **Investigation**:
  - Check Security Groups of affected instance
  - Review CloudTrail for any remote access
- **Response**:
  - Restrict public access
  - Apply NACLs or modify SGs
  - Set up VPC flow logs for monitoring

---

## 🔔 Detection Case 3: CryptoCurrency:EC2/BitcoinTool.B!DNS

- **Description**: An EC2 instance was communicating with known Bitcoin mining domains.
- **Test Method**: Deployed a test container running a known mining tool for simulation.
- **Severity**: 🔴 High
- **Why Triggered**: DNS requests to mining pools were detected by GuardDuty.
- **Investigation**:
  - Review VPC flow logs and DNS logs
  - Identify process/container causing traffic
- **Response**:
  - Quarantine instance
  - Terminate suspicious workload
  - Review IAM roles attached to the instance

---

## 📌 Common Actions to Tune & Respond to Alerts

- 📘 Enable CloudTrail + VPC Flow Logs for context
- 🔍 Use Athena or OpenSearch to query logs
- 🔐 Use IAM Service Control Policies (SCP) to restrict risky behaviors
- 📡 Use EventBridge to automate GuardDuty alerts to Slack/SIEM

---

## 🧠 Learning Note

You can simulate more detections using tools like:
- [`CloudGoat`](https://github.com/RhinoSecurityLabs/cloudgoat)
- [`AWS PenTesting Methodology`](https://github.com/toniblyx/my-aws-pentest-playbook)

---

📝 _Maintained by Abhijith as part of the Cloud Security Audit Lab_
