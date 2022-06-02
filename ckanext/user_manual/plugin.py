import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template, send_from_directory


def help():
    return render_template('help.html')


def get_help_video():
    UPLOAD_DIR = toolkit.config['ckan.storage_path'] + '/storage/uploads/admin/'
    return send_from_directory(UPLOAD_DIR, "help.mp4")


class UserManualPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)


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