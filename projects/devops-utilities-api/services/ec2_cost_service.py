import boto3
ec2_client = boto3.client("ec2")
# Approx On-Demand pricing (USD / hour)
INSTANCE_PRICING = {
    "t2.micro": 0.0116,
    "t2.small": 0.023,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}
def get_ec2_cost_estimate():
    response = ec2_client.describe_instances()
    breakdown = {}
    total_monthly_cost = 0
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]
            if instance_type not in breakdown:
                breakdown[instance_type] = {
                    "count": 0,
                    "running": 0,
                    "stopped": 0,
                    "monthly_cost_usd": 0
                }
            breakdown[instance_type]["count"] += 1
            if state == "running":
                breakdown[instance_type]["running"] += 1
            else:
                breakdown[instance_type]["stopped"] += 1
            hourly_price = INSTANCE_PRICING.get(instance_type, 0)
            monthly_price = hourly_price * 24 * 30
            breakdown[instance_type]["monthly_cost_usd"] += monthly_price
            total_monthly_cost += monthly_price
    return {
        "service": "EC2",
        "currency": "USD (estimated)",
        "total_estimated_monthly_cost": round(total_monthly_cost, 2),
        "breakdown": breakdown
    }





    