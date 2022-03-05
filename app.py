# Flask kütüphanesini kullanarak bir Python API geliştirin. Gelişterecek olduğunuz API, Boto3 kütüphanesini kullanarak, AWS'in EC2 servisi ile haberleşmeli ve listeleme, Instance başlatma ve Instance durdurma yeteneklerine ve aşağıda yer alan 3 endpointe sahip olmalı


# Endpoint-1: http: // <api_host > : < api_port > /ec2/list
# Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı
# aws_access_key_id
# aws_secret_access_key
# region_name
# Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir
# Query Parameter
# URL Parameter
# JSON Body
# Yukarıda yer alan 3 yöntem biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu region'da var olan EC2 instancelara ait InstanceId değerlerinin bir listesini alabilmeli.


# Endpoint-2: http: // <api_host > : < api_port > /ec2/start
# Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı
# aws_access_key_id
# aws_secret_access_key
# region_name
# InstanceId
# Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir
# Query Parameter
# URL Parameter
# JSON Body
# Yukarıda yer alan 3 yöntem biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu InstanceId değerine sahip olan EC2 instance'ı başlatabilmelidir.


# Endpoint-3: http: // <api_host > : < api_port > /ec2/stop
# Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı
# aws_access_key_id
# aws_secret_access_key
# region_name
# InstanceId
# Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir
# Query Parameter
# URL Parameter
# JSON Body
# Yukarıda yer alan 3 yöntemden biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu InstanceId değerine sahip olan EC2 instance'ı durdurabilmelidir.


# Geliştirmeyi tamamladıktan sonra ilgili dosyaları zip olarak gönderebilirsiniz.
# Başarılar dilerim.


# Opsiyonel
# Burada yer alan taskleri gerçekleştirmeniz ekstra puan almanızı sağlayacaktır.
# Uygun HTTP metotları kullanarak, farklı metotlar ile istek atılmasını engellemek.
# API host ve port bilgilerini harici bir config dosyasından okumak.
# API'a farklı yöntemler ile parametre alabilme yeteneği kazandırmak.
# Kullanıcıya detaylı bilgi içeren JSON formatında response dönebilmek.
# API response status codelarını düzenleyerek ilgili durumlarda doğru status code dönebilmek.
# Uygulamanızı geliştirirken kullanmış olduğunuz Python paketlerini içeren bir requirements.txt dosyası oluşturmak.
# Log dosyası oluşturmak.
# Try-Except yapısını kullanarak hata oluşabilecek durumları yakalayarak, karşılaşılan hataları kullanıcıya response olarak dönebilmek.
# Kaynak kodları bir versiyon kontrol sistemi uygulamasında(Github, Gitlab etc.) yayınlamak.

from urllib import response
from flask import Flask, render_template, request, jsonify, json, make_response
import boto3
from config import config


app = Flask(__name__)

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html


@app.route("/", methods=["GET"])
def home():
    return """
        <h3>
            Segmind Assignement
        </h3>
        <ul>
        <li>
            Creating a new instance can be done using the API at `/api/create` Both the GET and POST request works
            You specify the instance type by providing the query param `instance_type`
        </li>
        <li>
            The status of the current instance can be fetched using the API `/api/status`
            The API returns the status of all the instances
            To get the status of a perticular instance please provide the instance id using the query param instance_id
        </li>
        </ul>
        Please refer readme md for details
    """


@app.route('/ec2/list', methods=['GET'])
def list_ec2():
    if request.method == 'GET':
        try:
            client = boto3.client('ec2', region_name=config.aws_region_name,
                                  aws_access_key_id=config.aws_access_key_id,
                                  aws_secret_access_key=config.aws_secret_access_key
                                  )
            response = client.describe_instances()
            return jsonify(response)
        except Exception as error:
            print(str(error))
            return jsonify({'error': 'Unexpected Error occured'}), 500


@ app.route('/ec2/start', methods=['GET'])
def start_ec2():
    if request.method == 'GET':
        try:
            client = boto3.client('ec2', region_name=config.region_name,
                                  aws_access_key_id=config.aws_access_key_id,
                                  aws_secret_access_key=config.aws_secret_access_key)
            response = client.start_instances(InstanceIds=[config.instance_id])
            return jsonify(response)
        except Exception as e:
            return jsonify(e)


@ app.route('/ec2/stop', methods=['GET'])
def stop_ec2():
    if request.method == 'GET':
        try:
            client = boto3.client('ec2', region_name=config.region_name,
                                  aws_access_key_id=config.aws_access_key_id,
                                  aws_secret_access_key=config.aws_secret_access_key)
            response = client.stop_instances(InstanceIds=[config.instance_id])
            return jsonify(response)
        except Exception as e:
            return jsonify(e)


client = boto3.client('ec2',
                      aws_access_key_id=config['aws_access_key_id'],
                      aws_secret_access_key=config['aws_secret_access_key'],
                      region_name=config['region_name']
                      )

response = client.describe_instances(
    Filters=[
        {
            'Name': 'key:Name',
            'Values': [
                '*'
            ]
        }
    ]
)

InstanceIds = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        InstanceIds.append(instance['InstanceId'])

response = client.start_instances(
    InstanceIds=InstanceIds
)

print(response)


# Add a statement to run the Flask application which can be reached from any host on port 80
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host=config.config["host"], port=config.config["port"], debug=True)
