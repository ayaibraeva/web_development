from django.urls import path
from api.views import company_list, companies_detail, vacancy_list, vacancies_by_company, vacancy_list,vacancy_detail, top_ten

urlpatterns = [

    path('companies/', company_list),
    path('companies/<int:company_id>/', companies_detail),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/<int:company_id>/vacancies', vacancies_by_company),
    path('vacancies/topten/', top_ten)
]
