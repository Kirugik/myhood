# Myhood

Myhood is a simple web application for people to stay on the loop with what is happening in their neigborhoods. Once registered and logged in, a user can join one of the many neighborhoods created by other users, or create a new neighborhood. As a member of a neihborhood, a user can see updates posted by other members of the same neighborhood. These could include new businesses in the neighborhood and othe general information that might be important. A user can also create a new updates for other members to see, and can post new businesses as well. A user can leave one neighborhood and join a different neighborhood, but cannot be a member of two neighborhoods at the same time.

# By **Robert Kirui**

June 19, 2022.

# Description

Most people would like to receive important updates on whatever is happening in their neighborhoods. Also, contact information of important departments in the neighborhood such as the police and health departments can be vital moreso during emergency cases. For this reason, it is important to have a platform where such information can be accessed more easily. Myhood is a web application that offers exactly this. Users can register on the application, login, see different neighborhoods posted by other users of the app, create a new neighborhood, join a neighborhood, access important information of the specific neighborhood in which he/she belongs, post new businesses for members of that neighborhoods to see, post important updates, and leave the neighborhood when necesary. This ensures that as a member of a given neighborhood, a user can access information and updates regarding that neighborhood with ease.

# User Stories

    - As a user, I would like to sign in with the application to start using.
    - As a user, I would like to set up a profile about me and a general location and my neighborhood name.
    - As a user, I would like to find a list of different businesses in my neighborhood.
    - As a user, I would like to find Contact Information for the health department and Police authorities near my neighborhood.
    - As a user, I would like to create Posts that will be visible to everyone in my neighborhood.
    - As a user, I would like to change My neighborhood when I decide to move out.
    - As a user, I would like to, I would like to only view details of a single neighborhood.

# Screenshots

### Sign up and Sign in pages

![](static/images/sign-up.png) ![](static/images/sign-in.png)

### home page

![](static/images/home.png)

### User profile page

![](static/images/user-profile.png)

### Neigborhood details page

![](static/images/hood-details.png)

### Neigborhood residents list page

![](static/images/hood-residents.png)

### Create new neigborhood page

![](static/images/new-hood.png)

# Behaviour Driven Development (BDD)

- Scenario 1: User wants to sign in with the application
  *GIVEN the user has signed up with the application.
  *THEN the user can sign in using the username and password created when signing up.

- Scenario 1: User wants to join a neighborhood
  *GIVEN the user has signed in with the application, and is on the homepage
  *THEN the user can see a list of neighborhoods already created, and can click 'join hood' button to join a given neighborhood.

- Scenario 2: User wants to set up a profile
  *GIVEN the user has signed in with the application.
  *WHEN the user navigates to the profile page and clicks the update profile button on the navbar,
  \*THEN the user is able to add details to his/her profile

- Scenario 3: User wants to find a list of different businesses in the neighborhood
  *GIVEN the user has signed in with the application.
  *AND the user has joined one of the neighborhoods listed on the home page
  \*WHEN the user clicks the 'my hood' tab in the navbar and navigates to the neighborhood details page
  \*THEN the user can see a list of businesses in the neighborhood listed in the page.

- Scenario 4: User wants to find Contact Information for the health department and Police authorities in the neighborhood
  *GIVEN the user has signed in with the application.
  *AND the user has joined one of the neighborhoods listed on the home page
  \*WHEN the user clicks the 'my hood' tab in the navbar and navigates to the neighborhood details page
  \*THEN the user can see the Contact Information for the health department and Police authorities indicated on the page.

- Scenario 5: User wants to create Posts that will be visible to everyone in the neighborhood.
  *GIVEN the user has signed in with the application.
  *AND the user has joined one of the neighborhoods listed on the home page
  \*WHEN the user clicks the 'my hood' tab in the navbar and navigates to the neighborhood details page
  \*AND clicks the 'create a hood update' button on the page
  \*THEN the user can fill in the details of the post to create a new post that will be visible to everyone in the neighborhood.

- Scenario 6: User wants to change neighborhood
  *GIVEN the user has signed in with the application
  *AND the user has joined one of the neighborhoods listed on the home page
  *WHEN the user clicks the 'leave hood' button on the home page to leave the current neighborhood
  *THEN the user can click the 'join hood' button to join another neighborhood.

- Scenario 7: User wants to only view details of a single neighborhood
  *GIVEN the user has signed in with the application.
  *AND the user has joined one of the neighborhoods listed on the home page
  \*THEN the user can click the 'my hood' button in the navbar to see the details of a single neighborhood.

# Setup/Installation

- Fork the project from this repo
- Run git clone https://github.com/Kirugik/myhood.git to have the project files in your preferred directory on the local machine.
- Change directory into the specific folder containing the project files.
- Run 'pip install -r requirements.txt' to install the project dependencies.
- Run the project in the terminal using: 'python3.8 manage.py runserver'

# Technologies Used

Python, Django, HTML, CSS, heroku

# License

- Licensed under the [MIT License] (LICENSE).

Copyright (c) 2022. **Robert Kirui**
