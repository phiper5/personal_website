#!/usr/bin/python3

from flask import Flask, render_template, abort, request, send_from_directory
import glob
import argparse

# Create the application host
app = Flask(__name__)

# Base URL
base = 'https://phiper.pythonanywhere.com'

# Project webpages
projects = [ \
        "Big Friendly Flame", \
        "Liquid Rocketry", \
        "Vehicle Dynamics", \
        "Electric Vehicles", \
        "Propellant Chemistry", \
        "Computer Vision", \
        "Computational Fluid Dynamics", \
        "Bluetooth Headphones", \
        #"Inverse Heat Transfer", \
        #"Analytical Chemistry", \
        #"MATLAB CEA", \
        #"Altitude Solver", \
        #"CELI Fellow", \
        #"Surf CV", \
        #"Hypergolic Combustion CFD", \
        ]

@app.route('/')
def page_about_me():
    return render_template('about_me.html', title='Philip Piper')

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

@app.route('/outdoors')
def page_outdoors():
    return render_template('outdoors.html', title='Outdoors')

@app.route('/robots.txt')
@app.route('/sitemap.txt')
@app.route('/googlea920b76c17f050ca.html')
def static_from_root():
    print(app.static_folder)
    return send_from_directory(app.static_folder, request.path[1:])

def generate_sitemap():
    # Get webpages
    pages_rel = ['', '/projects', '/outdoors'] \
            + ['/projects/'+x.lower().replace(' ', '-') for x in projects]

    # Get images/videos
    file_types = ['jpg', 'mp4']
    media_rel = ['/'+f for f_ in \
            [glob.glob('**/*.'+ext, recursive=True) for ext in file_types] \
            for f in f_]

    # Make URLs absolute and join into string
    pages_abs = [base + page for page in pages_rel+media_rel]
    str_sitemap = '\n'.join(pages_abs)

    # Write the data
    with open(app.static_folder+'/sitemap.txt', 'w') as f:
        f.write(str_sitemap)

if __name__ == '__main__':
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Run the website server.')
    parser.add_argument('-g', '--generate-sitemap', \
            help='Generate a sitemap file', action='store_true')
    args = parser.parse_args()

    # Generate a sitemap or run the web host
    if args.generate_sitemap:
        generate_sitemap()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)
