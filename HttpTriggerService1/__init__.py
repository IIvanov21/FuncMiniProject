import logging

import azure.functions as func
import requests
import uuid
from azure.cosmos import exceptions, CosmosClient, PartitionKey, partition_key

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #Initialize the Cosmos client
    endpoint = 'https://ivo.documents.azure.com:443/'
    key = 'dtzlJ9YN0KNenbNqFABz2COiV5drjvhUT5qPUMmvgl1sZlyQtUXFHIdRW1hkq1pCOaxxoGh1AoBsV8vafrTs1A=='

    #Create cosmos client
    client=CosmosClient(endpoint,key)

    #Create database
    database_name='MiniProjectDatabase'
    database=client.create_database_if_not_exists(id=database_name)

    #Create a container
    container_name='Generated Username'
    container=database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
    )
    #Get service results
    result_str=requests.get('https://miniprojectfunc.azurewebsites.net/api/HttpTriggerService2?code=aIJ0p43Ug6h8VYXg4rgWrNhqbQKguwfFRrplp6kgV6PhFJ12Pnl1hA==')
    result_int=requests.get('https://miniprojectfunc.azurewebsites.net/api/HttpTriggerService3?code=CUEyW23Waioob2pm1maPaq3ikICb/4taBaKaVa8Xve/eeHW471MNuA==')
    logging.info('Requests made.')
    username=str(result_str.text+result_int.text)
    #Create container item and push it
    container_item={'id' : 'username_id ' + str(uuid.uuid4()),
        'username': username}
    container.create_item(body=container_item)
    #Return result
    return func.HttpResponse(username,status_code=200)
