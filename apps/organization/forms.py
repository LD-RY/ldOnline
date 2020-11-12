from django import forms
from operation.models import UserAsk
import re

class UserAskForm(forms.Form):
    '''我要咨询'''
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        '''验证手机号是否合法'''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = r"1[34578]\d{9}"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法',code = 'mobile_invalid')







