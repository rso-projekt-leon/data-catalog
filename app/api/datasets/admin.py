from flask_admin.contrib.sqla import ModelView


class DatasetsAdminView(ModelView):
    column_searchable_list = ("dataset_name", "file_name")
    column_editable_list = ("dataset_name", "file_name")
    column_filters = ("dataset_name", "file_name")
    column_sortable_list = ("dataset_name", "created_timestamp")
    column_default_sort = ("created_timestamp", True)
