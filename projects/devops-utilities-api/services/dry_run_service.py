def ec2_dry_run(instance_id):
    return {
        "resource": "EC2",
        "instance_id": instance_id,
        "action": "terminate",
        "dry_run": True,
        "message": f"EC2 instance {instance_id} would be terminated (dry-run only)"
    }


def s3_dry_run(bucket_name):
    return {
        "resource": "S3",
        "bucket_name": bucket_name,
        "action": "delete",
        "dry_run": True,
        "message": f"S3 bucket {bucket_name} would be deleted (dry-run only)"
    }