
from fastapi import APIRouter, HTTPException


router = APIRouter()
@router.get("/ec2", status_code=200)
def list_ec2_instances():
    try:
        return get_ec2_instances()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from services.aws_service import get_bucket_info, get_ec2_instances

@router.get("/s3",status_code=200)
def get_buckets():

    try:
        buckets_info = get_bucket_info()
        return buckets_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )



from services.ec2_cost_service import get_ec2_cost_estimate


@router.get("/ec2/cost", status_code=200)
def ec2_cost():
    return get_ec2_cost_estimate()


from services.s3_cost_service import get_s3_cost_estimate


@router.get("/s3/cost", status_code=200)
def s3_cost():
    return  get_s3_cost_estimate



from services.cost_summary_service import get_aws_cost_summary

@router.get("/aws/cost/summary", status_code=200)
def aws_cost_summary():
    return get_aws_cost_summary()


from services.aws_email_alert_service import aws_email_alert



@router.get("/aws/email-alert", status_code=200)
def aws_email_alert_api():
    return aws_email_alert()


from services.dry_run_service import ec2_dry_run, s3_dry_run


@router.get("/ec2/dry-run", status_code=200)
def ec2_dry_run_api(instance_id: str):
    return ec2_dry_run(instance_id)

@router.get("/s3/dry-run", status_code=200)
def s3_dry_run_api(bucket_name: str):
    return s3_dry_run(bucket_name)













