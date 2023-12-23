
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import os
import requests
import json
# Create your views here.

@api_view(['GET'])
def test(req):
    s='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Aenean sit amet diam mauris. Nam luctus, leo id sollicitudin efficitur
 , leo massa hendrerit elit, non vestibulum felis mi nec neque. Sed id
   lectus vel dolor venenatis finibus non sit amet justo. Curabitur accumsan eros et purus hendrerit, sed bibendum lorem gravida. Phasellus tincidunt consequat dui, at iaculis sem mollis scelerisque. Suspendisse ornare est sit 
   amet lectus sodales, non elementum lectus mattis. Morbi tristique mollis nunc, ullamcorper consequat 
elit accumsan nec. Donec sollicitudin cursus fringilla.
'''
    return Response(data={s},status=status.HTTP_200_OK)

@api_view(['POST'])
def t_to_t(req):
    text=req.data.get('text')
    api_key=os.environ.get('Gemini_API')
    s="hello how are you"
    headers={
    
        "Content-Type": "application/json",
    }
    payload1 = {
        "contents": [{
            "parts": [{
                "text":text
            }]
        }]
    }
    payload = {
        "contents": [{
            "parts": [{
                "text":text
            }]
        }],
        "generationConfig": {
            "stopSequences": [
                
            ],
            "candidateCount":1,
            "temperature": 1.0,
            "maxOutputTokens": 50,
            "topP": 0.5,
            "topK": 10
        }
    }
    res=requests.post(f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:countTokens?key={api_key}',data=json.dumps(payload1))
    print(res.json())
    res=requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}',data=json.dumps(payload),headers=headers)
    if res.status_code==200:
        data=res.json()
        f=data["candidates"][0]['content']['parts'][0]
        return Response(data=f,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)