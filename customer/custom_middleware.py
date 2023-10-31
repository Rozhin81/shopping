import json
import jwt
import logging
from environs import Env
from rest_framework.response import Response
from django.utils.deprecation import MiddlewareMixin

#Initialize logger
logger = logging.getLogger(__name__)

#Get jwt secret key
env = Env()
env.read_env()
SECRET_KEY = env("JWT_SECRET_KEY")


def create_response(request_id , code , message):
    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """
    try:
        req = str(request_id)
        data = {"data" : message , "code" :int(code) , "request_id" :req}
        return data
    except Exception as creation_error :
        logger.error(f'create_response : {creation_error}')


class CustomMiddleware(MiddlewareMixin) :
    """
    Custom Middleware Class to process a request before it reached the endpoint
    """
    def __init__(self   ,*args,**kwargs) :
        # self.get_response = get_response
        # self.authorization = authorization
        pass

    def __call__(self , request) :
        # response = request.META.get('Authorization')
        return "response"

    def process_request(self , request) :
        """
        Custom middleware handler to check authentication for a user with JWT authentication
        :param request: Request header containing authorization tokens
        :type request: Django Request Object
        :return: HTTP Response if authorization fails, else None
        """
        try : 
            jwt_token = request.headers.get('authorization' ,None)
            logger.info(f'request recievedfor endpoint {str(request.path)}')

            #if token exists
            if jwt_token :
                try:
                    payload = jwt.decode(jwt_token , SECRET_KEY , algorithms=['HS256'])
                    userid = payload['user_id']
                    logger.info(f'request recieved from user by {userid}')
                    return f'request recieved from user by {userid}'
                except jwt.ExpiredSignatureError :
                    response = create_response("" , 401 ,{"message": "Authentication token has expired"})
                    logger.info(f"Response {response}")
                    return Response(json.dumps(response) , status = 401)
                except (jwt.DecodeError , jwt.InvalidTokenError) :
                    response = create_response("" , 401 , {'message' : 'Authorization has failed , please send valid token'})
                    logger.info(f'Response : {response}')
                    return Response(json.dumps(response) , status = 401)
            else :
                response = create_response("" , 401 , {'message' : "Authorization not found, Please send valid token in headers"})
                logger.info(f'Response : {response}')
                return Response(json.dumps(response) , status = 401)
        except : 
            return Response