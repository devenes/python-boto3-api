# Python-Boto3-API

Flask kütüphanesini kullanarak bir Python API geliştirin. Gelişterecek olduğunuz API, Boto3 kütüphanesini kullanarak, AWS'in EC2 servisi ile haberleşmeli ve listeleme, Instance başlatma ve Instance durdurma yeteneklerine ve aşağıda yer alan 3 endpointe sahip olmalı;


- Endpoint-1: http://<api_host>:<api_port>/ec2/list
- 
Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı;
aws_access_key_id
aws_secret_access_key
region_name
Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir;
Query Parameter
URL Parameter
JSON Body
Yukarıda yer alan 3 yöntem biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu region'da var olan EC2 instancelara ait InstanceId değerlerinin bir listesini alabilmeli.


- Endpoint-2: http://<api_host>:<api_port>/ec2/start

Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı;
aws_access_key_id
aws_secret_access_key
region_name
InstanceId
Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir;
Query Parameter
URL Parameter
JSON Body
Yukarıda yer alan 3 yöntem biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu InstanceId değerine sahip olan EC2 instance'ı başlatabilmelidir.


- Endpoint-3: http://<api_host>:<api_port>/ec2/stop

Bu endpoint kullanıcıdan aşağıda yer alan parametreleri almalı;
aws_access_key_id
aws_secret_access_key
region_name
InstanceId
Parametreler kullanıcıdan 3 farklı yöntem ile alınabilir;
Query Parameter
URL Parameter
JSON Body
Yukarıda yer alan 3 yöntemden biri ile kullanıcıdan bu parametreleri almanız yeterli olacaktır. Kullanıcı, bu endpointe ilgili parametreler ile istek atarak, iletmiş olduğu InstanceId değerine sahip olan EC2 instance'ı durdurabilmelidir.

## Opsiyonel 

Burada yer alan taskleri gerçekleştirmeniz ekstra puan almanızı sağlayacaktır.
Uygun HTTP metotları kullanarak, farklı metotlar ile istek atılmasını engellemek.
API host ve port bilgilerini harici bir config dosyasından okumak.
API'a farklı yöntemler ile parametre alabilme yeteneği kazandırmak.
Kullanıcıya detaylı bilgi içeren JSON formatında response dönebilmek.
API response status codelarını düzenleyerek ilgili durumlarda doğru status code dönebilmek.
Uygulamanızı geliştirirken kullanmış olduğunuz Python paketlerini içeren bir requirements.txt dosyası oluşturmak.
Log dosyası oluşturmak.
Try-Except yapısını kullanarak hata oluşabilecek durumları yakalayarak, karşılaşılan hataları kullanıcıya response olarak dönebilmek.
Kaynak kodları bir versiyon kontrol sistemi uygulamasında (Github, Gitlab etc.) yayınlamak.
