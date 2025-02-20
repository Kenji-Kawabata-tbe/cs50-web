from django.urls import path

from . import views

app_name = "title"

urlpatterns = [
    #path("", views.index, name="index")
    path("<str:title>/", views.index, name="index") # <str:title>はtitleの値が動的にpathとして設定されるということ。

]
