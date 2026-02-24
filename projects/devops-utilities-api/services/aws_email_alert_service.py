from services.aws_service import get_bucket_info, get_ec2_instances
from services.email_service import send_email


def aws_email_alert():

    # ---------- S3 PART ----------

    # Step 1: S3 bucket info lao
    s3_data = get_bucket_info()

    # Step 2: Sirf 90+ days purane buckets lo
    old_buckets = s3_data["old_buckets_names"]

    # ---------- EC2 PART ----------

    # Step 3: EC2 instance info lao
    ec2_data = get_ec2_instances()

    # Step 4: 90+ days purane EC2 instances nikaalo
    old_instances = []

    for instance in ec2_data["instances"]:
        if instance["age_in_days"] >= 90:
            old_instances.append(instance)

    # Step 5: Agar S3 aur EC2 dono empty hain to email mat bhejo
    if len(old_buckets) == 0 and len(old_instances) == 0:
        return {
            "email_sent": False,
            "old_s3_buckets": 0,
            "old_ec2_instances": 0
        }

    # ---------- EMAIL BODY ----------

    email_body = ""

    # Step 6: S3 email section
    if len(old_buckets) > 0:
        email_body = email_body + "S3 BUCKETS OLDER THAN 90 DAYS\n"
        email_body = email_body + "------------------------------\n"

        for bucket in old_buckets:
            email_body = email_body + bucket + "\n"

        email_body = email_body + "\n"

    # Step 7: EC2 email section
    if len(old_instances) > 0:
        email_body = email_body + "EC2 INSTANCES OLDER THAN 90 DAYS\n"
        email_body = email_body + "------------------------------\n"

        for instance in old_instances:
            email_body = (
                email_body
                + instance["instance_id"]
                + " | "
                + instance["state"]
                + " | "
                + str(instance["age_in_days"])
                + " days\n"
            )

    # Step 8: Email bhejo
    send_email(
        subject="AWS Alert: Resources Older Than 90 Days",
        body=email_body
    )

    # Step 9: Response return karo
    return {
        "email_sent": send_email ,
        "old_s3_buckets": len(old_buckets),
        "old_ec2_instances": len(old_instances)
    }