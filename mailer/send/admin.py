from django.contrib import admin

# from send.models import Email


# class EmailAdmin(admin.ModelAdmin):
#     """
#     Admin part for managing the the Email model
#     """
#     list_display = ['send_to', 'send_from', 'subject', 'ok', ]
#     list_filter = ['ok']
#     readonly_fields = ['when', 'send_to', 'send_from', 'subject', 'body', 'ok']
#     search_fields = ['subject', 'body', 'to']

#     def has_delete_permission(self, request, obj=None):
#         return False

#     def has_add_permission(self, request):
#         return False


# admin.site.register(Email, EmailAdmin)
