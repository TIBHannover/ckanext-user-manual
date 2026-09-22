import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.exceptions import CkanConfigurationException
from flask import Blueprint, render_template, send_from_directory


def help():
    return render_template('help.html')

def check_plugin_enabled(plugin_name):
    enabled_plugins = toolkit.config.get("ckan.plugins", "").split()
    return plugin_name in enabled_plugins


def get_help_video():
    storage_path = toolkit.config.get('ckan.storage_path')
    if not storage_path:
        raise CkanConfigurationException(
            'ckan.storage_path must be configured to serve the help video'
        )
    upload_dir = os.path.join(storage_path, 'storage', 'uploads', 'admin')
    return send_from_directory(upload_dir, "help.mp4")

def which_sfb():
    ckan_root_path = toolkit.config.get('ckan.root_path')
    if  ckan_root_path and 'sfb1368/ckan' in ckan_root_path:
        return '1368'
    elif ckan_root_path and 'sfb1153/ckan' in ckan_root_path:
        return '1153'
    else:
        # localhost
        return '1368'


class UserManualPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public/statics', 'ckanext-user-manual')



    def get_blueprint(self):

        blueprint = Blueprint(self.name, self.__module__)        
        blueprint.add_url_rule(
            u'/user_manual/help',
            u'help',
            help,
            methods=['GET']
            )   
        
        blueprint.add_url_rule(
            u'/user_manual/video',
            u'video',
            get_help_video,
            methods=['GET']
            )   

        return blueprint 
    
    #ITemplateHelpers

    def get_helpers(self):
        return {'is_plugin_enabled': check_plugin_enabled, 
                'which_sfb': which_sfb}
