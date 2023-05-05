from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(p,cart):
    keys =  cart.keys()
    for id in keys:
        if int(id)==p.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(p,cart):
    keys =  cart.keys()
    for id in keys:
        if int(id)==p.id:
            return cart.get(id)
    return 
@register.filter(name='price_total')
def price_total(p,cart):
    return p.price * cart_quantity(p,cart )

@register.filter(name='cart_total_price')
def cart_total_price(filter, cart): #filter is cart all product
    sum=0
    for tp in filter:
        sum += price_total(tp,cart)
    return sum

@register.filter(name='multiply')
def multiply(number,number1):
    return number * number1
 