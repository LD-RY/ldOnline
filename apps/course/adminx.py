import xadmin
from course.models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    '''课程'''
    list_display = ['name','desc','detail','degree','learn_times','students']
    search_fields = ['name','desc','detail','degree','students']
    list_filter = ['name','desc','detail','degree','learn_times','students']
    model_icon = 'fa fa-book'


class LessonAdmin(object):
    '''章节'''
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']
    model_icon = 'fa fa-bookmark'


class VideoAdmin(object):
    '''视频'''
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']
    model_icon = 'fa fa-video-camera'


class CourseResourceAdmin(object):
    '''课程资源'''
    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course__name','name','download','add_time']
    model_icon = 'fa fa-cloud-download'


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)









