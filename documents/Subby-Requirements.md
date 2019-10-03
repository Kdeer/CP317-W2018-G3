# Subby

---
## Requirements Document
Version 1.0 – 5/20/18
 1. **[Introduction](#1introduction)**  
     1.1. [Purpose](#11purpose)  
     1.2. [Scope](#12scope)  
     1.3. [Document Lexicon](#13documentlexicon)  
        1.3.1. [Definitions](#131definitions)  
        1.3.2. [Acronyms and Abbreviations](#132acronymsandabbreviations)  
     1.4. [References](#14references)  
     1.5. [Overview](#15overview)  
2. **[Overall Description](#2overalldescription)**  
    2.1. [Product Perspective](#21productperspective)  
        2.1.1. [Front-End Users](#211frontendusers)  
        2.1.2. [Back-End Users](#212backendusers)  
        2.1.3. [Other Features](#213otherfeatures)  
        2.1.4. [Sample GUI](#214samplegui)  
    2.2. [Product Functions](#22productfunctions)  
    2.3. [User Characteristics](#23usercharacteristics)  
    2.4. [Constraints](#24constraints)  
    2.5. [Assumptions and Dependencies](#25assumptionsanddependancies)  
3. **[Specific Requirements](#3specificrequirements)**  
    3.1. [External Interfaces](#31externalinterfaces)  
    3.2. [Functions](#32functions)  
    3.3. [Logical Database Requirements](#33logicaldatabaserequirements)  
    3.4. [Portability](#34portability)  
4. **[Revision History](#40revisionhistory)**  


# 1. Introduction

---
A major issue many students face in their time at post-secondary school is the dreaded one-year lease. Most students scramble to find potential candidates to take over their lease as their semester comes to an end. This is where Subby comes into play: Subby is an easy-to-use website that enables students to either sublet their place or simply find a sublet of their own. The goal of Subby is to create a one-stop marketplace for sublets as opposed to the current struggle of students using multiple sites. The site comes with a variety of useful features such as a localized map and search priorities that allow for a visually appealing and detailed search.


### 1.1. Purpose
This document outlines the features that Subby will provide to users and administrators. Throughout the term, members on the Subby team will refer to this document and make changes as necessary.

### 1.2. Scope
As an online student-to-student subletting service, Subby seeks to streamline the way in which tenants and subletters can connect with one another. In contrast to other lodging services, Subby specialises in subletting exclusively between university and college students for periods of four or eight months. For the time being, Subby will only facilitate subletting listings within the Kitchener-Waterloo (KW) region.

### 1.3. Document Lexicon

#### 1.3.1. Definitions
* **Sublet:** The action of leasing a property to someone else.
* **Sublet Seeker/Lessee:** The person looking to sublet a place.
* **Lease Owner/Lessor:** The person looking to rent their place to someone else.

#### 1.3.2. Acronyms and Abbreviations
* **API - Application Programming Interface:** Tools for building application software.

### 1.4. References
Based on [IEEE Std 830-1998](https://standards.ieee.org/findstds/standard/830-1998.html).

### 1.5. Overview
The remaining elements of this document highlights the functions and appearance of the Subby website. 

# 2. Overall Description

---
**Renting with Subby:**
Those students seeking to sublet a residence can use the rental database at any time without charge and without
a Subby account. A hopeful subtenant can search for housing using customized search filters designed with
student renters in mind. Thus, in addition to standard search fields such as price and location (by address or
location), search results can be further refined by:
 
 * **Property Type** – single bedroom, shared bedroom, etc  
 * **Size** – number of beds/bedrooms/washrooms
 * **Distance from Campus** -- distance range from a given university campus
 * **Convenience** -- how convenient is it to reach a nearby plaza, gym, etc
 * **Availability** -- move-in date
 * **Rental Period** -- users can sublet for periods of four or eight months
 * **Keyword Search** -- search for features and amenities such as ‘on-site laundry’
 * **Number of Roommates** -- the number of roommates expected to occupy residence during their stay
 * **Leasee Rating** -- the star-point rating of the lease owner and the unit from a scale of 0 to 5 stars

Once a sublet seeker finds a unit to their liking, they must create a profile of their own using a university email
to be able to add the property to their ‘Wish List.’ Otherwise, the sublet seeker may directly contact the lessee by sending them a message of interest through the communication form which is found on every listing page.

**Subleasing with Subby:**
To promote available rental units, users must first register and create an account using a valid university email. Once the user has successfully registered, they may create a listing for their residence(s) under ‘My Listings’ and promote said listing through a title, description, location and up to 20 captioned photographs. A myriad of search fields including price, property type, rental period and size will be available to make searching easier. 
 
Moreover, registered users can create personalized profiles so that potential subtenants may get to know the lessee a little better. Under "My Profile," a user can include their name, contact information, and profile description in addition to uploading a profile picture.


### 2.1. Product Perspective

The website will utilize Google Maps API to help users locate and post sublets in the KW region. 

#### Actors and Use Cases

![Use Case Chart](https://i.imgur.com/6lY7PvN.png)

#### 2.1.1. Front-End Users
The front-end user interface will be simplistic in design to allow users of all computer literacy to navigate the site. The homepage will consist of a search bar in the center of the page where students can search for sublets. Additionally, a sign-in link and a register link will be located at the top-left of the homepage. Since the website is targeted towards students, individuals will have to register using a university or college email address. Accordingly, the amount of fake accounts can be reduced, resulting in less spam.

There will be two main feature sets available to front-end users:
1. **Lease Owner – the individual looking to sublet their place**
    * These individuals must register to post
    * After registration, they may post details about the property they are subletting (i.e. pictures, brief description of their place, price, location) 
    * They can edit their post at any time (i.e. lower the price, mark as sold, delete the listing)
    * They can share their posts to social sites like Twitter, Facebook, etc.

2. **Sublet Seeker – the individual looking for a sublet**
    * These individuals do not have to register to use the website
    * They can edit the location and set various filters on their searches (i.e. they want a sublet near Laurier for 4 months under $500 with an ensuite bathroom)
    * Once they see a sublet they’re interested in, they can contact the lease owner with a contact form set to the lease owner’s email
    * They could also choose to register and post a “WANTED” advertisement if they do not see anything that meets their requirements
    * Will have a “FAVOURITE” and “SHARE” function – if users find a room they like, they could add them to a list of potential sublets they’re interested in or share it with a friend who might be interested in it as well
    
#### 2.1.2. Back-End Users / Administrators
The administrator users will have access to special features to maintain user accounts and enforce rules.

Here are the main features available for back-end users: 
* **Regulate Rules:** The administrators of Subby will be able to adjust the rules that govern regular users, such as the number of listings they can have up at any time, or the maximum distance from K/W they are allowed to post.
* **Enforce Rules:** Administrators will give appropriate punishments to individuals who violate the terms of using Subby (i.e. spamming, scamming, etc). Punishments include giving them warnings and banning their accounts.
* **Provide Customer Service:** Individuals will be able to contact a Subby administrator by email if any problems or questions arise. Administrators will be able to reset passwords and email addresses to ensure users have account access.

#### 2.1.3. Additional Features
* **Review:** Both sublet seekers and lease owners can rate each other based on their experience on a scale of 0 to 5. For instance, the sublet seeker can rate their experience with the lease owner based on the satisfaction of their stay and the lease owner can rate their experience with the sublet seeker based on payment reliability and property damage (or lack thereof). This will allow individuals to trust others more freely if they have good reviews.

* **Competitive Pricing:** On the search results page, there will be two boxes that show the competitive pricing. One box will show the lowest rent price set up by lease owners of rooms (same type) in same building, or by leases of same criteria [same criteria? as in same search results?]. The other box will show the highest bidding set by sublet seekers for either rooms (same type) in same building or rooms that fulfill same criteria. The purpose of this feature is to show the competitive pricing of each unit listed. This way, people will have better understanding of how much they should be paying for a sublet or of how much they should charge for subletting their unit.

* **Tinder-Style Swipe:** Provide an interface allowing users to easily narrow down their search by quickly viewing photos of potential sublets. For mobile devices, the user could swipe "left" to ignore a sublet- or "right" to view more information and contact the lessor. Desktop users would either tap the left or right arrow keys respectively to achieve the same result.

#### 2.1.4. Sample GUI
**Home Page:**

![Home](https://i.imgur.com/b15lkY9.jpg)

**Sign-up Overlay:**

![Sign-up Overlay](https://i.imgur.com/Zyjz1fQ.jpg)

**Search Results Page:**

![Search Results](https://i.imgur.com/vR9HFiG.jpg)

**(Single) Listing Page:**

![Single Listing](https://i.imgur.com/1b1d2vy.jpg)

**User "My Listings" Page:**

![User "My Listings"](https://i.imgur.com/Cqlj6j5.jpg)

**User "Reporting Issue" Page:**

![User "Reporting Issue"](https://i.imgur.com/xOPc6zi.jpg)

**User "My Account" Page:**

![User "My Account" V2](https://i.imgur.com/b0Nhu2B.jpg)

### 2.2. Product Functions
Every individual will have the option to search for sublets. Registered users will be able to post listings. Everyone will have access to the Google Maps displaying the subletting options. If a user has specific requirements that need to be met, then they can use the filters while searching for a sublet. In addition, if a person is looking to sublet their place, they can search for individuals looking for a specific sublet using the filters. Individuals can directly message each other using the emails they registered with.  

### 2.3. User Characteristics
Subby is made for students with basic knowledge of how to navigate a website. The website will be designed to be as straightforward as possible so even the most non-technological individuals can use it.

### 2.4. Constraints
Google API only allows for 25,000 free map loads per day. Subby wishes to make this project as cost-efficient as possible so if the site exceeds the 25,000 map loads, the map will not be displayed. However, Subby creators do not expect the site to exceed 25,000 map loads per day during its first few years of release.  

### 2.5. Assumptions and Dependencies
Anyone can visit and search the rental database. However, to post a unit to sublet, users must first register with a valid university or college email. Additionally, individuals are expected to have access to a device with Wi-Fi and use a browser compatible with Google Maps.

# 3. Specific Requirements

---
### 3.1. External Interfaces
Unless otherwise stated, all inputs listed here will be stored in the application database as is appropriate for the model it represents.

* **User Management**
    * The user will be allowed to change their password by first providing their current password, then the new password, and lastly confirming the new password to ensure no typos have been made.
    * All changes to user account information will have to be confirmed through email to ensure account security.
    * The user will be able to enter an address of a property they are interested in for the application to more accurately determine which Sublet records may be relevant to them.
* **User ‘Favorites’ View**
    * All listings with a "matching" Favorite record (sublets that relate to the property a user has favourited) will be displayed to the user as well as links to view the full listing and delete the Favorite record.
    * Favorites which no longer have an existing Sublet record will no longer be displayed in a user's favourite list, with a notification that the listing is no longer available.
* **Sublet Listings**
    * Will list all sublets that fall within a default radius from the user (determined by IP geolocation or browser functionality) unless otherwise defined by the user.
    * Each listing will display its rating as a one-decimal float (the average of all ratings it has), as well as address, availability date, and distance.
    * The search functionality for this page is primarily based on listing address. However, filters may further exclude the returned records based on user selection. Filters will include sublet attributes such as the number of bedrooms, amenities, review ratings, and so on. Search queries are not stored, and are simply used to filter database results for a given area.
* **Sublet Wanted Listings**
    * User emails will not be displayed for those wanting to contact posters of ‘Sublet Wanted’ postings. The application will provide a simple form which will broker the first email between the two users, preventing malicious users from scraping email addresses from our system.
    * Similar filters and distance options will be available, as with the Sublet Listings page.
    * The same limits for maximum number of listings per area will be imposed for Sublets Wanted.
* **Listing Management**
    * A list of Sublets available or "Sublet Wanted" listings will appear on this page, with the address and various actions such as ‘edit’ or ‘delete’. A listing may be edited or created and may have photos, descriptions, or attributes added to it. A maximum of 8 photos will be allowed, and descriptions limited to short text (<500 characters)
* **Review Submission**
    * An integer rating range of 0 to 5 is allowed to be submitted along with a short text description. The description will be sanitized for safety of the database and application.
* **User Administration**
    * A list of all users, their email addresses, and number of postings will be shown to the administrator as well as links to ‘edit’.
    * An administrator will be able to edit a user’s email address as well as send a password reset link. The administrator will not be allowed to directly edit a user’s password.
    * The administrator will be able to select to ‘ban’ or ‘delete’ a user.

### 3.2. Functions
* The system will perform basic validation for all models. For example, a User cannot be created without an email address (which must also pass a simple email format validation), and a Sublet posting cannot be made without an availability date.
* The system will ensure that users are not creating more than their administrator-defined allowed postings for their geographic area.
* The system will allow administrators to ban users, removing their posts and account access but maintaining the user record to prevent later sign-ups from that address. Deleting a user performs the same task, but also removes the user record.
* The system will delete dependent records when a model is removed. For example, deleting a Sublet posting will delete Favorite records associated with it (i.e. tell the user that it was sold), and deleting a User would remove the Sublet postings created by them.
* Deleting a Sublet posting will also delete Favorite records associated with it. A notification may be displayed to the user to show that Favorite records have been removed.

### 3.3. Logical Database Requirements
* Several tables with many attributes will be required to maintain the data for this project. All tables will have a unique ID as the primary key for the table.
    * **Users table:** The Users table will require a distinct and unique email address, and salted/hashed passwords will also be stored. Two user types will be supported - regular clients who sign up from the web application and administrators who will have access to back-end functionality, which can be defined as a "tinyint" and treated as a boolean in the business logic of the application. Account status (such as bans or strikes against the account) will also be stored. Note that users can have zero-to-many relationships with the Sublets, Reviews, and Favorites tables.
    * **Sublets table:** Analogous to postings, the Sublets table will include address information (longitude/latitude as provided by Google’s Maps API), availability date, pricing, and so on. An individual sublet posting will be owned by a User through their distinct ID as a foreign key. As the ‘Wanted’ feature would cover many of the same attributes as a regular sublet, conditional logic or a ‘boolean’-treated field would determine whether a Sublet record is for a physically offered sublet, or a sublet-wanted ad.
    * **Reviews table:** Reviews will have foreign keys for both the owning User as well as the target user record it is for, preventing it from being invalidated when a posting is removed. It will also include a text field for the review content as well as an integer column for rating.
    * **Favorites table:** The Favorites table will include foreign keys on both Users and Sublets, allowing a User to look up several Sublet records that were of interest to them at some point. This is a simple join table, and no other information should be required.

Additional tables, such as those related to Auction/Bidding type listings may be added to support the product roadmap as features are implemented. Indexes will applied to all uniquely identifying fields such as IDs (as well as other fields of import, such as email addresses or location data) to ensure fast look-ups for individual and related records.

### 3.4. Portability
We must create a functional web page that is accessible on all devices, and because of the web-based nature, we must ensure compatibility with the largest browsers: Google Chrome, FireFox, Edge, and Safari. This means that there should be no issue with accessing the project through Windows, Mac OS X, or Linux. There will be a mobile-friendly version of the site.
* **Server-Side:** Use of a well-supported, platform agnostic language and framework such as Python/Django are recommended. Clients do not need to support these technologies as they will be accessing the application through their web browser.
* **Client-Side:** Clients will need to have a modern web browser with support for HTML5, CSS, and JavaScript.

### 3.5. Performance Requirements
This application is intended as a proof-of-concept and not for production-level scalability. As such, while common sense is to be used when implementing features, pre-optimization is not desired. For example, the application should be able to support 10 concurrent users at all times, or roughly 150 requests per minute (if each user were to make a request every 4 seconds).

### 3.6. Reliability
The application will not crash or produce unexpected errors when within the performance confinements outlined in section 3.5. Additionally, Subby will likely depend on a separate database server, so cases where this server becomes unavailable should be considered. As this is a proof of concept, load balancing, automated scaling, host health checks, or other reliability strategies are not required at this stage.

### 3.7. Security
There are a few main areas of concern for the security of this application:
* **User Passwords:** User passwords must be hashed with a unique salt in the event that a malicious actor were to obtain a dump of the database. Additionally, user invitations must use one-time tokens; password resets require confirmation; administrators are able to modify user account access should a user become compromised.
* **Administrators:** Administrator accounts have powerful capabilities, and should only be created manually via migration. No UI will exist allowing a user or administrator to change their permission level.
* **SQL Injection:** No queries are to be manually written that might allow for a user to supply a malicious payload.
* **Logging:** Basic logging should be done for future investigation of security issues (request information such as route, client IP, etc).

# 4.0. Revision History

---
## Version 1.1
* **Section 3**
    * Navdeep Sharma [1] [2018-05-27]
    * Sarah Younes [1, 1.1, 1.2] [2018-05-27]
    * Alex Kirsopp [2.1.2-2.1.4, 3.4-3.7] [2018-05-28]

* **Other**
    * Alex Kirsopp - Markdown

## Version 1.0
* **Section 1**
    * Sandra Sung [1.1-1.5] [2018-05-20]

* **Section 2**
    * Sandra Sung [2.1-2.5] [2018-05-20]
    * Jingchi Chen [2.1.4] [2018-05-20]
    * Xiaochao Luo[2.1] [2018-05-22]
    * Sizhao Lin [2.1.3] [2018-05-23]
    * Sarah Younes [2.1, 2.1.4] [2018-05-20]


* **Section 3**
    * Alex Kirsopp [3.1-3.3] [2018-05-20 - 2018-05-21]
    * Mackenzie Dang [3.4] [2018-05-22]

* **Other**
    * Mackenzie Dang - Markdown
    * Alex Kirsopp - Markdown
