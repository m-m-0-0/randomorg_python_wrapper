import requests
import json
from time import sleep
import copy 

API_URL = "https://api.random.org/json-rpc/1/invoke"
BASE_REQ = {"jsonrpc": "2.0", "id": 0, "params": {} }

class api_exception(Exception):
    pass

def buildRequest(basereq, *args, method=""):
    reqargs = copy.deepcopy(basereq)
    reqargs["method"] = method

    if len(args) == 0:
        return reqargs

    params = args[0]
    del params["self"]

    for param in params.items():
        key,value = param
        reqargs["params"][key] = value
    return reqargs

def apiRequest(reqargs):
    request = requests.post(API_URL, json = reqargs)
    response = json.loads(request.text)
    statuscode = request.status_code
    try:
        errorcode = response["error"]["code"]
        errormess = response["error"]["message"]

        raise api_exception("%s: %s"%(errorcode,errormess))
    
    except api_exception:
        raise
    except:
        pass

    if statuscode == 200:
        return response
    else:
        raise api_exception(statuscode)

class Randomorg:
    def __init__(self, apiKey):
        self.basereq = copy.deepcopy(BASE_REQ)
        self.basereq["params"]["apiKey"] = apiKey
        req = requests.post(API_URL, json = buildRequest(self.basereq, method="getUsage"))
        
        if req.status_code == 200:
            pass
        else:
            raise api_exception(req.status_code)
        
        response = json.loads(req.text)
        
        try:
            errorcode = response["error"]["code"]
            errormess = response["error"]["message"]
            raise api_exception("%s: %s"%(errorcode,errormess))

        except api_exception:
            raise
        except:
            pass

        if response["result"]["status"] == "stopped":
            raise api_exception("Api key is stopped.")
       
        if response["result"]["requestsLeft"] == 0:
            raise api_exception("Requests limit reached.")

        if response["result"]["bitsLeft"] == 0:
            print("WARNING: bits limit reached.")

    def status(self):
        response = apiRequest(buildRequest(self.basereq, method="getUsage"))
        return response["result"]["status"]

    def bitsLeft(self):
        response = apiRequest(buildRequest(self.basereq, method="getUsage"))
        return response["result"]["bitsLeft"]

    def requestsLeft(self):
        response = apiRequest(buildRequest(self.basereq, method="getUsage"))
        return response["result"]["requestsLeft"]

    def generateIntegers(self, n, min, max, replacement="true", base="10"):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateIntegers"))
        return response["result"]["random"]["data"]

    def generateDecimalFractions(self, n, decimalPlaces, replacement="true"):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateDecimalFractions"))
        return response["result"]["random"]["data"]

    def generateGaussians(self, n, mean, standardDeviation, significantDigits):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateGaussians"))
        return response["result"]["random"]["data"]

    def generateStrings(self, n, length, characters, replacement="true"):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateStrings"))
        return response["result"]["random"]["data"]

    def generateUUIDs(self, n):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateUUIDs"))
        return response["result"]["random"]["data"]

    def generateBlobs(self, n, size, format="base64"):
        response = apiRequest(buildRequest(self.basereq, locals(), method = "generateBlobs"))
        return response["result"]["random"]["data"]
