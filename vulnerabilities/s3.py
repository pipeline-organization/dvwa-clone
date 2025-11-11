# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkja")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)




var pg_port=1212;
var pg_host="gitguardians.com:9082/BLUDB";
var pg_user="root";
var pg_pass="sup3rstr0ngpass1ForGG";

var mongo_uri = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority";


apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: key-private
data:
  key.private: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlDV2dJQkFBS0JnR2lLd2tiSnBocjB5Y2JRSXB1R3BlRmJpa0t6T2hxVGwxbnpBbGpCb1h2OFNNRFUzbVluCjFHemR5Y2hFdDd5dFJBbFowYnFObGdVMlBneU5IUjRHcE1oWkFsY0w3aGlpTUludHJTZ05YVnFMcFJDUFVQMWUKM3krbHhGMXo3Smc2TUJXMHYraVVvK3dmelJLeTBwajdvOWFMNEVaQ1dJT0VTMHY1TGRSNmVNdlJBZ01CQUFFQwpnWUFwM3FsQXdMS09TVXduSEdVLzlRV3E1SWJUZ0FUZGNBOUdMMVhaUm5QdXZIUkhCdnFyMzNmc3drZDJ0azhBCmVrU3RtaE90cTlkUjd3K2E1MG1xSk84SjYzZlVOMFg0b3Bzc0RDSHJoaHlHa2RaVi9jWXA4dkpYTE9qT3NjenkKa3Y2YkVURDNGQkRkd2RnYTN6S2Fkc3BneVlOUHc0RC9JZjVrUFZtb2JmcXZnUUpCQUsvL0hpM1lhMHZMcUtLUApWVlV0L25GczNQWkxEMmYwdzNkSVRXU091Ylp0Nm1sa2xWWHUvN0hKRGFFZW9BRWFjZjh2dXdPVVl3RjdIMkYzCmQ4WXVsalVDUVFDWUVHbFViV0RLRVdnTW8yZS9OTzZTUUkxSlViSEw0ZEd6REp1ZkRaM3BHZmRVNmh1NFdTWDgKV3FqWnRLaVpiU2JmTXprc3FDc1gzWFNtdHJJbEtXS3RBa0EvRkIvNzdJSmdVeWtvd2xpaVErN2JObHBueC9WSQpuQmhtcXpwWjNUSEFxZHFIVmE2VWN5bWZ6ZUNkcTcxTFIvQXR0eXkvRnJMNWQraUNaWEEvVHJrMUFrQm12TC9OCk1ORHg5T3l0alVFczZDQS9ZNm1SWGNhWUR3dlV3ckhwdGhONFIvall3QXJXZERTNzJLeTMyZDBITzczRmt5QVAKMGRhN212MlRIV0FpeDJGSkFrQmlGejVTUGV2MUlFa3RpejEyb0M2eE1jZDZhZ3I5N1UzeHhxS0RBRnBPNHRLaAozUUZwSzNDUndlWmJUb2s1aFo1dnljaG9FeVhLeENkS0RwNzFpNlhTCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t