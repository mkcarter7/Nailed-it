# NAILED IT SERVER 🔨🛠️🪚🪛🔫🔧

## ABOUT
Nailed Its is a Django web application for managing DIY home projects with user specific data. Firebase is integrated for data management and authentication.

The user is able to manage their projects by room including materials and tools used.

## FEATURES
User Authentication is used for the user to be able to manage their own projects. The user can manage project, room, tool and materials relationships showing a many to one relationship. The user can manage project and tool relationships that are managed through a many-many relationship. The user has full CRUD (create, read, update, delete operations) on rooms, projects, materials and tools.

## INSTALLATION
Basic Django Set Up https://github.com/nashville-software-school/server-side-python-curriculum/blob/evening-cohorts/book-3-levelup/chapters/DRF_INSTALLS.md

## ERD
https://dbdiagram.io/d/NAILEDIT-67ac0bfd263d6cf9a0d71261

## WIREFRAME
https://www.figma.com/design/mdmMrUzpVJtkxMlXEYf8WU/Nalied-It?node-id=0-1&t=mtk2ykQgeDDCS9vL-1

## PROJECT BOARD
https://github.com/users/mkcarter7/projects/12

## VIDEO WALK THROUGH WITH LOOM
https://www.loom.com/share/2b5d95ea25c5481f9ac01942f315f423?sid=3f31fde2-1aa4-4b88-ba5d-a873997eafb1
https://www.loom.com/share/b0e9d66bfb5f4e84a6f7abbda9922e2e?sid=ab3ad0ee-9380-47a1-bbcc-81e5f49fd278

## SLIDE
https://docs.google.com/presentation/d/1GImrl0uY5I7ai90HgeRPLttrSVUHGeU_mOHvGrxaV9c/edit?usp=sharing

## API DOCUMENTS 
https://documenter.getpostman.com/view/33251382/2sAYdkGoc3

## TECH STACK
Django Python Postman Firebase Auth

## CONTRIBUTORS
https://github.com/mkcarter7

## MVP
Pass the Postman Student Certification
Use Postman to document your API (Your FE for this Capstone)
Deploy your Postman API Documentation
You are required to use the backend framework that you were taught for the backend of your application (e.g. ASP.NET, Django, etc...).
You must show your proficiency by following the Single Responsibility Principle and writing modular code, where each module has a single responsibility (e.g. displays a list of things, displays a single thing, manages application state, etc.).
Include a integration test for each https response / request method (expained more in the Baseline Requirements for API section)
You must have a README with the following:
Name of the Project
Overview of the project
Link to the deployed project
Link to your project board (yes...even though it is a part of the repo)
Description of the user
List of features
List of contributors and links to their GH profiles
Link to Loom video walkthrough of your deployed postman (no more than 1 minute long! Make it great)
Baseline Requirements for API
BE students must have at least 4 entities with full CRUD.
A join table is required but does NOT count as one of the 4 CRUD entities.
At least one many-to-many relationship is required.
Minimum: 5 tables (4 full CRUD entities + join table).
Maximum: 6 tables if you choose to create an additional entity instead of using a join table as one of your full CRUD entities.
Each of the 4 main CRUD entities must have integration tests covering GET, POST, PUT, and DELETE (minimum 16 tests total).
Write tests the same way you would manually test in Postman.
Send the correct request method (GET, POST, PUT, DELETE).
Include a request body if required (e.g., for POST and PUT).
Provide an entity ID if required (e.g., for GET by ID, PUT, DELETE).
Verify the response status code (200 for GET, 201 for POST, etc.).
Check that the response contains the expected keys and values.
Tests do not need to cover edge cases—just ensure the endpoints return the expected data.
Your tests should reflect the required behavior of your API and confirm that CRUD operations work properly.
Specify the data structure of what the endpoint will produce via Postman
Postman is the front-end for BE capstones. No React front-end.
Database of information
Needs at least 16 endpoints that returns/modifies different types of data
4 READS
4 CREATE
4 DELETES
4 UPDATES
