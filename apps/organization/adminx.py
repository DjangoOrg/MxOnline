# !usr/bin/env python3
# encoding:utf-8
"""
@project = MxOnline
@file = adminx
@author = 'Easton Liu'
@creat_time = 2018/12/20 20:22
@explain:

"""
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']

class TeacherAdmin(object):
    list_display = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'image','add_time']
    search_fields = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'image']
    list_filter = ['org','name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'image','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)