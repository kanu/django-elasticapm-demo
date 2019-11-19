import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse
from home.models import LinkItem
import redis


logger = logging.getLogger("info")

rc = redis.StrictRedis(**settings.REDIS)

CLICK_COUNTER_KEY = "LinkItem_counter"


def get_link_counter_field(link, kind="click"):
    return f"{link.id}:{kind}"


def index(request, *args, **kwargs):
    return render(request, "index.html")


def link_list(request):
    counts = rc.hgetall(CLICK_COUNTER_KEY)

    items = sorted(
        [
            (link, counts.get(get_link_counter_field(link, "click"), 0))
            for link in LinkItem.objects.iterator()
        ],
        key=lambda x: int(x[1]),
    )

    context = {"links": items}
    return render(request, "link-list.html", context)


def link_detail(request, link_id):
    link = get_object_or_404(LinkItem, id=link_id)

    context = {
        "click_count": rc.hget(CLICK_COUNTER_KEY, get_link_counter_field(link, "click"))
        or 0,
        "obj": link,
        "url": reverse("link-redirect", kwargs={"link_id": link.id}),
    }
    return render(request, "link-detail.html", context)


def link_redirect(request, link_id, *args, **kwargs):
    link = get_object_or_404(LinkItem, id=link_id)
    count = rc.hincrby(CLICK_COUNTER_KEY, get_link_counter_field(link, "click"), 1)
    logger.info(
        "Increase the counter for link:%(link)s to %(count)s",
        dict(link=link.id, count=count),
    )
    return HttpResponseRedirect(redirect_to=link.url)


def start_presentation(request):
    user = request.user
    user_data = user._wrapped.__dict__

    raise NotImplementedError("Sorry")
