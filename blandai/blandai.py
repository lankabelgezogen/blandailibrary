import requests

class BlandAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'authorization': self.api_key}
        
    def call(self, phone_number, task, voice_id, request_data, reduce_latency, amd):
        # API endpoint
        url = 'https://api.bland.ai/call'
        
        # Data payload
        data = {
            'phone_number': phone_number,
            'task': task,
            'voice_id': voice_id,
            'request_data': request_data,
            'reduce_latency': reduce_latency,
            'amd': amd,
            #'webhook': webhook
        }
        
        # Make the API call
        response = requests.post(url, json=data, headers=self.headers)
        
        # Return the response
        return response.json()
    
    def logs(self, call_id):
        # API endpoint
        url = 'https://api.bland.ai/logs'
        
        # Data payload
        data = {'call_id': call_id}
        
        # Make the API call
        response = requests.post(url, json=data, headers=self.headers)
        
        # Return the response
        return response.json()

    def hold(self, phone_number, hold_connect, task):
        # API endpoint
        url = 'https://api.bland.ai/hold'
        
        # Data payload
        data = {
            'phone_number': phone_number,
            'hold_connect': hold_connect,
            'task': task
        }
        
        # Make the API call
        response = requests.post(url, json=data, headers=self.headers)
        
        # Return the response
        return response.json()

    def end_call(self, call_id):
        # API endpoint
        url = 'https://api.bland.ai/end'
        
        # Data payload
        data = {'call_id': call_id}
        
        # Make the API call
        response = requests.post(url, json=data, headers=self.headers)
        
        # Return the response
        return response.json()
