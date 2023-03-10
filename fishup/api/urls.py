from . import views
from django.urls import path




urlpatterns = [     
    
    path("signup-customer/",views.customercreate.as_view(),name="signup-owner"),
    path("signup-fisherman/",views.fishermancreate.as_view(),name="signup-fisherman"),
    path("signup-retailer/",views.retailerscreate.as_view(),name="signup-retailer"),
    path("addfish/",views.fishcreate.as_view(),name="addfish"),
     path("addfish4/",views.fishcreate4.as_view(),name="addfish4"),
    
    path("listfish/",views.fishlist.as_view(),name="listfish"),
    path("listcustomer/",views.customerlist.as_view(),name="listcustomer"),
    path("listretailer/",views.retailerslist.as_view(),name="listretailer"),
    path("listfisherman/",views.fishermanlist.as_view(),name="listfisherman"),
    
    # path("addfishcount/<int:pk>/",views.fishcount.as_view({"get": "retrieve"}),name="addfishcount"),
    

    path("deletecustomer/<int:pk>/",views.deletecustomer.as_view(),name="deletecustomer"),
    path("deletefisherman/<int:pk>/",views.deletefisherman.as_view(),name="deletefisherman"),
    path("deleteretailers/<int:pk>/",views.deleteretailers.as_view(),name="deleteretailers"),
    path("deletefish/<int:pk>/",views.deletefish.as_view(),name="deletefish"),

    path("updatecustomer/<int:pk>/",views.updatecustomer.as_view(),name="updatecustomer"),
    path("updatefisherman/<int:pk>/",views.updatefisherman.as_view(),name="updatefisherman"),
    path("updateretailers/<int:pk>/",views.updateretailers.as_view(),name="updateretailers"),
    path("updatefish/<int:pk>/",views.updatefish.as_view(),name="updatefish"),

    path("retrievecustomer/<int:pk>/",views.retrievecustomer.as_view(),name="retrievecustomer"),
    path("retrieveretailers/<int:pk>/",views.retrieveretailers.as_view(),name="retrieveretailers"),
    path("retrievefisherman/<int:pk>/",views.retrievefisherman.as_view(),name="retrievefisherman"),
    path("retrievefish/<int:pk>/",views.retrievefish.as_view(),name="retrievefish"),

    path("filterretailer/",views.retailerslist2.as_view(),name="filterretailer"),


    # path("counter/",views.fishcount.as_view(),name="couter"),

    

]

