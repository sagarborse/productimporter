from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as conf_settings
import logging
import os
# Create your views here.
logger = logging.getLogger("custom_logger")
from django.http import HttpResponse, JsonResponse
from werkzeug.utils import secure_filename
import uuid

@csrf_exempt
def index(request):
    return render(request, "csv_uploader.html")

@csrf_exempt
def upload(request):
    logger.info(request.FILES)
    logger.info(request.POST)
    if request.method == 'POST':
        file = request.FILES['file']
        file_name = file.name
        save_path = os.path.join(conf_settings.FILE_UPLOADS_PATH, secure_filename(file_name))
        current_chunk = int(request.POST['dzchunkindex'])

        if os.path.exists(save_path) and current_chunk == 0:
            return HttpResponse(('File already exists', 400))

        with open(save_path, 'ab+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        total_chunk = int(request.POST['dztotalchunkcount'])
        if current_chunk == total_chunk - 1:
            os.rename(save_path, "{0}/{1}_{2}".format(conf_settings.FILE_UPLOADS_PATH, str(uuid.uuid4()), file_name))

        logger.info(save_path)
        return HttpResponse(('Uploaded Chunk', 200))
    return JsonResponse({'Cannot access URI', 400})

def showProducts(request):
    return HttpResponse("showProducts.")

