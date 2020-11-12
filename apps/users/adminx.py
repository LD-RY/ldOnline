
import xadmin
from users.models import UserProfile,EmailVerifyRecord,Banner
from xadmin import views
# Register your models here.
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    '''
        设置网站标题和页脚
    '''
    site_title = '在线教育平台'
    site_footer = 'Powered By 1906C - 2020'
    menu_style = 'accordion'    # 菜单折叠


class UserProfileAdmin(object):         # xadmin这里继承的是object，不再是继承admin
    list_display = ["username","gender","mobile","address"] # 显示的列
    search_fields = ["username","gender","mobile","address"] # 搜索的字段，不要添加事件搜索
    list_filter = ["username","gender","mobile","address"]   # 过滤器
    model_icon = 'fa fa-user'       # 给用户添加一个图标
    style_fields = {'address':'ueditor'}        # 给地址字段添加富文本
    ordering = ['date_joined'] # 排序
    readonly_fields = ['nick_name'] # 只读字段，不能编辑
    exclude = ['gender']   # 不显示字段
    list_editable = ['mobile']  # 出现对号填写手机号
    refresh_times = [3,5]   # 刷新间隔时间


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']
    model_icon = 'fa fa-envelope'


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']
    model_icon = 'fa fa-picture-o'


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)