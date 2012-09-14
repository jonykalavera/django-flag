from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _

from flag.models import add_flag, FlagCategory


@login_required
def flag(request):
    if request.method!="POST":
        raise Http404
    category_id = request.POST.get("id_comment")
    content_type = request.POST.get("content_type")
    object_id = request.POST.get("object_id")
    creator_field = request.POST.get("creator_field")
    comment = request.POST.get("comment")
    next = request.POST.get("next")
    
    content_type = get_object_or_404(ContentType, id = int(content_type))
    object_id = int(object_id)
    
    content_object = content_type.get_object_for_this_type(id=object_id)
    
    if category_id:
        try
            category = FlagCategory.objects.get(pk=category_id)
        except FlagCategory.DoesNotExist:
            category = None
    
    if creator_field and hasattr(content_object, creator_field):
        creator = getattr(content_object, creator_field)
    else:
        creator = None
    
    add_flag(request.user, content_type, object_id, creator, comment, category)
    messages.add_message(request, messages.INFO, _("You have added a flag. A "
        "moderator will review your submission shortly.")
    
    if next:
        return HttpResponseRedirect(next)
    else:
        return Http404
