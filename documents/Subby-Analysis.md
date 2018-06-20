# Subby

---
## Requirements Document
Version 1.0 – 5/20/18
1. **[Introduction](#1introduction)**  
  1.1. [Purpose](#11purpose)  
2. **[Object Classification](#2objectclassification)**  
  2.1. [Class Diagram](#21classdiagram)  
  2.2. [Packages](#22packages)  
  2.2.1. [User Package](#221userpackage)  
  2.2.2. [Sublet Package](#222subletpackage)  
  2.2.3. [Rating Package](#223ratingpackage)  
  2.2.4. [Favorite Package](#224favoritepackage)  
  2.2.5. [Report Package](#225reportpackage)  
3. **[Requirements](#3requirements)**  
  3.1. [Database](#31database)  
  3.1.1 [Administrator Terms of Use](#311administratortermsofuse)  
  3.1.2 [User Terms of Use](#312usertermsofuse)
4. **[Model Analysis](#4modelanalysis)**  
  4.1. [UML Diagram](#41umldiagram)
5. **[User Interface Specification](#5userinterfacespecification)**  
  5.1 [Sequence Diagram](#51sequencediagram)  
  5.2. [Task List](#52tasklist)  
  5.2.1. [Task Specifications](#521taskspecifications)  
6. **[Revision History](#40revisionhistory)**  

# 1. Introduction

Improving the current state of subletting would be beneficial to students throughout our target market (KW Region), as we will be able to consolidate listings posted on non-specialized platforms, as well as provide quality assurance on the posted listings. The database of sublet listings will be organized based on standard filters for renting such as location, rating, etc.

The website will display the listing information found in the database in the form of text, diagrams, or maps. The website will allow administrators to insert, edit, and remove entries from the database/website at their discretion. A website user would be allowed access to the data on the front-end and browse through the listings on the site, as well as post new listings. 

## 1.1. Purpose
The current state of subletting is disorganized and inconvenient to use, with the most popular platform being FaceBook- a site not even designed for posting sublets. Subby will allow for listings on FaceBook, Kijiji, and other sites to be consolidated, thus providing  a more comprehensive product than what is currently available to the student sublettng market. 

The idea is to provide:
1. **Subletters:**
    * Simple interface to browse through sublet listings, easily sorted using specialized filters
    * Ability to contact sublessors through site or through provided contact information
    * Security in browsing since all listings will go through a verification process to confirm legitimacy
2. **Sublessors:**
    * Ability to post new sublet listings according to site policy
    * Ability to modify existing listings in case any information changes
    * Allows for listings to be seen by verified users, and be contacted by these users
    * Provide an interface to let one know the current competitive pricing in the property area
3. **Administrators:**
    * All functionality available to users, as well as the ability to remove and edit any listing at their discretion
# 2. Object Classification
Here we have provided all entity, boundary, and control objects found in all the Packages. They are broken down later in the Model Analysis.

## 2.1. Class Diagram

This class diagram shows an overall picture of the various actor interactions, as well as controller/entity packages to which the GUI's pertain. Note that some views will potentially retrieve data from more than one source; these have been indicated with dashed lines.

![SubbyClassDiagram](http://i.imgur.com/64hk0Jr.jpg)

## 2.2. Packages

### 2.2.1. User Package

The User package contains the following:
* **Entity Object:** User
* **Control Objects:**
    * User Creator: Create and persist Users to the database.
    * User Manager: Edit and Destroy Users.
    * User Retriever: Retrieve single records of a User for display.
    * User Lister: List the index of Users.
* **Border Objects:**
    * User Sign-Up: Submit email, password, and other relevant data to create an account.
    * User Edit: Modify preferences, email, password.
    * User Display: View a user's data.
    * User List: List all users in the database.

As displayed in the Class Diagram, visitors are the only actors who will be able to use the User Creator view and controller. Administrators and regular users will be able to display accounts, and possibly edit them depending on their role.

### 2.2.2. Sublet Package

The Sublet package contains the following:
* **Entity Object:** Sublet
* **Control Objects:**
    * Sublet Creator: Create and persist Sublets to the database.
    * Sublet Manager: Edit and Destroy Sublets.
    * Sublet Lister: List the index of Sublets.
    * Sublet Searcher: Searches for Sublet records, taking params such as search query and page number.
    * Sublet Retriever: Retrieve single records of a Sublet for display.
* **Border Objects:**
    * Sublet Create: Provide input to create a sublet listing- address, description, and so on.
    * Sublet Edit: Edit an existing sublet posting.
    * Posted Sublet List: List of posted sublets in a given area.
    * Sublet Search: Search for sublets by user input with filters.
    * Sublet Display: Display a single sublet.

Note that controllers such as the Sublet Manager will determine, based on User role, whether an actor has permission to edit or destroy a Sublet record. The Sublet Searcher controller will have no such authorization, as it is open to both visitors and regular users.

### 2.2.3. Rating Package

The Rating package contains the following:
* **Entity Object:** Rating
* **Control Objects:**
    * Rating Creator: Create and persist Ratings to the database.
    * Rating Manager: Edit and Destroy Ratings.
    * Rating Retriever: Retrieve single records of a Rating for display.
* **Border Objects:**
    * Rating Create: Provides input to set a rating level.
    * Rating Edit: Edit an existing rating.
    * Rating Display: Display a list of ratings for a user.

Note that both the User Display UI, Sublet Search UI, and Sublet Display UI will also use the Rating Retriever Control to display Rating information on their respective pages.

### 2.2.4. Favorite Package

The Favorite package contains the following:
* **Entity Object:** Favorite
* **Control Objects:**
    * Favorite Lister: Retrieve all of a User's Favorites to display the related Sublet listings.
    * Favorite Manager: Create and destroy Favorite entities.
* **Border Objects:**
    * Favorites List: Displays a list of favorites belonging to a user.

The Sublet Search UI will display whether a Sublet listing has been "Favorited", and will access the Favorites Manager. 

### 2.2.5. Report Package

The Report package contains the following:
* **Entity Object:** Report
* **Control Objects:**
    * Report Creator: Create and persist Reports to the database.
    * Report Retriever: Retrieve single records of a Report for display.
    * Report Lister: Retrieve all of a User's Reports to display the related Sublet listings.
* **Border Objects:**
    * Report Create: Display input areas necessary to create a Report.
    * Report Display: Display a user's Report.
    * Reports List: Display a list of Reports from a given user.

The Reports UI's will be available to both regular and admin users, so records will need to be persisted and retrieved regardless of authorization.

# 3. Requirements

## 3.1 Database
Administrators are allowed to modify website content when logged in, while general users may view website content, insert content, and modify their inserted content. 

### 3.1.1. Administrator Terms of Use
An administrator is one of two actors in the system, and is allowed to insert, edit, and remove both users and content from the site.

### 3.1.2. User Terms of Use
The user is the second of two actors in the system, and is allowed to insert content into the site and edit their inserted content.

# 4. Model Analysis

## 4.1. UML Diagram

This UML diagrams displays the various models required to accomplish the above use-cases, as well as their attributes and relations.

![SubbyUML](http://i.imgur.com/N7jpNTX.jpg)

# 5. User Interface Specification

## 5.1. Sequence Diagram

![SQCreateUser](https://i.imgur.com/XNlL1ft.png)

Figure 5.2. Sequence Diagram for Task 1 and 2.

A sequence diagram is provided for task 1 and Task 2 for an admin to log in to the management tool, and create a new user. This flow begins with an administrator required to log in, however there is no need to log out after a task is completed. Thus, an administrator can freely execute multiple tasks in one session.

## 5.2. Task List
A sample task list for an administrator:

1. Logging into Subby management tool.
2. Creating a user.
3. Modifying an existing user's information.
4. Deleting a user.
5. Deleting a sublet listing.
6. Logging out Subby management tool.

A sample task list for the user:

7. Creating an account using Subby sign-up interface.
8. Logging into Subby using login interface. 
9. Inserting a new sublet listing.
10. Modifying an existing sublet listing.
11. Viewing/filtering/selecting posted listings.
12. Rating a listing. 

### 5.2.1. Task Specifications
**Task 1: Logging into Subby management tool.**
The user has opened a web browser and has navigated to the Subby management tool log in page. The user enters valid admin credentials and logs in by selecting the "Login" button.

**Task 2: Creating a user. (Prerequisites: Task 1 as Administrator)**
An administrator selects the "Create User" which generates a overlayed display that prompts them to fill in fields such as:
* Username
* Password
* E-mail Address
* Birth Date

An administrator enters the relevant information and selects the "Create" button. If the user information already exists in the database, there will be an error message saying that the entry is a duplicate, otherwise a notification will prompt the admin of successful user creation.

**Task 3: Modifying an existing user's information. (Prerequisites: Task 1, Task 2 if no users currently exist)**
An administrator looks at the current database of users, and selects the "Edit User" action next to a user entry. A new page will be loaded displaying the information of the selected user. An administrator will be prompted to edit any of:
* Username
* Password
* E-mail
* Birth Date

As well as the ability to see all listings currently posted by the selected user (The ability to complete task 5 and 10 is available here as well if there are available listings). An administrator enters and information changes desired, and presses the "Save" button at the bottom of the form. Should there be an error such as duplicate information in the database found, an error message will be displayed, otherwise the information should save. Alternatively, should the administrator deem no changes neccesary, there is a "Cancel" button next to the save to bring the administrator to their previous viewing page.

**Task 4: Deleting a user. (Prerequisites: Task 1, Task 2 if no users currently exist)**
An administrator will view all the users entered in the database, and select the "Delete User" button next to the data entry. This will issue a prompt asking for confirmation as to whether or not to proceed with the deletion. Should the administrator press "Confirm", the data entry will be removed from the database, else the administrator will press "Cancel" resulting in the prompt disappearing and no changes occurring to the database. Deleting a user will also remove all listings posted by said user.

**Task 5: Deleting a sublet listing. (Prerequisites: Task 1)**
An administrator will view the database containing all listings, and select the "Delete Listing" button next to the data entry. This will issue a prompt asking for confirmation as to whether or not to proceed with the deletion. Should the administrator press "Confirm", a prompt will appear with a textbox asking the administrator to file a reason for deletion. The admin will fill in a relevant reason, and press "Okay". The data entry will be removed from the database, and a message to the lister will be sent with the reason specified for deletion. Otherwise the administrator will press "Cancel" resulting in the prompt disappearing and no changes occurring to the database.

**Task 6: Logout. (Prerequisites: Task 1)**
An administrator will press the "Log out" button in the top right corner of the management tool, which will take the user back to the log in page.

**Task 7: Creating an account using Subby sign-up interface.**
The user has navigated to the home page of Subby. The user will press the "Register" button in the top right corner of the website, which will create an overlay over the current page prompting the user to enter the following information:
* Username
* Password
* E-mail
* Birth Date

As well as passing a captcha to ensure human entry. A link to terms of service and privacy policy will be included below the form for the user to read if neccesary. Upon entering the correct information, the user will press the "Sign Up" button at the bottom of the overlay, which will then prompt the user as to whether or not the account creation was successful. A successful account creation must follow the following criteria:
* Non-duplicate username
* Password conforming to site-specified rules
* Non-duplicate e-mail address
* Valid captcha entry
Upon success, the overlay will disappear and be replaced by a pop-up informing the user that a verification email has been sent to their address. Upon failure, the form will highlight where the errors are in red around the specific entries and prompt the user to enter their information again.

**Task 8: Logging into Subby using login interface. (Prerequisites: Task 7)**
The user will log in by selecting the "Login" button in the top right corner of the web page. This will create an overlay over the current page prompting the user to enter their login information:
* Username/E-mail
* Password

Upon entering their credentials, the user will select the "Sign in" button at the bottom of the overlay, which will then prompt the user if their credentials were correct or not. If they were correct, the user will be redirected to the home page, otherwise the overlay will display an error message saying invalid credentials were entered.

**Task 9: Inserting a new sublet listing. (Prerequisites: Task 8)**
The user will select the "Post Listing" button in the top right corner of the page. This will load a new page containing a form for the user to fill out about their listing. Information includes:
* Location
* Price per month
* Duration of sublet
* Special features 
* Picture Attachments

Upon entering the relevant information, the user will press the "Post" button at the bottom of the form which will prompt the user with either a success message or an error message based on whether the post went through. The user may also cancel a new listing by pressing the "Cancel" button next to the "Post" button.

**Task 10: Modifying an existing sublet listing. (Prerequisites: Task 8, Task 9 if no posted listings)**
The user will navigate to their "my listings" to view all current listings posted by themselves. The user will select the "Edit" hyperlink next to a listing, and be directed to a new page containing a form with the listing information. The user will be able to edit any information they entered in task 9, as well as have the ability to mark the listing as "Sold". Upon making the relevant changes, the user will press the "Save" button at the bottom of the form to confirm any changes they made. The user may also cancel editing by pressing the "Cancel" button next to the "Save" button.

**Task 11: Viewing/filtering/selecting posted listings.**
The user has navigated to the home page of Subby. The user will enter a location into the search bar loading a new page containing top listings closest to the location specified in the search bar. The user will be presented with filter options on the right hand side of the page, which allows the user to narrow their results to their specifications. The user will press the "Filter" button upon selecting desired filters, and the page will be reloaded showing a search of new sublets fulfilling their needs. The user will select a listing that interests them which will redirect them to the individual listing page displaying all information about the sublet to the user. The user has the ability to view the sublessor contact information on the right hand side of the page if they are interested in making an offer.

**Task 12: Rating a listing (Prerequisites: Task 8)**
The user has navigated to an individual listings page. The user will hover over the stars on the listings page at a desired rating level and press down when they are satisfied with the rating they are giving. The user will be prompted to submit proof of lease for the rating in an overlay which allows the user to submit an attachment. Once the user has attached their lease, the user will press the "Submit" button allowing for the rating to go through.

# 6.0. Revision History

---
## Version 1.1
* **Section 2**
  * Alex Kirsopp [2.1-2.2.5] [2018-06-19]
* **Section 4**
  * Alex Kirsopp [4.1] [2018-06-19]

* **Other**
  * Alex Kirsopp - Misc small fixes (spelling, wording, layout, markdown)

## Version 1.0
* **Section 1**
  * Mackenzie Dang [1.0-1.1] [2018-06-03] Initial Draft
* **Section 2**
  *  Alex Kirsopp [2.1.1-2.1.4, 2.4] [2018-06-03]
* **Section 3**
  * Mackenzie Dang [3.0 - 3.1.2.] [2018-06-03] Initial Draft
* **Section 4**
  *  Alex Kirsopp [4.1] [2018-06-03]
* **Section 5**
  * Mackenzie Dang [5 - 5.2] [2018-06-03] Initial Draft

* **Other**
  * Alex Kirsopp - Doc layout and formatting
