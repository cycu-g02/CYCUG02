from django import template

register = template.Library()

@register.filter(name='to_int') # 過滤器在模板中使用时的name
def full_number(value):
    if value is not None:
        if type(value) == str:
            if len(value.strip()) > 0:
                try:
                    return round(int(value))
                except:
                    return 0
        else:
            return round(value)#round沒有指定小數位即四捨五入
    return 0

@register.filter(name='multiply') # 過滤器在模板中使用时的name
def multiply_number(value, times):
    if value is not None and times is not None:
        return round((value * float(times)))  #round沒有指定小數位即四捨五入
    return 0

@register.filter(name='list_len') # 過滤器在模板中使用时的name
def list_len(value):
    if value is not None:
        return len(value)
    else:
        return 0

@register.filter(name='order_status') # 過滤器在模板中使用时的name
def order_status(value):
    if value is not None:
        if value == '0':
            return '未付款'
        elif value == '1':
            return '已付款'
        elif value == '2':
            return '已取消'
        else:
            return 'N/A'
    else:
        return 'N/A'