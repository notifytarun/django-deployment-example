from django import template

register = template.Library()

def cut(value,arg):
    
    return value.replace(arg,'')



def ad(value,r):
    return r+value
register.filter('ad',ad)
register.filter('cut',cut)


