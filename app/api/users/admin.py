from flask_admin.contrib.sqla import ModelView


class UsersAdminView(ModelView):
    column_searchable_list = ("username", "name_surname", "email")
    column_editable_list = ("username", "name_surname", "email", "active", "created_timestamp")
    column_filters = ("username", "name_surname", "email", "active")
    column_sortable_list = ("username", "name_surname", "email", "active", "created_timestamp")
    column_default_sort = ("created_timestamp", True)
