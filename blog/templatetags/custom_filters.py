from django import template
from django.template.defaultfilters import timesince as timesince_default
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter(name='timesince')
def timesince_custom(value, arg=None):
    if not value:
        return ''

    if arg:
        return timesince_default(value, arg)

    delta = now() - value
    if delta.total_seconds() < 60:  # 1분 미만
        return '{}초 전'.format(int(delta.total_seconds()))
    elif delta.total_seconds() < 3600:  # 1시간 미만
        return '{}분 전'.format(int(delta.total_seconds() / 60))
    elif delta.days == 1:  # 1일 전
        return '어제'
    elif delta.days > 1:  # 1일 이상
        return '{}일 전'.format(delta.days)
    else:
        hours = int(delta.total_seconds() // 3600)
        minutes = int((delta.total_seconds() % 3600) // 60)
        return '{}시간 전'.format(hours)
