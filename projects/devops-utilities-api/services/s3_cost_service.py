def get_s3_cost_estimate():
    buckets = s3_client.list_buckets()["Buckets"]

    bucket_costs = {}
    total_s3_cost = 0
    S3_STANDARD_PRICE_PER_GB = 0.023

    for bucket in buckets:
        bucket_name = bucket["Name"]

        metrics = cloudwatch.get_metric_statistics(
            Namespace="AWS/S3",
            MetricName="BucketSizeBytes",
            Dimensions=[
                {"Name": "BucketName", "Value": bucket_name},
                {"Name": "StorageType", "Value": "StandardStorage"}
            ],
            StartTime=datetime.utcnow() - timedelta(days=2),
            EndTime=datetime.utcnow(),
            Period=86400,
            Statistics=["Average"]
        )

        if not metrics["Datapoints"]:
            size_gb = 0
        else:
            size_bytes = metrics["Datapoints"][0]["Average"]
            size_gb = round(size_bytes / (1024 ** 3), 2)

        monthly_cost = round(size_gb * S3_STANDARD_PRICE_PER_GB, 2)

        bucket_costs[bucket_name] = {
            "size_gb": size_gb,
            "monthly_cost_usd": monthly_cost
        }

        total_s3_cost += monthly_cost

    return {
        "service": "S3",
        "currency": "USD (estimated)",
        "total_estimated_monthly_cost": round(total_s3_cost, 2),
        "buckets": bucket_costs
    }