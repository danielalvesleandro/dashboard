
import flask
import requests

ACCESS_TOKEN = 'F9sY85G9qiAGmYZX-FP_'

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/12680270/repository/commits?private_token={}'.format(ACCESS_TOKEN)

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>', methods=[ 'GET' ])
def get_project_commits(projectid):
    
    PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)

    context = {
        'page': 'commits',
        'commits': requests.get(PROJECT_COMMITS).json(),
    }

    return flask.render_template('commits.html', context=context)