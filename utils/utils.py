import allure
import requests
import curlify
import logging
from allure_commons.types import AttachmentType

BASE_URL = 'https://demowebshop.tricentis.com/'


def post_request(url, **kwargs):
    url = BASE_URL + url
    with allure.step(f"POST {url}"):
        responce = requests.post(url, **kwargs)
        curl = curlify.to_curl(responce.request)
        allure.attach(body= curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(responce.request))
        return responce
