import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    result_int = ''.join((str(random.randint(0,22)) for i in range(5)))
    return func.HttpResponse(result_int)
