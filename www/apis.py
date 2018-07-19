'''
 * @Author: beartree 
 * @Date: 2018-07-19 21:29:32 
 * @Last Modified by:   beartree 
 * @Last Modified time: 2018-07-19 21:29:32 
 '''

'''
JSON API definition
'''

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not founnd. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permissson:forbidden', 'permission', message)


 


