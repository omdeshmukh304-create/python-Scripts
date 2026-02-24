import boto3
from datetime import datetime, timezone,timedelta
ec2_client = boto3.client("ec2")
def get_ec2_instances():

    response = ec2_client.describe_instances()
    current_time = datetime.now(timezone.utc)

    instances_list = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            launch_time = instance["LaunchTime"]
            time_passed = current_time - launch_time

            instances_list.append({
                "instance_id": instance["InstanceId"],
                "instance_type": instance["InstanceType"],
                "state": instance["State"]["Name"],
                "launch_time": launch_time.strftime("%Y-%m-%d %H:%M:%S"),
                "age_in_days": time_passed.days,
                "age_in_hours": round(time_passed.total_seconds() / 3600, 2),
                "availability_zone": instance["Placement"]["AvailabilityZone"]
            })

    return {
        "total_instances": len(instances_list),
        "instances": instances_list
    }











def get_bucket_info():

    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    new_buckets = []
    old_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "total_buckets":len(buckets),
        "new_buckets":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_buckets_names":new_buckets,
        "old_buckets_names":old_buckets
    }












