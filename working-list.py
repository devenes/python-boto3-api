from flask import Flask, Response, request, jsonify, make_response
from config import config
import logging
import boto3


app = Flask(__name__)
logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)


# Endpoint-1: http: // <api_host > : < api_port > /ec2/list
@app.route('/ec2/list', methods=['POST', 'GET'])
def aws_list():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    client = boto3.client('ec2',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name
                          )

    # except Exception as error:
    #     print(str(error))
    #     return jsonify({'Error': "Unexpected Error occured"}), 500

    instances = client.describe_instances()
    output = []
    for reservation in instances['Reservations']:
        output.extend([{'id': instance['InstanceId'],
                        "instance-type": instance['InstanceType'],
                        "instance-state": instance['State']['Name']}
                       for instance in reservation['Instances']])

    print(output)
    return jsonify(output), 200


if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)
