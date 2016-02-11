from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Grain_weight, Grain
from my_test.models import Count, Test
from easy_pdf.views import PDFTemplateView

class MyAdminSite(AdminSite):
    def get_urls(self):
                    from django.conf.urls import url

                    urls = super(MyAdminSite, self).get_urls()
                    urls += [
                        url(r'^pdf/(?P<pk>\d+)/$', self.admin_view(PDFView.as_view()))
                    ]
                    return urls

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Grain)
admin_site.register(Grain_weight)
admin_site.register(Test)
admin_site.register(Count)
class PDFView(PDFTemplateView):
    pk_url_kwarg = 'pk'

    template_name="hello.html"
    context_object_name = 'Pdf'


    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        print 'pdf:',pk
        pdf_element = Grain_weight.objects.get(pk=pk)
        return super(PDFView, self).get_context_data(hi = pdf_element, title="PDF", **kwargs)
    def render_to_response(self, context, **response_kwargs):
        return super(PDFView, self).render_to_response(context, **response_kwargs)


