from flask import Flask, request, jsonify
from config import config
import logging
import boto3

app = Flask(__name__)

logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level']
)


def get_aws_client(request):
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    return boto3.client('ec2',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name
                        )


# Endpoint: http://<api_host>:<api_port>/ec2/list
@app.route('/ec2/list', methods=['GET'])
def aws_list():
    try:
        client = get_aws_client(request)

        instances = client.describe_instances()
        output = []
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                output.append(
                    {
                        'id': instance['InstanceId'],
                        "instance-type": instance['InstanceType'],
                        "instance-state": instance['State']['Name'],
                        "private-ip": instance['PrivateIpAddress'],
                        "key-name": instance['KeyName'],
                        "image-id": instance['ImageId'],
                        "vpc-id": instance['VpcId'],
                        "subnet-id": instance['SubnetId'],
                        "security-group-ids": instance['SecurityGroups'],
                    }
                )

        print(output)
        return jsonify(output), 200

    except Exception as error:
        print(str(error))
        return jsonify({'Message': "Unexpected Error occured", 'Error': str(error)}), 500


# Endpoint: http://<api_host>:<api_port>/ec2/start
@app.route("/ec2/start", methods=["POST"])
def start_ec2_instances():
    try:
        client = get_aws_client(request)
        InstanceId = request.args.get("InstanceId")

        response = client.start_instances(
            InstanceIds=[InstanceId]
        )

        return jsonify(response["StartingInstances"][0]), 200

    except Exception as error:
        print(str(error))
        return jsonify({'Message': "Unexpected Error occured", 'Error': str(error)}), 500


# Endpoint: http://<api_host>:<api_port>/ec2/stop
@app.route("/ec2/stop", methods=["POST"])
def stop_ec2_instances():
    try:
        client = get_aws_client(request)
        InstanceId = request.args.get("InstanceId")

        response = client.stop_instances(
            InstanceIds=[InstanceId]
        )

        return jsonify(response["StoppingInstances"][0]), 200

    except Exception as error:
        print(str(error))
        return jsonify({'Message': "Unexpected Error occured", 'Error': str(error)}), 500


@app.route("/ec2/create", methods=["POST"])
def create_ec2_instance():
    try:
        client = get_aws_client(request)
        KeyName = request.args.get("KeyName")
        SecurityGroupIds = request.args.get("SecurityGroupId")

        response = client.run_instances(
            ImageId='ami-0fb653ca2d3203ac1',  # Ubuntu Server 20.04, 64-bit x86
            InstanceType='t2.micro',  # 1 vCPU, 1 GB RAM (Free tier ^^)
            MinCount=1,
            MaxCount=1,
            KeyName=KeyName,
            SecurityGroupIds=[SecurityGroupIds]
        )

        print(response)
        return jsonify(response["Instances"][0]), 200

    except Exception as error:
        print(str(error))
        return jsonify({'Message': "Unexpected Error occured", 'Error': str(error)}), 500


@app.route("/ec2/terminate", methods=["POST"])
def terminate_ec2_instance():
    try:
        client = get_aws_client(request)
        InstanceId = request.args.get("InstanceId")

        response = client.terminate_instances(
            InstanceIds=[InstanceId]
        )

        return jsonify(response["TerminatingInstances"][0]), 200

    except Exception as error:
        print(str(error))
        return jsonify({'Message': "Unexpected Error occured", 'Error': str(error)}), 500


if __name__ == "__main__":
    app.run(host=config["host"],
            port=config["port"],
            debug=True)
