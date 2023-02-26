from models import db, app, Project
from utils.clean_date import clean_date
from flask import (render_template, url_for, request, redirect)
import datetime


"""
Create the Homepage route/view
Route: /

This view should render a page of all of the projects, where each project displays the following fields:


Create an interface for a portfolio web application. The main (index) page lists your projects including the project title and short description. Each project links to a detail page that displays the title, date, and description.
"""


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


"""
Create the Detail route/view
Route: /project/<id>

This view should render a detail page of a project, it should display the following fields on the page:

Title
Date
Description
Skills practiced
Link to the project’s GitHub repo
NOTE: This page should contain a link/button that takes the user to the Edit route for the project with this <id>.
"""


@app.route('/project/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    formatted_date = (project.date).strftime("%B, %Y")
    return render_template('detail.html', project=project, formatted_date=formatted_date)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    if request.form:
        formatted_date = clean_date(request.form['date'])
        if type(formatted_date) != datetime.datetime:
            return render_template('projectform.html', date_error=True)
        new_project = Project(
            title=request.form['title'], date=formatted_date, skills=request.form['skills'], repo_link=request.form['github'], description=request.form['desc'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


"""
Create the Edit route/view
Route: /project/<id>/edit

Create an edit view with the route /project/<id>/edit that allows the user to edit the project with an id of the <id> passed in:

Title
Date
Description
Skills practiced
GitHub repo link
Ideally, you should pre-populate each form field with the existing data on load. So the form is filled out with the existing data so the User can easily see what the value is and make edits to the form to make the update.

NOTE: Updating a project should not result in a new project being created, this behavior would not be seen as editing this would be adding a new project. To check this, you can simply make an edit and then reload the listing page to see if a duplicate record was created.
"""


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    return render_template('editproject.html', project=project)


"""
Create the Delete route
Create a delete route to delete the project from the database. When the delete button is clicked by the user, the project will be removed from the database and they will be redirected to the homepage.
"""


@app.route('/project/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    """
    NOTE: When run, the database should already contain at least the 4 previous projects of the Techdegree.
    """

    app.run(debug=True, port=8000, host='127.0.0.1')

    with app.app_context():
        db.create_all()
