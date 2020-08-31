from . import views
from django.urls import path


urlpatterns = [

	path('',views.index,name="index"),
	path('add_user/',views.signup,name="add_user"),
	path('login/',views.login_view,name='login'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('logout/',views.logout_user,name='logout'),
	path('all_workers/',views.all_workers,name="all_workers"),
	path('assign_load/',views.assign_load,name="assign_load"),
	path('carrier_detail/<str:pk>', views.user_detail,name='user_detail'),
	#path('add_truck/<str:pk>',views.add_truck,name='add_truck'),
	#path('remove_truck/<str:pk>',views.remove_truck,name='remove_truck'),
	path('user',views.user,name="user"),
	path('active_loads',views.user_active_load,name="user_active_loads"),
	path('remove_equipment/<str:pk>',views.remove_equipment,name="remove_equipment"),
	path('add_equipment/<str:pk>',views.add_equipment,name="add_equipment"),
	path('load_detail/<str:pk>',views.load_detail,name="load_detail"),
	path('myProfile',views.myProfile,name="myProfile"),
	path('complete_load',views.complete_load,name ="complete_load"),
	path('training_center',views.training_center,name="training_center"),
	path('invoicing',views.invoicing,name='invoicing'),
	path('add_carrier',views.add_carrier,name='add_carrier'),
	path('all_carrier',views.all_carrier,name='all_carrier'),
	path('mark_completed/<str:pk>',views.mark_completed,name="mark_completed"),
	path('mark_paid/<str:pk>',views.mark_paid,name="mark_paid"),
	path('all_loads/',views.all_loads,name="all_loads"),
	path('awaiting_loads/',views.awaiting_loads,name="awaiting_loads"),
	path('awaiting_load/<str:pk>',views.awaiting_detail,name="awaiting_load"),
	path('is_await/<str:pk>',views.is_await,name='is_await'),
	path('awb/<str:pk>',views.awb,name="awb"),
	path('is_awb/<str:pk>',views.is_awb,name='is_awb'),
	path('quiz',views.quiz,name='quiz'),
	path('unpaid_loads',views.unpaid_loads,name="unpaid"),
	path('invoice/<str:pk>',views.invoicing,name='invoice'),
	path('pdf_invoice/<str:pk>',views.pdf_invoice,name="pdf_invoice"),
	path('all_invoice',views.all_invoice, name = 'all_invoice'),
	path('password', views.change_password, name='change_password'),
	path('user_info',views.user_info,name='user_info'),
	path('all_users',views.all_users,name='all_users'),
	path('remove_carrier/<str:pk>',views.remove_carrier,name='remove_carrier'),
	path('update_load/<str:pk>',views.edit_loads,name='update_load'),
	path('update_carrier/<str:pk>',views.update_carrier,name='update_carrier'),
	path('update_user',views.update_profile,name='update_user')


]
