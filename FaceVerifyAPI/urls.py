from django.urls import path
from . import views

urlpatterns = [
# Url For Help
    path('help/' , views.api_overview , name = "api-overview"),

# Person Class URLS:
    path('person/list/' , views.person.list_all , name = "user-list"),
    path('person/create/' , views.person.create_person , name = "user-create"),

    path('person/update/<str:id>' , views.person.update_person , name = "user-update"),
    path('person/delete/<str:id>' , views.person.delete_person , name = "user-delete"),

# Face Class URLS:
    path('image/listall/' , views.face.list_all , name = "image-list"),
    path('image/create/' , views.face.add_image , name = "image-create"),

    path('image/listbyperson/<str:id>' , views.face.list_by_person , name = "image-list-by-person"),
    path('image/update/<str:id>' , views.face.update_image , name = "image-update"),
    path('image/delete/<str:id>' , views.face.delete_image , name = "image-delete"),

# Verify Class URLS:
    path('verify/linear' , views.verify_image.linear_verify , name = "linear-verification"),

#Debug Paths for development purpose
    path('dev/embeddings/<str:id>' , views.dev.return_embeddings , name = "return-embeddings"),
]
