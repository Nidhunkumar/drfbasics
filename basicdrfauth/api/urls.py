from django.urls import path
from api import views

urlpatterns = [
	path('robotcategory/',
		views.RobotCategoryList.as_view(),
		name='robotcategory-list'),
	path('',
		views.ApiRoot.as_view(),
		name=views.ApiRoot.name)
]
