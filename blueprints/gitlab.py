
import flask
import requests

ACCESS_TOKEN = 'F9sY85G9qiAGmYZX-FP_'
ID = '12680386'
PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
projectid = None

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)

    context = {
        'page': 'projetos',
        'projects': requests.get(PROJECTS_URL).json(),
        'commits': requests.get(PROJECT_COMMITS).json()
    }
    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>', methods=[ 'GET' ])
def get_project_commits(projectid):

    PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)

    context = {
        'page': 'commits',
        'commits': requests.get(PROJECT_COMMITS).json()
    }
    return flask.render_template('commits.html', context=context)

