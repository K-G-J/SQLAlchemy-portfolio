from models import db, app, Project
from flask import (render_template, url_for, request, redirect)


"""
Routes for the Application
Create each of the following routes for your application

/ - Known as the root page, homepage, or landing page.

/projects/new - The Create route

/projects/<id> - The Detail route

/projects/<id>/edit - The Edit or Update route

/projects/<id>/delete - Delete route

NOTE: Each route is of course prefixed with the running server address

Example: The route /project would be mapped to: http://<address>:<port>/project
"""


"""
Create the Homepage route/view
Route: /

This view should render a page of all of the projects, where each project displays the following fields:

Title - should be a linked title, clicking it routes the user to the detail page for the clicked project.
Short description - Each project should have a short description of what the project is about.
Skills practiced - a list of the skills practiced in the project
GitHub link - A link to the project on GitHub

Create an interface for a portfolio web application. The main (index) page lists your projects including the project title and short description. Each project links to a detail page that displays the title, date, and description.
"""


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


"""
Create the Add route/view
Create an add view with the route /project/new that allows the user to add a project with the following fields:

Title - string
Date - date
Description - text
Skills - text
GitHub repo link - text
The page should present a new blank project form that allows the user to Create a new project that will be stored in the database.
"""


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


"""
Create the Delete route
Create a delete route to delete the project from the database. When the delete button is clicked by the user, the project will be removed from the database and they will be redirected to the homepage.
"""


if __name__ == '__main__':
    """
    NOTE: When run, the database should already contain at least the 4 previous projects of the Techdegree.
    """

    app.run(debug=True, port=8000, host='127.0.0.1')

    with app.app_context():
        db.create_all()
