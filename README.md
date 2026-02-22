📦 Cloud Backup Validator

A Python-based cloud backup integrity validation system built using AWS S3.
This project uploads files to S3, restores them, verifies data integrity using hashing, and simulates corruption scenarios.

---

🚀 Project Overview

Cloud Backup Validator ensures that files stored in the cloud remain unaltered during backup and restore operations.

It performs:

* ✅ File upload to AWS S3
* ✅ File restoration from S3
* ✅ Integrity verification using SHA-256 hashing
* ✅ Metadata logging
* ✅ Corruption simulation testing

---

🛠 Tech Stack

* Python 3.11
* AWS S3
* Boto3 (AWS SDK for Python)
* Git & GitHub

---

📁 Project Structure

```
cloud_backup_validator/
│
├── main.py
├── uploader.py
├── simulator.py
├── metadata.json
│
├── original_files/
│   └── sample.txt
│
├── restored_files/
│   └── sample.txt
```

---

⚙️ Setup Instructions

 1️⃣ Install Dependencies

```bash
pip install boto3
```

---

2️⃣ Configure AWS Credentials

Run:

```bash
aws configure
```

Enter:

* Access Key ID
* Secret Access Key
* Region: `us-east-1`
* Output format: `json`

---

3️⃣ Create S3 Bucket

Create an S3 bucket in AWS Console (example):

```
cloud-backup-validator-yourname
```

Update bucket name inside `main.py`.

---

▶️ How to Run

🔹 Full Backup + Validation

```bash
python main.py
```

This will:

* Upload file
* Restore file
* Verify integrity

---

🔹 Validate Only

```bash
python main.py validate
```

This checks integrity without re-uploading.

---

🔹 Simulate Corruption

```bash
python main.py corrupt
```

This:

* Restores file
* Injects corrupted data
* Fails integrity check

---

🔐 How Integrity Verification Works

1. Original file hash is generated using SHA-256.
2. File is uploaded to S3.
3. File is restored from S3.
4. Restored file hash is generated.
5. Both hashes are compared.

If hashes match → ✅ Integrity Verified
If hashes differ → ❌ Integrity Check Failed

---

🧪 Test Cases Implemented

* Test Case 1: Normal backup and validation
* Test Case 2: Validation without upload
* Test Case 3: Corruption simulation

---

📌 Example Output

```
✅ Integrity Verified
```

or

```
❌ Integrity Check Failed
```

---

🔮 Future Improvements

* Add versioning support
* Encrypt files before upload
* Add logging system
* Create a simple web dashboard
* Support multiple file uploads

---

👩‍💻 Author

Shusmitha Nallamothu
Cloud Computing / Python Project

---

📄 License

This project is for educational and learning purposes.


