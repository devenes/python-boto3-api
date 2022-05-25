# Python Boto3 API

![api](./readme/boto3.jpg)

### Python API uses the Flask and Boto3 libraries. It has instance listing, instance start, instance stop, instance create and instance terminate features; It has 5 endpoints communicating with EC2 service on AWS.

---

## 📝 Features

- [Create a new instance](#create_instance)
- [List instances](#list_instance)
- [Start an instance](#start_instance)
- [Stop an instance](#stop_instance)
- [Terminate an instance](#terminate_instance)


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
