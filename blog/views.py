from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView


from .models import SongiYangiliklar,Voqealar

from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    songiyangiliklar = SongiYangiliklar.objects.all()
    voqealar = Voqealar.objects.all()
    context = {
      "songiyangilik" : songiyangiliklar,
        "voqealar" : voqealar
    }
    return render(request,"index.html",context=context)
# def Edit(request,pk):
#     daraxt = get_object_or_404(Comments,id=pk)
#     form = CommentForm(request.POST or None, instance=daraxt)
#     if form.is_valid():
#         form.save()
#         return reverse_lazy('news')
#     context = {
#         "form": form,
#         "daraxt": daraxt
#     }
#     return render(request,'comment/tahrirlash.html',context)
# def Delete(request,pk):
#     contact = get_object_or_404(Comments,id=pk)
#     if request.method == "POST":
#         contact.delete()
#         return reversed('yangilik')
#     return render(request, 'comment/ochirish.html', context={})
# class ContactEdit(UpdateView,LoginRequiredMixin):
#     model = Comments
#     form_class = CommentForm
#     context_object_name = 'comment'
#     template_name = 'comment/tahrirlash.html'
# def newsDetel(request,id):
#     yangilik = get_object_or_404(News, id=id)
#     post = get_object_or_404(News,id=id)
#     if post:
#         post.views=post.views+1
#         post.save()
#     comments = yangilik.comments.filter(active=True)
#     new_comment = None
#     comment_form = None
#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#
#
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.news = yangilik
#             new_comment.user = request.user
#             new_comment.save()
#             comment_form = CommentForm()
#
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         "news": yangilik,
#         "post":post,
#         "comments": comments,
#         "comment_form": comment_form,
#         "new_comment" : new_comment,
#     }
#     return render(request, 'Detel/articlesdetel.html', context)
# def articlesdetel(request,id):
#     yangilik = get_object_or_404(yangilikDetel,id=id)
#     context ={
#         "yangilik": yangilik
#     }
#     return render(request,'Detel/articlesdetel.html',context)
# def articles(request):
#     news = yangilikDetel.objects.all()
#     context = {
#         "detel": news,
#     }
#     return render(request,"article.html",context=context)

def asosiytexnalogiyalar(request):
    return render(request,"asosiytexnologiyal.html",context={})
def html_3d_gis(request):
    return render(request,"3dgis.html",context={})
def events(request):
    voqealar = Voqealar.objects.all()
    context = {
        "voqealar":voqealar
    }
    return render(request,"events.html",context=context)
def supermapgishaqida(request):
    return render(request,"supermapgishaqida.html",context={})
def ai_gis(request):
    return render(request,"aigis.html",context={})
def bulutli_gis_serveri(request):
    return render(request,"bulutligis.html",context={})
def cloud_gis(request):
    return render(request,"coloudgisserver.html",context={})
def comp_gis_terminali(request):
    return render(request,"terminalgisforweb.html",context={})
def cross_platform(request):
    return render(request,"crossplatform.html",context={})
def edge_gis_server(request):
    return render(request,"edgegisserver.html",context={})
def gis_10_i(request):
    return render(request,"gis10.html",context={})
def gis9(request):
    return render(request,"gis9.html",context={})
def joinus(request):
    return render(request,"joinus.html",context={})
def kattamalumot(request):
    return render(request,"kattamalumot.html",context={})
def mulkboshqarish(request):
    return render(request,"mulkboshqarish.html",context={})
def onlinegisplatform(request):
    return render(request,"onlinegisplatform.html",context={})
def suvsaqlash(request):
    return render(request,"suvsaqlash.html",context={})
def tabiatresurs(request):
    return render(request,"tabiatresurs.html",context={})
def tabiiyofat(request):
    return render(request,"tabiiyofat.html",context={})
def terminalgisformobile(request):
    return render(request,"terminalgisformobile.html",context={})
def terminalgisforpc(request):
    return render(request,"terminalgisforpc.html",context={})
def transport(request):
    return render(request,"transport.html",context={})
def xavfsizlik(request):
    return render(request,"xavfsizlik.html",context={})
def yermulk(request):
    return render(request,"yermulk.html",context={})
def aqllishahar(request):
    return render(request,"aqllishahar.html",context={})
def news(request):
    songiyangiliklar = SongiYangiliklar.objects.all()
    context = {
        "songiyangilik" : songiyangiliklar
    }
    return render(request,"news.html",context=context)
def bimgis(request):
    return render(request,"bimgis.html",context={})
def indexdetel(request,id ):
    yangilik = get_object_or_404(SongiYangiliklar, id=id)
    yangiliklist  = SongiYangiliklar.objects.all()[4:]
    context = {
        "detel":yangilik,
        "detellist":yangiliklist
    }

    return render(request,"detail.html",context)
def indexdetel2(request,id ):
    yangilik1 = get_object_or_404(Voqealar, id=id)
    yangiliklist1 = Voqealar.objects.all()[:4]
    context = {
        "detel2": yangilik1,
        "detellist2":yangiliklist1
    }

    return render(request,"detail.html",context)





