from django.shortcuts import render
from http.client import HTTPResponse


def test(request):
    return HTTPResponse("hello")