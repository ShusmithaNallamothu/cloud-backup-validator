import sys
import time
import json
from datetime import datetime
from uploader import upload_file, restore_file
from simulator import generate_hash

bucket_name = "cloud-backup-validator-shusmitha"
file_path = "original_files/sample.txt"
metadata_file = "backup_metadata.json"


def save_metadata(data):
    try:
        with open(metadata_file, "r") as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    existing_data.append(data)

    with open(metadata_file, "w") as f:
        json.dump(existing_data, f, indent=4)


def full_backup():
    print("---- FULL BACKUP TEST ----")

    original_hash = generate_hash(file_path)
    upload_file(file_path, bucket_name)

    start_time = time.time()
    restore_file(bucket_name, "sample.txt")
    end_time = time.time()

    recovery_time = round(end_time - start_time, 3)

    restored_hash = generate_hash("restored_files/sample.txt")

    status = "Verified" if original_hash == restored_hash else "Failed"

    print("Recovery Time (RTO):", recovery_time, "seconds")
    print("Integrity Status:", status)

    metadata = {
        "filename": "sample.txt",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "original_hash": original_hash,
        "restored_hash": restored_hash,
        "recovery_time_seconds": recovery_time,
        "status": status
    }

    save_metadata(metadata)


def validate_only():
    print("---- VALIDATION ONLY TEST ----")

    original_hash = generate_hash("original_files/sample.txt")
    restored_hash = generate_hash("restored_files/sample.txt")

    status = "Verified" if original_hash == restored_hash else "Failed"
    print("Integrity Status:", status)


def simulate_corruption():
    print("---- SIMULATING CORRUPTION ----")

    with open("restored_files/sample.txt", "a") as f:
        f.write("\nCORRUPTED DATA")

    print("File corrupted successfully.")


if len(sys.argv) > 1:
    if sys.argv[1] == "validate":
        validate_only()
    elif sys.argv[1] == "corrupt":
        simulate_corruption()
    else:
        full_backup()
else:
    full_backup()