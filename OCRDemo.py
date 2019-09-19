# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from HWOcrClientAKSK import HWOcrClientAKSK
from HWOcrClientToken import HWOcrClientToken

if __name__ == '__main__':
    '''
    Token demo code
   '''

    username = "rdx_aaa"
    password = "JdibA12344321"
    domain_name = "rdx_aaa"  # if the user isn't IAM user, domain_name is the same with username
    region = "cn-north-4"  # cn-north-1,cn-east-2 etc.
    endpoint="ocr.cn-north-4.myhuaweicloud.com"
    option={}
    option["side"]="front"
    try:
       ocrClient=HWOcrClientToken(domain_name,username,password,region,endpoint)
       response=ocrClient.request_ocr_service_base64('/v1.0/ocr/general-text','./data/general-text-demo.jpg')
       print("Status code:"+str(response.status_code)+" content:"+response.text)
    except ValueError as e:
       print(e)



    '''
    AK SK demo code
   '''

    AK="3R2JJLK3INE4NA33LXPZ"  #AK from authentication
    SK="HMwwHr0JsaJ76I11fHbwA8ACJIUam80d5DzTcMj6"   #SK from authentication
    endpoint="ocr.cn-north-4.myhuaweicloud.com"  #http endpoint information
    ocr_client=HWOcrClientAKSK(AK,SK,endpoint)  #initialize ocr_client from ak,sk and endpoint information
    option={}
    option["side"]="front"
    try:
       response=ocr_client.request_ocr_service_base64("/v1.0/ocr/id-card",'./data/id-card-demo.png',option) #call OCR interface to recognize picture
       print("Status code:"+str(response.status_code)+" content:"+response.text)
    except ValueError as e:
       print(e)

