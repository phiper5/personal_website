#!/usr/bin/python3

from flask import Flask, render_template, abort

# Create the application host
app = Flask(__name__)

projects = [ \
        "Big Friendly Flame", \
        "Liquid Rocketry", \
        "Vehicle Dynamics", \
        "Electric Vehicles", \
        #"Propellant Chemistry", \
        #"CELI Fellow", \
        #"Surf CV", \
        #"Vehicle CV", \
        #"Incompressible CFD", \
        #"Hypergolic Combustion CFD", \
        #"MATLAB CEA", \
        #"Altitude Solver", \
        #"Bluetooth Headphones", \
        ]

@app.route('/')
def page_home():
    return render_template('home.html', title='Home')

@app.route('/projects')
def page_projects():
    project_strs = [x.lower().replace(' ', '-') for x in projects]
    project_pics = ['/static/img/projects/'+x+'/'+x+'.jpg' \
            for x in project_strs]
    project_links = ['/projects/'+x for x in project_strs]
    project_htmls = [x.replace(' ', '<br>') for x in projects]
    return render_template('projects.html', title="Projects", \
            project_htmls=project_htmls, project_pics=project_pics, \
            project_links=project_links)

@app.route('/projects/<project_name>')
def page_project_names(project_name):
    title = project_name.replace('-', ' ').title()
    if title not in projects:
        abort(404)
    return render_template('/projects/'+project_name+'.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
