from examproject.exam.models import Profile, Item


def get_user():
    return Profile.objects.first()


def get_all_items():
    return Item.objects.all() if Item.objects.all() else None