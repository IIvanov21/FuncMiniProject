import logging

import azure.functions as func

import string
import random
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters=string.ascii_letters
    result_str = ''.join((random.choice(letters) for i in range(5)))
    return func.HttpResponse(result_str)
