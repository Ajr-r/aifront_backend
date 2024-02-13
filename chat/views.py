from chat.gemini import gemini_text
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random,os,json

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
    i=random.randint(0,9)

    poems = [
    "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore— While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door— Only this and nothing more.”",
    "I wandered lonely as a cloud That floats on high o'er vales and hills, When all at once I saw a crowd, A host, of golden daffodils; Beside the lake, beneath the trees, Fluttering and dancing in the breeze.",
    "Shall I compare thee to a summer's day? Thou art more lovely and more temperate: Rough winds do shake the darling buds of May, And summer's lease hath all too short a date: Sometime too hot the eye of heaven shines, And often is his gold complexion dimmed; And every fair from fair sometime declines, By chance, or nature's changing course, untrimmed; But thy eternal summer shall not fade, Nor lose possession of that fair thou ow'st; Nor shall Death brag thou wanderest in his shade, When in eternal lines to time thou grow'st; So long as men can breathe, or eyes can see, So long lives this, and this gives life to thee.",
    "I celebrate myself, and sing myself, And what I assume you shall assume, For every atom belonging to me as good belongs to you. I loafe and invite my soul, I lean and loafe at my ease observing a spear of summer grass. My tongue, every atom of my blood, form'd from this soil, this air,",
    "It little profits that an idle king, By this still hearth, among these barren crags, Matched with an aged wife, I mete and dole Unequal laws unto a savage race, That hoard, and sleep, and feed, and know not me. I cannot rest from travel: I will drink",
    "I wandered through each chartered street, Near where the chartered Thames does flow, A mark in every face I meet, Marks of weakness, marks of woe. In every cry of every man, In every infant's cry of fear,",
    "My heart leaps up when I behold A rainbow in the sky: So was it when my life began; So is it now I am a man; So be it when I shall grow old, Or let me die!",
    "Thou still unravish'd bride of quietness, Thou foster-child of Silence and slow Time, Sylvan historian, who canst thus express A flowery tale more sweetly than our rhyme: What leaf-fring'd legend haunts about thy shape Of deities or mortals, or of both,",
    "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore— While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door— Only this and nothing more.”",
    "I wandered lonely as a cloud That floats on high o'er vales and hills, When all at once I saw a crowd, A host, of golden daffodils; Beside the lake, beneath the trees, Fluttering and dancing in the breeze."
]
    return gemini_text(text,api_key)


