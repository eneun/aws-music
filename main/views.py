from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm
import requests

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.save()
            return redirect('main')
    else:
        from django.conf import settings
        musics = Music.objects.all
        form = MusicForm()
        try:
            service_info=requests.get("http://169.254.169.254/latest/meta-data/instance-id",timeout=2).text
        except:
            service_info =""
        return render(request, 'main.html', {'form': form, 'musics': musics, 'service_info': service_info})

def setting(request):
    from .custom_storage import MediaStorage

    MediaStorage.aws_region = request.POST['s3-region']
    MediaStorage.bucket_name = request.POST['s3-bucket-name']
    MediaStorage.custom_domain = '%s.s3.%s.amazonaws.com' % (MediaStorage.bucket_name, MediaStorage.aws_region)
    return redirect('main')