import json
from load_data import upload_to_aws
from datetime import datetime
import csv
def lambda_handler(event,context):
    dt_string = datetime.now().strftime("%Y-%m-%d")
    csv_file_name =  'twitter-data-raw_'+dt_string +'.csv'
    header = ["id","text"]
    with open("/tmp/out.csv","w+") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(event)
        f.close()
    url = upload_to_aws("/tmp/out.csv", "aws-data-pipeline-team3", csv_file_name)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": url # invoke layer function
        }),
    }
