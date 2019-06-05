from django.forms.fields import MultiValueField
from cmsplugin_cascade.bootstrap4.grid import Breakpoint
from cmsplugin_cascade.fields import SizeField
from cmsplugin_cascade.widgets import MultipleTextInputWidget


class MultipleSizeField(MultiValueField):
    widget = MultipleTextInputWidget([bp.name for bp in Breakpoint])

    def __init__(self, *args, **kwargs):
        required = kwargs.pop('required', False)
        allowed_units = kwargs.pop('allowed_units', None)
        fields = [SizeField(required=required, allowed_units=allowed_units)] * len(Breakpoint)
        super().__init__(fields=fields, *args, **kwargs)

    def compress(self, data_list):
        return data_list

