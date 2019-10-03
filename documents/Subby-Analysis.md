# Subby

---
## Analysis Document
Version 1.2 - 06/27/18
1. **[Introduction](#1introduction)**  
  1.1. [Purpose](#11purpose)  
2. **[Object Classification](#2objectclassification)**  
  2.1. [Class Diagram](#21classdiagram)  
  2.2. [Packages](#22packages)  
  2.2.1. [User Package](#221userpackage)  
  2.2.2. [Sublet Package](#222subletpackage)  
  2.2.3. [Rating Package](#223ratingpackage)  
  2.2.4. [Favourite Package](#224favouritepackage)  
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

The website will display the listing information found in the database in the form of text, diagrams, or maps. The website will allow administrators to insert, edit, and remove entries from the database/website at their discretion. The general users would be allowed access to the data on the front-end and browse through the listings on the website, as well as posting new listings.

## 1.1. Purpose
The current state of subletting is disorganized and inconvenient to use, with the most popular platform being Facebook - a site not even designed for process of subletting. Subby will allow for listings on Facebook, Reddit, and other sites to be consolidated, thus providing a more comprehensive product than what is currently available to the student sublettng market.

The idea is to provide:
1. **Subletters:**
    * Simple interface to browse through sublet listings which are easily sorted using specialized filters
    * Ability to contact sublessors through site or through provided contact information
    * Security in browsing since all listings will go through a verification process to confirm legitimacy in ownership/ability to lease
2. **Sublessors:**
    * Ability to post new sublet listings that complies with site policy
    * Ability to modify existing listings in case any information changes
    * Allows for listings to be seen by and be contacted by verified users
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
    * User Creator: Create and persist Users to the database
    * User Manager: Edit and Destroy Users
    * User Retriever: Retrieve single records of a User for display
    * User Lister: List the index of Users
* **Boundary Objects:**
    * User Sign-Up: Submit email, password, and other relevant data to create an account
    * User Edit: Modify preferences, email, password
    * User Display: View a User's data
    * User List: List all Users in the database

As displayed in the Class Diagram, visitors are the only actors who will be able to use the User Creator view and controller. Administrators and regular users will be able to display accounts, and possibly edit them depending on their role.

### 2.2.2. Sublet Package

The Sublet package contains the following:
* **Entity Object:** Sublet
* **Control Objects:**
    * Sublet Creator: Create and persist Sublets to the database
    * Sublet Manager: Edit and Destroy Sublets
    * Sublet Lister: List the index of Sublets
    * Sublet Searcher: Searches for Sublet records, taking params such as search query and page number
    * Sublet Retriever: Retrieve single records of a Sublet for display
* **Boundary Objects:**
    * Sublet Create: Provide input to create a sublet listing- address, description, and so on
    * Sublet Edit: Edit an existing sublet posting
    * Posted Sublet List: List of posted sublets in a given area
    * Sublet Search: Search for sublets by user input with filters
    * Sublet Display: Display a single sublet

Note that controllers such as the Sublet Manager will determine, based on User role, whether an actor has permission to edit or destroy a Sublet record. The Sublet Searcher controller will have no such authorization, as it is open to both visitors and regular users.

### 2.2.3. Rating Package

The Rating package contains the following:
* **Entity Object:** Rating
* **Control Objects:**
    * Rating Creator: Create and persist Ratings to the database
    * Rating Manager: Edit and Destroy Ratings
    * Rating Retriever: Retrieve single records of a Rating for display
* **Boundary Objects:**
    * Rating Create: Provides input to set a rating level for a new Rating object
    * Rating Edit: Edit an existing Rating
    * Rating Display: Display a list of ratings for a User

Note that both the User Display UI, Sublet Search UI, and Sublet Display UI will also use the Rating Retriever Control to display Rating information on their respective pages.

### 2.2.4. Favourite Package

The Favourite package contains the following:
* **Entity Object:** Favourite
* **Control Objects:**
    * Favourite Lister: Retrieve all of a User's Favourites to display the related Sublet listings
    * Favourite Manager: Create and destroy Favourite entities
* **Boundary Objects:**
    * Favourites List: Displays a list of favourites belonging to a User

The Sublet Search UI will display whether a Sublet listing has been "Favourited", and will access the Favourites Manager. 

### 2.2.5. Report Package

The Report package contains the following:
* **Entity Object:** Report
* **Control Objects:**
    * Report Creator: Create and persist Reports to the database
    * Report Retriever: Retrieve single records of a Report for display
    * Report Lister: Retrieve all of a User's Reports to display the related Sublet listings
* **Boundary Objects:**
    * Report Create: Display input areas necessary to create a Report
    * Report Display: Display a user's Report
    * Reports List: Display a list of Reports from a given User

The Reports UI's will be available to both regular and admin users, so records will need to be persisted and retrieved regardless of authorization.

# 3. Requirements

## 3.1 Database
Administrators are allowed to modify and delete website content when logged in, while general users may view website content, insert content, and modify their inserted content. 

### 3.1.1. Administrator Terms of Use
An administrator is one of two actors in the system, and is allowed to insert, edit and remove both users and content from the site.

### 3.1.2. User Terms of Use
The user is the second of two actors in the system, and is allowed to insert content into the site and edit their inserted content.

# 4. Model Analysis

## 4.1. UML Diagram

This UML diagrams displays the various models required to accomplish the above use-cases, as well as their attributes and relations.

![SubbyUML](https://i.imgur.com/PdYF7h9.jpg)

# 5. User Interface Specification

## 5.1. Sequence Diagram

![SQCreateUser](https://i.imgur.com/XNlL1ft.png)

Figure 5.1. Sequence Diagram for Task 1 and Task 2.

A sequence diagram is provided for Task 1 and Task 2 for an admin to log in to the management tool and create a new user. This flow begins with and administrator logging in. However, there is no need to logout after a task is completed. Thus, an administrator can freely execute multiple tasks in one session.

![SQUserTasks](https://i.imgur.com/STNS7Zt.png)

Figure 5.1.1 Sequence Diagram for Tasks 7, 8, 9 and 11.

A sequence diagram is also provided to outline the basic user tasks.



## 5.2. Task List
A sample task list for an administrator:

1. Logging into Subby management tool
2. Creating a user
3. Modifying an existing user's information
4. Deleting a user
5. Deleting a sublet listing
6. Logging out of Subby management tool

A sample task list for the user:

1. Creating an account using Subby sign-up interface
2. Logging into Subby using login interface 
3. Inserting a new sublet listing
4. Modifying an existing sublet listing
5. Viewing/filtering/selecting posted listings
6. Rating a listing

### 5.2.1. Task Specifications

#### Administrator Tasks:

**Task 1: Logging into Subby management tool.**
The user opens a web browser and navigates to the Subby management tool login page. The user enters valid admin credentials and logs in by selecting the "Login" button.

**Task 2: Creating a user. (Prerequisites: Task 1 as Administrator)**
An administrator selects the "Create User" which generates an overlayed display that prompts them to fill in the following fields:
* Username
* Password
* E-mail Address
* Birth Date

An administrator enters the relevant information and selects the "Create" button. If the user information already exists in the database, an error message is displayed, indicating that the entry is a duplicate. Otherwise, a notification will prompt the admin of successful user creation.

**Task 3: Modifying an existing user's information. (Prerequisites: Task 1, Task 2 if no users currently exist)**
An administrator looks at the current database of users, and selects the "Edit User" action next to a user entry. A new page is loaded displaying the information of the selected user. The administrator is then prompted to edit any of the following:
* Username
* Password
* E-mail
* Birth Date

Additionally, the administrator is afforded the ability to see all listings currently posted by the selected user; the ability to complete Tasks 5 and 10 can also be done within Task 3 if any available listings exist. An administrator makes the desired information changes and presses the "Save" button at the bottom of the form. Should the administrator attempt to make invalid changes, such as duplication of information, an error message will be displayed. Otherwise, the information is committed. Alternatively, should the administrator deem no changes neccesary, there is a "Cancel" button next to the "Save" button to bring the administrator to their previous viewing page.

**Task 4: Deleting a user. (Prerequisites: Task 1, Task 2 if no users currently exist)**
An administrator views all the users entered in the database, and selects the "Delete User" button next to the data entry. This issues a prompt asking for confirmation as to whether or not to proceed with the deletion. Should the administrator press "Confirm", the data entry will be removed from the database. Otherwise, the administrator presses "Cancel", resulting in the prompt disappearing and no changes occurring to the database. Note that deleting a user will also remove all listings posted by said user.

**Task 5: Deleting a sublet listing. (Prerequisites: Task 1)**
An administrator views the database containing all listings, and selects the "Delete Listing" button next to the data entry. This issues a prompt asking for confirmation as to whether or not to proceed with the deletion. Should the administrator press "Confirm", a prompt will appear with a form asking the administrator to file a reason for deletion. The admin then fills in a relevant reason for deletion, and presses "Okay". The data entry will be removed from the database, and a message to the lister is sent with the reason specified for deletion. Otherwise, the administrator presses "Cancel" resulting in the prompt disappearing and no changes occurring to the database.

**Task 6: Logout. (Prerequisites: Task 1)**
An administrator presses the "Logout" button in the top right corner of the management tool, which take the user back to the login page.

#### User Tasks:

**Task 1: Creating an account using Subby sign-up interface.**
The user navigates to the home page of Subby and presses the "Register" button in the top-right corner of the website, creating an overlay over the current page prompting the user to enter the following information:
* Username
* Password
* E-mail
* Birth Date

Additionally, the user must pass a captcha to ensure human entry. A link to terms of service and privacy policy will be included below the form for the user to read if neccesary. Upon entering the correct information, the user presses the "Sign Up" button at the bottom of the overlay, which will then prompt the user as to whether or not the account creation was successful. A successful account creation must follow the following criteria:
* Non-duplicate username
* Password conforming to site-specific rules
* Non-duplicate e-mail address
* Valid captcha entry
Upon success, the overlay will disappear and be replaced by a pop-up informing the user that a verification email has been sent to their address. Upon failure, the form will highlight where the errors are in red around the specific entries and prompt the user to enter their information again.

**Task 2: Logging into Subby using login interface. (Prerequisites: Task 7)**
The user logs in by selecting the "Login" button in the top-right corner of the web page. This creates an overlay over the current page prompting the user to enter their login information:
* Username/E-mail
* Password

Upon entering their credentials, the user selects the "Sign-in" button at the bottom of the overlay, which then indicates to the user whether or not their credentials are valid or not. If the former, the user is redirected to the home page, otherwise the overlay displays an error message indicating that invalid credentials are entered.

**Task 3: Inserting a new sublet listing. (Prerequisites: Task 8)**
The user selects the "Post Listing" button in the top right corner of the page. This loads a new page containing a form for the user to fill out about their listing. Such listing fields include: 
* Location
* Price per month
* Duration of sublet
* Special features 
* Picture Attachments
* Furniture
* Utilities

Upon entering the relevant information, the user presses the "Post" button at the bottom of the form which prompts the user with either a success message or an error message based on whether the fields contain incorrect or no data or not. The user may also cancel a new listing by pressing the "Cancel" button next to the "Post" button.

**Task 4: Modifying an existing sublet listing. (Prerequisites: Task 8, Task 9 if no posted listings)**
The user navigates to their "My Listings" to view all their currently posted listings. The user selects the "Edit" hyperlink next to a listing, and is directed to a new page containing a form with the listing information. The user is able to edit any information they entered in Task 9, as well as have the ability to mark the listing as "Sold". Upon making the relevant changes, the user presses the "Save" button at the bottom of the form to confirm any changes they made. The user may also cancel editing by pressing the "Cancel" button next to the "Save" button.

**Task 5: Viewing/filtering/selecting posted listings.**
Task 5: Viewing/filtering/selecting posted listings. The user navigates to the home page of Subby and enters a location into the search bar. Subsequently, a new page containing top listings closest to the location specified is loaded. The user is presented with filter options on the right hand side of the page, which allows the user to refine their results to their liking. Once the desired filters are selected, the user presses the "Filter" button to view the corresponding search results. Then, the user selects the listing of their interest, redirecting them to the individual listing page which displays all the relevant information about the sublet. Additionally, The user has the ability to contact the sublessor through "Contact Sublessor?" option on the bottom portion of the page, if they are interested in making an offer.

**Task 6: Rating a listing (Prerequisites: Task 8)**
Task 6: Rating a listing (Prerequisites: Task 8) The user has navigates to individual pages with listing details. The user hovers over the stars on the "Write a Review" page (navigated to with "View Reviews" option on each listing details page) at a desired rating level and press down when they are satisfied with the rating they are giving for the sublessor. The user then presses the "Submit" button allowing for the rating to go through.

# 6.0. Revision History

---
## Version 1.3

* **SQA Fixes**
    * Mackenzie Dang [1, 3, 5] [2018-07-04]

## Version 1.2

* **SQA Fixes**
    * Alex Kirsopp [2.1-2.2.5] [2018-06-27]

## Version 1.1
* **Section 2**
    * Alex Kirsopp [2.1-2.2.5] [2018-06-19]
* **Section 4**
    * Alex Kirsopp [4.1] [2018-06-19]
* **Section 5**
    * Mackenzie Dang [5.1.1] [2018-06-20] 

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
