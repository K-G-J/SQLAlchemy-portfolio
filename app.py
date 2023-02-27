import datetime
from flask import (render_template, url_for, request, redirect)
from models import db, app, Project
from utils.clean_date import clean_date


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


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


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        formatted_date = clean_date(request.form['date'])
        if type(formatted_date) != datetime.datetime:
            return render_template('editproject.html', project=project, date_error=True)
        project.date = formatted_date
        project.skills = request.form['skills']
        project.repo_link = request.form['github']
        project.description = request.form['desc']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project)


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
    app.run(debug=True, port=8000, host='127.0.0.1')

    with app.app_context():
        db.create_all()
