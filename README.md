# <center> AskToday </center> #

The purpose of AskToday is to create a site which allows users to ask questions and have them answered by other users on the site. In addition to this users have the ability to read all questions that have been asked on the site, follow posts and upload pictures to be attached to a question they have asked.

# <center><br> Features and Functionalities </center> #

### **Sign Up and Login Pages** ###
In order for users to gain access to all features on the site it is necessary for them to sign up and create an account.
 
To create an account users must go to the signup page and put in the necessary details. These details include submitting their name, email and password. Once a user has entered all these details they will gain access to all the features on offer on AskToday.
 
Users who already have made an account have the ability to sign back into their account via the login page where they will be asked to enter their email and password. Users have the ability to logout of their accounts if they are signed in on the site.

### <br>**Homepage** ###
The homepage serves to contextualise the site and its purpose. Additionally, the navbar at the top of the page allows users to navigate to other sections of the site.
 
### <br>**Terms of Use** ###
In the footer of the site, users can be directed to the terms of use page which outlines AskToday's privacy policy, website disclaimer and the terms of use for contributors.
 
### <br>**Feed** ###
The feed displays all questions that have been previously asked on the site. From this page users can submit their own question, go to an individual question's page for more details on the post and see all previously asked questions.
 
### <br>**Creating a Post** ###
One of the main features of the site, is the ability for users to ask questions to other users on the site. They can do this by navigating to the feed page, entering their post in the forum and then submit the query. Users will need to enter a post title, a more detailed description in the post content and a rank of importance for the question out of 10 before submitting a question. Once a question has been submitted it will be uploaded and can be found on the feed.

### <br>**Individual Posts** ### 
Users are able to go to an individual post's page via clicking the post's title in the feed. From this page the complete content of the post is displayed including the creator, title, in depth post information, the attached images and any replies. The original creator of the post is able to attach an image to the post from this page and edit or delete the post. Other users can reply to the post or follow/unfollow the post from this page.
 
### <br>**User Index** ###
This page contains a list of all users on the site, including their names and emails.
 
### <br>**User Account Page** ###
On this page users are able to access their individual account information, including the posts that they are following and the total self-ranked importance of the questions they've asked. Individuals are also able to edit their username and password from this page.

# <center><br> Installation Instructions </center> #
1) This application is written in Python 3 and it is assumed that users have it downloaded and installed on their computers. If not follow this link and the instructions to fulfill this requirement https://www.python.org/downloads/.
 
2) The databases for this program runs on PostgreSQL. If you do not have it downloaded follow this link and instructions and install the software according to the appropriate operating system https://www.postgresql.org/download/. Notably, some users may first have to install the software Homebrew to install PostgreSQL and a link to explaining how to install Homebrew is attached https://brew.sh/.
 
3. Once both Python and PostgreSQL are installed, ensure you have the file which contains the code for the application downloaded onto your computer. Navigate into the (initial) q_and_a_app directory from your command line with the command ‘CD’ till you reach the appropriate folder.
 
4. As this application uses a lot of packages a virtual environment is needed to be created and activated. Depending on which operating system you are using, the commands in the terminal may vary slightly to create a venv. The official documentation for creating a virtual environment in Python can be found here https://docs.python.org/3/library/venv.html.
 
5. Once your environment has been created make sure it is activated by following the commands in the documentation above.
 
6. Finally, all the packages from the requirements.txt must be installed before the application can be run. This can be achieved by running the command 'pip install -r requirements.txt' in the command line. Make sure you are still in the directory outlined above.

# <center><br> Set Up Instructions </center> #
1. Ensure all the necessary software and dependencies discussed in the installation instructions have been downloaded and are ready to go on your machine.
 
2. Navigate into the directory named ‘q_and_a_app’ via the terminal.
 
3. In order to create the databases for the website to run type the following command into your terminal 'flask db init'.
 
4. Next type in the command 'flask db migrate -m "initial migration"'.
 
5. Finally enter 'flask db upgrade' into your terminal and the databases should now be functioning.
 
6. Enter the command 'flask run' to launch the application.
 
7. The application will now be running on your local host if you have followed all the steps correctly. Type the address 'http://127.0.0.1:5000/' into your browser to access the site.
 
8. In order to stop running the application type 'CTRL+C' into your terminal.