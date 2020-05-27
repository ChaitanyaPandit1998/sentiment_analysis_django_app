from django.urls import path
from .views import api_sentiment_pred

urlpatterns = [
  path('api/predict/',api_sentiment_pred,name='api_sentiment_pred'),
]