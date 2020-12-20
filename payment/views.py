from django.shortcuts import render, redirect, get_object_or_404
import braintree  # pylint: disable=import-error
from django.conf import settings
from orders.models import Order
