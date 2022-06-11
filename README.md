<div align="center" id="top"> 
  <img src="./readme/boto3.jpg" alt="Python Boto3 Api" />

&#xa0;

  <!-- <a href="https://pythonboto3api.netlify.app">Demo</a> -->
</div>

<h1 align="center">Python Boto3 API for AWS</h1>

<p align="center">
  <img src="https://badges.aleen42.com/src/docker.svg" alt="Docker" />
  <img src="https://badges.aleen42.com/src/python.svg" alt="Python" />
  <img src="https://badges.aleen42.com/src/amazon.svg" alt="AWS" />  
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/devenes/python-boto3-api?color=blue">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/devenes/python-boto3-api?color=green">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/devenes/python-boto3-api?color=purple">
  <img alt="License" src="https://img.shields.io/github/license/devenes/python-boto3-api?color=orange">
  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/devenes/python-boto3-api?color=56BEB8" /> -->
  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/devenes/python-boto3-api?color=56BEB8" /> -->
  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/devenes/python-boto3-api?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Python Boto3 Api 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/devenes" target="_blank">Author</a>
</p>

<br>

## :dart: About

Python API uses the Flask and Boto3 libraries. It has instance listing, instance start, instance stop, instance create and instance terminate features; It has 5 endpoints communicating with EC2 service on AWS.

## :sparkles: Features

- [:dart: About](#dart-about)
- [:sparkles: Features](#sparkles-features)
- [:rocket: Technologies](#rocket-technologies)
- [:white_check_mark: Requirements](#white_check_mark-requirements)
- [:checkered_flag: Starting](#checkered_flag-starting)
- [Create Instance <a name = "create_instance"></a>](#create-instance-)
- [List Instances <a name = "list_instance"></a>](#list-instances-)
- [Start Instance <a name = "start_instance"></a>](#start-instance-)
- [Stop Instance <a name = "stop_instance"></a>](#stop-instance-)
- [Terminate Instance <a name = "terminate_instance"></a>](#terminate-instance-)
- [Resources](#resources)
- [:memo: License](#memo-license)

## :rocket: Technologies

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Boto3](https://boto3.amazonaws.com/)
- [AWS](https://aws.amazon.com/)
- [Docker](https://www.docker.com/)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

## :checkered_flag: Starting

```bash
# Clone this project
git clone https://github.com/devenes/python-boto3-api

# Access
cd python-boto3-api

# Install dependencies
pip install -r requirements.txt

# Run the project
python app.py

# The server will initialize in the <http://localhost:8080>
```

## Create Instance <a name = "create_instance"></a>

You send a POST request to the `create` endpoint with the following parameters and it will create Ubuntu EC2 instance. You create your EC2 Instance with the `region_name`, `KeyName` and `SecurityGroupId` parameters you send in the request.

```
http://<api_host>:<api_port>/ec2/create
```

| Parameter               | Type     | Description           |
| :---------------------- | :------- | :-------------------- |
| `aws_access_key_id`     | `string` | AWS Access Key ID     |
| `aws_secret_access_key` | `string` | AWS Secret Access Key |
| `region_name`           | `string` | AWS Region Name       |
| `KeyName`               | `string` | AWS Key Name          |
| `SecurityGroupId`       | `string` | AWS Security Group ID |

---

## List Instances <a name = "list_instance"></a>

You send a GET request to the `list` endpoint by entering the following parameters, then you can list all the instances and their status in your AWS account in the region you specify.

```
http://<api_host>:<api_port>/ec2/list
```

| Parameter               | Type     | Description           |
| :---------------------- | :------- | :-------------------- |
| `aws_access_key_id`     | `string` | AWS Access Key ID     |
| `aws_secret_access_key` | `string` | AWS Secret Access Key |
| `region_name`           | `string` | AWS Region Name       |

---

## Start Instance <a name = "start_instance"></a>

You send a POST request to the `start` endpoint by entering the following parameters, and you can start the instance you specified with `instance_id`, in the region you specified with `region_name` and the status of the instance will be changed to `pending` and then to `running`.

```
http://<api_host>:<api_port>/ec2/start
```

| Parameter               | Type     | Description           |
| :---------------------- | :------- | :-------------------- |
| `aws_access_key_id`     | `string` | AWS Access Key ID     |
| `aws_secret_access_key` | `string` | AWS Secret Access Key |
| `region_name`           | `string` | AWS Region Name       |
| `instance_id`           | `string` | Instance ID Number    |

---

## Stop Instance <a name = "stop_instance"></a>

You send a POST request to the `stop` endpoint by entering the following parameters, and you can stop the instance you specified with `instance_id`, in the region you specified with `region_name` and the status of the instance will be changed to `stopping` and then to `stopped`.

```
http://<api_host>:<api_port>/ec2/stop
```

| Parameter               | Type     | Description           |
| :---------------------- | :------- | :-------------------- |
| `aws_access_key_id`     | `string` | AWS Access Key ID     |
| `aws_secret_access_key` | `string` | AWS Secret Access Key |
| `region_name`           | `string` | AWS Region Name       |
| `instance_id`           | `string` | Instance ID Number    |

---

## Terminate Instance <a name = "terminate_instance"></a>

You send a POST request to the `terminate` endpoint by entering the following parameters, and you can terminate the instance you specified with `instance_id`, in the region you specified with `region_name` and the status of the instance will be changed to `shutting-down` and then `terminated`.

```
http://<api_host>:<api_port>/ec2/terminate
```

| Parameter               | Type     | Description           |
| :---------------------- | :------- | :-------------------- |
| `aws_access_key_id`     | `string` | AWS Access Key ID     |
| `aws_secret_access_key` | `string` | AWS Secret Access Key |
| `region_name`           | `string` | AWS Region Name       |
| `instance_id`           | `string` | Instance ID Number    |

## Resources

- [AWS](https://aws.amazon.com/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Boto3](https://boto3.amazonaws.com/)

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/devenes" target="_blank">devenes</a>

&#xa0;

<a href="#top">Back to top</a>
