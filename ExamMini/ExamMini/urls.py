"""djproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first),
    #path('evaluatorlogin/', evaluatorlogin, name="evaluatorlogin"),
    path('adminlogin/', adminlogin, name="adminlogin"),
    path('link/', link, name="link"),
    path('question/', question, name="question"),
    path('questionpaper/', questionpaper, name="questionpaper"),
    # path('evaluator2/', evaluator2, name="evaluator2"),
    # path('evaluator1/', evaluator1, name="evaluator1"),
    # path('process/', process, name="process"),
    path('thankyou/', thankyou, name="thankyou"),
    # path('selectsubject/', selectsubject, name="selectsubject"),
    path('eval1/', eval1, name="eval1"),
    path('eval3/', eval3, name="eval3"),
    path('update/', update, name="update"),

]