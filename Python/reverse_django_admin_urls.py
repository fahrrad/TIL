from django.core.urlresolvers import reverse
reverse('admin:{{app_label}}_{{model_name}}_[change|delete|history|add|changelist]', args=(id))
# in template
{% url opts|admin_urlname:'delete' user.pk %}


# all info here https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
