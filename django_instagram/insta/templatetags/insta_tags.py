from django import template

register = template.Library()


@register.filter
def is_like_user(post, user):
    # 해당 글의 is_like_user를 반환 하여줍니다.
    return post.is_like_user(user)