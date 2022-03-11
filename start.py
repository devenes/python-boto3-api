from flask import Flask, request, jsonify
from config import config
import logging
import boto3


app = Flask(__name__)
logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)


# Endpoint: http://<api_host>:<api_port>/ec2/start
@app.route("/ec2/start", methods=["POST", "GET"])
def start_ec2_instances():
    try:
        aws_access_key_id = request.args.get("aws_access_key_id")
        aws_secret_access_key = request.args.get("aws_secret_access_key")
        region_name = request.args.get("region_name")
        InstanceIds = request.args.get("InstanceId")
        client = boto3.client('ec2',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              region_name=region_name,
                              )

    except Exception as error:
        print(str(error))
        return jsonify({'Error': "Unexpected Error occured"}), 500

    response = client.describe_instances()
    InstanceIds = []
    for instance in response["Reservations"][0]["Instances"]:
        InstanceIds.append(instance["InstanceId"])

    response = client.start_instances(
        InstanceIds=InstanceIds
    )

    print(response)
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)
