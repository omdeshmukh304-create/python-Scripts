from services.ec2_cost_service import get_ec2_cost_estimate
from services.s3_cost_service import get_s3_cost_estimate

def get_aws_cost_summary():
    ec2_cost = get_ec2_cost_estimate()
    s3_cost = get_s3_cost_estimate()

    return {
        "currency": "USD (estimated)",
        "services": {
            "ec2": ec2_cost["total_estimated_monthly_cost"],
            "s3": s3_cost["total_estimated_monthly_cost"]
        },
        "total_estimated_monthly_cost": round(
            ec2_cost["total_estimated_monthly_cost"] +
            s3_cost["total_estimated_monthly_cost"], 2
        )
    }