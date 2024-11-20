# coding:utf-8

# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------

import os
import json

from flask import Blueprint, render_template
from flask import request

from admin.user_login_check import panel_login_required

from utils.plugin import plugin as MwPlugin
from utils.site import sites as MwSites
import core.mw as mw
import thisdb

from .site import blueprint


# 获取证书信息
@blueprint.route('/get_ssl', endpoint='get_ssl', methods=['POST'])
@panel_login_required
def get_ssl():
    site_name = request.form.get('site_name', '')
    ssl_type = request.form.get('ssl_type', '')
    return MwSites.instance().getSsl(site_name, ssl_type)

# 获取证书列表
@blueprint.route('/get_cert_list', endpoint='get_cert_list', methods=['GET','POST'])
@panel_login_required
def get_cert_list():
    return MwSites.instance().getCertList()








