from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from yandex_geocoder import Client
from django.conf import settings

client = Client(settings.YANDEX_API_KEY)


class GeoFormView(TemplateView):
    template_name = 'geoform.html'


@method_decorator(csrf_exempt, name='dispatch')
class GetGeoCodeView(View):
    def post(self, request):
        resp = request.POST.get('response')
        r = client.coordinates(resp)
        return HttpResponse(f'{r[0]} {r[1]}')
