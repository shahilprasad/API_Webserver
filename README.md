# Venue Queues API

### Table of Contents:
- [Installation Instructions](#installation-instructions)
- [R1 - Identification of the problem you are trying to solve by building this particular app.](#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)
- [R2 - Why is it a problem that needs solving?](#r2---why-is-it-a-problem-that-needs-solving)
- [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
- [R4 - Identify and discuss the key functionalities and benefits of an ORM](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)
- [R5 - Document all endpoints for your API](#r5---document-all-endpoints-for-your-api)
- [R6 - An ERD for your app](#r6---an-erd-for-your-app)
- [R7 - Detail any third party services that your app will use](#r7---detail-any-third-party-services-that-your-app-will-use)
- [R8 - Describe your projects models in terms of the relationships they have with each other](#r8---describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
- [R9 - Discuss the database relations to be implemented in your application](#r9---discuss-the-database-relations-to-be-implemented-in-your-application)
- [R10 - Describe the way tasks are allocated and tracked in your project](#r10---describe-the-way-tasks-are-allocated-and-tracked-in-your-project)
- [References](#references)

### Installation Instructions

Prerequisites:
- Python 3
- PostgreSQL

Clone or download the repository from Github and navigate the the **/src** directory.

#### Mac instructions

Open the terminal and run:

```psql postgres```

Create the databaseL

```CREATE DATABASE venue_queues;```

Connect to the database:

```\c venue_queues;```

Create a user, set a password, and grant privileges:

```CREATE USER admin_api WITH PASSWORD 'admin123';```

```GRANT ALL PRIVILEGES ON DATABASE venue_queues TO admin_api;```

```GRANT ALL ON SCHEMA public to admin_api;```

Open another terminal tab and run:

```python3 -m venv .venv```

```source .venv/bin/activate```

Install dependencies:

```pip install -r requirements.txt```

Rename the .envexample file to .env and set the database url and secret key:

```DATABASE_URL="postgresql+psycopg2://admin_api:admin123@127.0.0.1:5432/venue_queues"```

```SECRET_KEY="Save yourself time"```

Create, drop and seed the database tables:

```flask db create```
    
```flask db seed```

Run the application:

```flask run```

Use an app such as Insomnia or Hoppscotch to run the application via the URL pefix 127.0.0.1:5000/ or localhost:5000/

___

### R1 - Identification of the problem you are trying to solve by building this particular app.

Have you ever booked an Uber to a venue for a night out only to get there and see a long spannning queue that doesn't seem to be moving? Then you realise that you don't want to spend your time waiting in the qeueue as you need to get home and continue working on building application(s). The next best venue another Uber ride away, but you don't know if the queue is any better there. You decide to go there anyway, only to find that the queue is even longer than the previous venue. You end up calling it a night after wastiing your time and money. On the way home, you think to yourself, "If only there was a way to know how long the queue was before I got there, I could have saved myself a lot of time and effort."

This application seeks to solve the problem of lack of transparency and real-time information about nightclub, bar, and venue queues. Currently, individuals often have to physically visit a venue to assess the queue length, wasting time, money, and effort, especially during peak times. Additionally, information about upcoming events and venue details may be scattered across various sources, making it difficult to plan a night out efficiently. This application will provide a centralised source of information about venues, including queue length, upcoming events, and venue details, allowing users to plan their night out more efficiently.

___

### R2 - Why is it a problem that needs solving?

#### This lack of transparency and information presents several significant problems:

- Wasted Resrouces: Individuals spend valuable time waiting in lines, sometimes for longer than anticipated, without knowing the actual queue length. This leads to frustration, waster resource, and an overall poor experience.

- Difficulty in Planning: Uncertain queue lengths make it difficult to plan outings effectively. Individuals may arrive at a venue too early or miss out on popular events due to inaccurate information.

- Missed Opportunities: Lack of awareness of upcoming events and venue details can lead to missed opportunities for individuals to enjoy specific events or discover new venues.

- Inefficient Venue Management: Venues lack real-time data on their queue lengths, hindering their ability to effectively manage crowd flow and optimise their operations.

Therefore, the problem of lack of transparency and information about nightclub and venue queues is a significant issue that negatively impacts both users and businesses. This application provides a valuable solution by offering real-time data and facilitating informed decision-making, leading to a more enjoyable and efficient nightlife experience for all.
___

### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

#### PostgreSQL's advantages:

- PostgreSQL has extensive capability that goes beyond simple CRUD operations. The efficiency and responsiveness of the API are improved by materialised views, triggers, and stored procedures, which allow for sophisticated data manipulation and the automation of processes like queue updates.

- ACID Compliance: PostgreSQL uses ACID transactions to ensure data consistency, which is essential for maintaining precise queue lengths during real-time changes. In addition to avoiding possible problems like missing or damaged queue information, this guarantees dependable data retrieval.

- Open-source: Because PostgreSQL is open-source, there are no licencing fees and a vibrant community for development and support is encouraged. This results in reduced costs for development and upkeep while enjoying continuous contributions and advancements from the community.

- Performance: PostgreSQL performs exceptionally well for sophisticated queries and concurrent operations, which is essential for managing the expected load of the API even though it isn't the fastest database in the world by any means.


#### PostgreSQL disadvantages:


- Learning curve: Compared to more straightforward databases like MySQL, PostgreSQL has a steeper learning curve due to its comprehensive feature set. Nonetheless, this obstacle can be surmounted with the aid of the wealth of documentation and community support tools.

- Potential complexity: Compared to simpler solutions, managing and optimizingPostgreSQL for complex workloads may require more experience. But this difficulty is frequently outweighed by the advantages in terms of data integrity, performance, and scalability.


#### Comparisons with other databases:

- MongoDB: Although MongoDB's adaptable document-oriented structure has benefits, its weak ACID guarantees may cause problems with data consistency when updating queues. For maintaining data integrity in a real-time queue environment, PostgreSQL is therefore a more secure choice.

- Cloud-based databases: Pay-per-use cloud alternatives, such as Google Cloud SQL and Amazon Aurora, can get pricey, particularly for high-traffic applications, despite providing straightforward scalability and management. Because PostgreSQL is open-source, it offers a flexible and affordable solution with control over data management.

___

### R4 - Identify and discuss the key functionalities and benefits of an ORM

An ORM, or Object-Relational Mapper, connects your application's object-oriented programming paradigm to your database's relational structure. It translates object models and relationships into SQL queries and vice versa, hiding database interaction complexity from code

Key Functionalities of ORMs:
ORMs automatically construct and execute SQL queries based on object manipulations and relationships. This reduces development time and errors by eliminating manual query writing.
ORMs seamlessly manage object relationships, foreign key constraints, and data consistency across tables. This streamlines data handling and minimises inconsistencies in complex data models like the Venue Queue API.
Lazy loading: ORMs optimise performance and memory by delaying data loading. This is useful for applications with enormous datasets, like a venue queue with many users and events.
Data validation and serialisation: Some ORMs have built-in data validation and serialisation, simplifying data management and decreasing manual implementation.

Benefits of using an ORM:
Developer productivity: Objects instead of SQL speed up development and reduce bugs. Project timeframes and resource allocation depend on this.
Cleaner code: Separating data logic and database interface improves code readability and maintainability. This streamlines code reviews, cooperation, and maintenance.
Less boilerplate code: Automatic query generation removes repeating SQL statements, reducing codebase size and improving clarity.
Increased database portability: Many ORMs include database-agnostic functions, allowing your code to adapt to multiple databases with little changes. This gives your app flexibility and future-proofing.

Why SQLAlchemy?
SQLAlchemy was my selected ORM for my Venue Queue API due to its extensive feature set and fit for the project such as versatility and future-proofing. It boasts a  large and active community, and is a mature and extensively used ORM. This means detailed documentation, vast tutorials, and easy help. SQLAlchemy's relationship management and automatic query generation enhance my Venue Queue API project. These improvements streamline queue updates, venue-event linkages, and database interaction, improving API performance.

___

### R5 - Document all endpoints for your API

### Users Endpoints

### 1. /users/register 

- **HTTP Request Verb:** POST
- **Required data:** Username, email, password.
- **Expected response:** '201 CREATED' - Returns email, username, and id of the newly created user.
- **Authentication:** N/A
- **Description:** Allows a new user to register.


![POST / Register](./docs/endpoints/POST-user-register.png)

### 2. /users/login

- **HTTP Request Verb:** POST
- **Required data:** username, password
- **Expected response:** '200 OK' - Returns JWT token, email, and username.
- **Authentication:** Username and email.
- **Description:** Allows a user to login with their email and password if they are already registered. Returns a JWT token that is used to authenticate the user for subsequent requests.

![POST / Login](./docs/endpoints/POST-user-login.png)

### 3. /users

- **HTTP Request Verb:** GET
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns a list of all users with their data except for their password, along with some venue data.
- **Authentication:** Valid JWT token of an admin.
- **Description:** Allows admin to get a list of all users who are currently registered. If a user has created a venue, the venue id and name will be nested within their user data.

![GET / Get all users](./docs/endpoints/GET-all-users.png)

### 4. /users/&lt;int:user_id&gt;

- **HTTP Request Verb:** DELETE
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns empty JSON response.
- **Authentication:** Valid JWT token of an admin, or the user whose id is specified in the URL.
- **Description:** Allows admin to delete a user, or a user to delete their own account.

![DELETE / Delete a user](./docs/endpoints/DELETE-user.png)

### Venues Endpoints

### 5. /venues

- **HTTP Request Verb:** GET
- **Required data:** N/A
- **Expected response:** '200 OK' - Retuns a list of all venues, with events and queue data nested within each venue.
- **Authentication:** N/A
- **Description:** Anyone with access to the API will be able to get a list of all venues, along with their events and queue data.

![GET / Get all venues](./docs/endpoints/GET-all-venues.png)

### 6. /venues/&lt;int:venue_id&gt;

- **HTTP Request Verb:** GET
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns a venue with its events and queue data nested within it.
- **Authentication:** N/A
- **Description:** Anyone with access to the API will be able to get a venue, along with its events and queue data.

![GET / Get a venue](./docs/endpoints/GET-one-venue.png)

### 7. /venues

- **HTTP Request Verb:** POST
- **Required data:** Name, address, suburb and postcode.
- **Expected response:** '201 CREATED' - Returns the newly created venue, along with user id and username.
- **Authentication:** Valid JWT token.
- **Description:** Allows a user or admin to create a new venue.

![POST / Create a venue](./docs/endpoints/POST-new-venue.png)

### 8. /venues/&lt;int:venue_id&gt;

- **HTTP Request Verb:** PUT
- **Required data:** Atleast one of the 4 fields: name, address, suburb, postcode.
- **Expected response:** '200 OK' - Returns the updated venue, with queue and event data.
- **Authentication:** Valid JWT token of user who created the venue or admin.
- **Description:** Allows an admin or the user who created the venue to update venue details.

![PUT / Update a venue](./docs/endpoints/PUT-update-venue.png)

### 9. /venues/&lt;int:venue_id&gt;

- **HTTP Request Verb:** DELETE
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns empty JSON response.
- **Authentication:** Valid JWT token of user who created the venue or admin.
- **Description:** Allows an admin or the user who created the venue to delete a venue.

![DELETE / Delete a venue](./docs/endpoints/DELETE-venue.png)

### Events Endpoints

### 10. /venues/&lt;int:venue_id&gt;/events

- **HTTP Request Verb:** GET
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns a list of all events for a venue.
- **Authentication:** N/A
- **Description:** Allows anyone to get a list of all events for a venue, and also nests venue and queue data within each event.

![GET / Get all events](./docs/endpoints/GET-all-events.png)

### 11. /venues/&lt;int:venue_id&gt;/events

- **HTTP Request Verb:** POST
- **Required data:** Event name, description, date, start time and end time.
- **Expected response:** '201 Created' - Returns the created event along with its id, along with the nested user id and username.
- **Authentication:** Valid JWT token.
- **Description:** Allows a user with a valid JWT token to create a new event for a venue.

![POST / Create new event](./docs/endpoints/POST-new-event.png)

### 12. /venues/&lt;int:venue_id&gt;/events/&lt;int:event_id&gt;

- **HTTP Request Verb:** PUT
- **Required data:** Atleast one of the 5 fields: name, description, date, start time, end time
- **Expected response:** '200 OK' - Returns the updated event, along with the nested user id and username.
- **Authentication:** Valid JWT token of user who created the event or admin.
- **Description:** Allows a user who created the event or admin to update event details.

![PUT / Update an event](./docs/endpoints/PUT-event-details.png)

### 13. /venues/&lt;int:venue_id&gt;/events/&lt;int:event_id&gt;

- **HTTP Request Verb:** DELETE
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns empty JSON response.
- **Authentication:** Valid JWT token of user who created the event or admin.
- **Description:** Allows a user who created the event or admin to delete an event.

![DELETE / Delete an event](./docs/endpoints/DELETE-event.png)

### Queues Endpoints

### 14. /venues/&lt;int:venue_id&gt;/queue

- **HTTP Request Verb:** GET
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns queue info for a venue, along with nested venue and queue data.
- **Authentication:** N/A
- **Description:** Allows any user to get queue info for a venue, along with nested venue and queue data.

![GET / Get queue info](./docs/endpoints/GET-queue-info.png)

### 15. /venues/&lt;int:venue_id&gt;/queue

- **HTTP Request Verb:** POST
- **Required data:** Wait time.
- **Expected response:** '201 CREATED' - Returns the created queue info, along with nested venue and event data.
- **Authentication:** Valid JWT token.
- **Description:** Allow a user with a valid JWT token to create queue info for a venue.

![POST / Update queue info](./docs/endpoints/POST-queue-info.png)

### 16. /venues/&lt;int:venue_id&gt;/queue/&lt;int:queue_id&gt;

- **HTTP Request Verb:** DELETE
- **Required data:** N/A
- **Expected response:** '200 OK' - Returns empty JSON response.
- **Authentication:** Valid JWT token of user who created the queue info or admin.
- **Description:** Allows a user who created the queue info or admin to delete queue info.

![DELETE / Delete queue info](./docs/endpoints/DELETE-queue-info.png)

___

### R6 - An ERD for your app

This is the final version of the Entity Relationship Diagram for my application.

![ERD](./docs/ERD.png)
___

### R7 - Detail any third party services that your app will use

### Flask
This application was built using Flask, a web application framework that simplifies RESTful web service development. Web server queries and answers are handled by the Werkzeug WSGI toolkit and Jinja2 template engine.

Extensions in Flask let developers construct scalable apps rapidly. This micro framework helps developers without worrying about low-level details. Setup is simple, making it ideal for small to medium-sized web applications. Flask has several libraries to integrate and improve its functionality.

### SQLAlchemy

The Flask web application framework can integrate with the SQLAlchemy ORM library using Flask-SQLAlchemy. Popular Python database package SQLAlchemy provides a high-level interface for relational databases. It lets developers use Python objects instead of SQL statements to interface with databases in a "pythonic" approach.

### Marshmallow

Python object serialisation and deserialisation library marshmallow. Complex data structures like Python objects can be translated to and from JSON using marshmallow. It helps define schema and includes field validation, default values, and more.

Marshmallow works with Flask-Marshmallow, a Flask extension. Like Flask-SQLAlchemy, it simplifies Marshmallow library use in Flask with enhanced syntax and support. A few files utilise the marshmallow-sqlalchemy library to integrate Marshmallow with SQLALchemy.

### Psycopg2

Python library Psycopg2 works with PostgreSQL. Python developers may read and write PostgreSQL data with Psycopg2. Postgres is an open-source relational database management system.

### Flask-JWT-Extended

Flask-JWT-Extended is a Flask extension that adds JSON Web Token (JWT) support to Flask. It allows developers to create endpoints that require a valid JWT token to access. It also provides a mechanism for refreshing tokens. 

### Bcrypt

Bcrypt is a password hashing library for Python. It uses the Blowfish cipher to hash passwords. Bcrypt is a popular password hashing algorithm because it is slow and difficult to crack. It is also a one-way hash, which means it cannot be reversed to obtain the original password. Bcrypt is used to hash passwords before storing them in the database.

___

### R8 - Describe your projects models in terms of the relationships they have with each other

My project contains four models which are Users, Venues, Events, and Queues. Their data fields and relationship amongst themselves have been defined with SQLAlchemy

### User Model
user.py

The user model represents a registered user of the Venue Queue API. It has a one to many relationship with the Venue model, and a one to many relationship with the Event model. This means that a user can create many venues and events, but a venue or event can only be created by one user. The user_id column is a foreign key in the Venue and Event models that references the id column in the User model.

```python
class User(db.Model):
    __tablename__= "users"
   
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    venues = db.relationship('Venue', back_populates='user')
    events = db.relationship('Event', back_populates='user')
```

### Venues Model
venue.py

The venue model represents a venue that has been created by a user. It has a one to one relationship with the Queue model, and a one to many relationship with the Event model. This means that a venue can only have one queue abd a queue can only be associated with one venue. A venue can have many events, but an event can only be associated with one venue. It also has a many to one relationship with the user model .The user_id column is a foreign key in the Venue model that references the id column in the User model. The venue_id column is a foreign key in the Queue and Event models that references the id column in the Venue model.

```python
class Venue(db.Model):
    __tablename__= "venues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode= db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='venues')

    queue = db.relationship('Queue', back_populates='venue')
    event = db.relationship('Event', back_populates='venue')
```

### Events Model
event.py

The event model represents an event that has been created by a user and links to a venye. It has a many to one relationship with the Venue model. This means that an event can only be associated with one venue, but a venue can have many events. It also has a many to one relationship with the user model. The user_id column is a foreign key in the Event model that references the id column in the User model. The venue_id column is a foreign key in the Event model that references the id column in the Venue model.

```python
class Event(db.Model):
    __tablename__= "events"
   
    id = db.Column(db.Integer,primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='events')
```

### Queue Model
queue.py

The queue model represents the queue information for a venue. It has a one to one relationship with the Venue model. This means that a queue can only be associated with one venue, but a venue can only have one queue. The venue_id column is a foreign key in the Queue model that references the id column in the Venue model.

```python
class Queue(db.Model):
    __tablename__= "queues"

    id = db.Column(db.Integer,primary_key=True)
    wait_time = db.Column(db.String, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    comment = db.Column(db.String())

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue', back_populates='queue')
```
___

### R9 - Discuss the database relations to be implemented in your application

### Users and Venues

One-to-Many Relationship: A user can create multiple venues, indicating a one-to-many relationship between the User and Venue models. This relationship is represented by the venues field in the User model, which is linked to the user_id foreign key in the Venue model.

### Users and Events
One-to-Many Relationship: Similarly, a user can create multiple events. There's a one-to-many relationship between the User and Event models. The events field in the User model is connected to the user_id in the Event model through a foreign key.

### Venues and Events
One-to-Many Relationship: A venue can host multiple events, but an event is associated with only one venue. The event field in the Venue model establishes a one-to-many relationship with the Event model through the venue_id foreign key.

### Venues and Queues
One-to-One Relationship: Each venue has one queue information associated with it, which is represented by a one-to-one relationship between the Venue and Queue models. The queue field in the Venue model references the Queue model through the venue_id foreign key.

___

### R10 - Describe the way tasks are allocated and tracked in your project

Tasks in my project were allocated and tracked using Trello. Trello is a web-based Kanban-style list-making application. It is a visual collaboration tool that allowed me to create boards, lists, and cards to organise and prioritise tasks in my project. I updated my Trelo board almost every day since beginning the project, and it was a great way to keep track of my progress and stay on top of my tasks.

![Trello](./docs/trello.png)


### References

- Abba, IV 2022, What is an ORM – The Meaning of Object Relational Mapping Database Tools, freeCodeCamp.org.
- Altexsoft 2023, Database Management Systems (DBMS) Comparison: MySQL, Postgr, AltexSoft.
- Countryman, M n.d., Flask-Bcrypt — Flask-Bcrypt 1.0.1 documentation, flask-bcrypt.readthedocs.io.
- JWT n.d., JWT.IO - JSON Web Tokens Introduction, jwt.io.
- marshmallow n.d., marshmallow: simplified object serialization — marshmallow 3.17.1 documentation, marshmallow.readthedocs.io.
- PostgreSQL 2021, PostgreSQL 13.2 Documentation, PostgreSQL Documentation.
- SQLAlchemy 2023, SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation, docs.sqlalchemy.org.