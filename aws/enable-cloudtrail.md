# 🛡️ Enable AWS CloudTrail

CloudTrail is an essential AWS service for logging all API calls and activities in your account. This guide helps you enable CloudTrail for security auditing and incident response.

---

## 🔧 Option 1: Enable CloudTrail via AWS Console

1. Sign in to the [AWS Console](https://console.aws.amazon.com/)
2. Navigate to **CloudTrail** → Click on **"Trails"**
3. Click **Create Trail**
4. Provide:
   - **Trail name**: `OrgTrail` or `DefaultTrail`
   - **Apply trail to all regions**: ✅ Yes
   - **Read/Write events**: Choose **All**
   - **Storage location**: Create a new or use existing **S3 bucket**
5. Under **Event type**:
   - ✅ Management Events (recommended)
   - ✅ Data Events (for S3, Lambda if needed)
6. Click **Create Trail**

---

## 💻 Option 2: Enable CloudTrail via AWS CLI

### 🔹 Step 1: Create an S3 Bucket
### ```bash
aws s3api create-bucket --bucket my-cloudtrail-bucket --region us-east-1

---
### 🔹 Step 2: Enable CloudTrail
### ```bash
aws cloudtrail create-trail \
  --name my-trail \
  --s3-bucket-name my-cloudtrail-bucket \
  --is-multi-region-trail

### 🔹 Step 3: Start Logging
### ```bash
aws cloudtrail start-logging --name my-trail

### 🔹 Verify Trail Status
### ```bash
aws cloudtrail get-trail-status --name my-trail


📁 Where Logs Go
s3://my-cloudtrail-bucket/AWSLogs/{account-id}/CloudTrail/{region}/YYYY/MM/DD/

