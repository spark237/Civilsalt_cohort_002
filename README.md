 Reflection Questions:
Q1: What are models in Django, and how do they relate to the database?
  *Ans: Models are Python classes that define the structure of your database tables. Django uses them to generate the database schema and manage the data via ORM (Object-Relational Mapping).

Q2: What’s the difference between a view and a template?
  *Ans: A view handles logic and data fetching. A template handles how data is displayed (HTML). Views process data and pass it to templates.

Q3: What happens when you run makemigrations and migrate?
   *Ans:

makemigrations creates migration files based on changes in models.py.

migrate applies those migrations to your actual database, creating or updating tables.

Q4: How would you explain the flow of a request in a Django app?
   *Ans:

1. User makes a request via URL.

2. Django URL dispatcher matches it to a view.

3. View processes data, optionally queries models.

4. View passes data to template.

5. Template renders HTML.

6. Response sent back to browser.
