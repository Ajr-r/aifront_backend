from rest_framework.response import Response
import json,requests
from rest_framework import status
def gemini_text(text,api_key):

    headers={
    
        "Content-Type": "application/json",
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
    #return Response(data=poems[i],status=status.HTTP_200_OK)
    res=requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}',data=json.dumps(payload),headers=headers)
    if res.status_code==200:
        data=res.json()
        print(data)
        try:

            f=data["candidates"][0]['content']['parts'][0]
        except:
            return Response(data=data["candidates"][0],status=status.HTTP_400_BAD_REQUEST)

        print(f)
        return Response(data=f,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
