# NannyNest Project

## Description

The NannyNest project is a Flask-based application that provides a platform for managing childcare services, including users, categories, posts, and comments.

## API Reference

| Endpoint                          | Method | Parameters   | Description                      |
|-------------------------  |--------|---------------------------------------------------------|
| `/api/users`                      | GET    |              | Get all users                    |
| `/api/users/<user_id>`            | GET    |              | Get user by ID                   |
| `/api/users`                      | POST   | JSON payload | Create a new user                |
| `/api/users/<user_id>`            | PUT    | JSON payload | Update user by ID                |
| `/api/users/<user_id>`            | DELETE |              | Delete user by                   |
| `/api/categories`                 | GET    |              | Get all categories               |
| `/api/categories/<category_id>`   | GET    |              | Get category by ID               |
| `/api/categories`                 | POST   | JSON payload | Create a new category            |
| `/api/categories/<category_id>`   | PUT    | JSON payload | Update category by ID            |
| `/api/categories/<category_id>`   | DELETE |              | Delete category by ID            |
| `/api/posts`                      | GET    |              | Get all posts                    |
| `/api/posts/<post_id>`            | GET    |              | Get post by ID                   |
| `/api/posts`                      | POST   | JSON payload | Create a new post                |
| `/api/posts/<post_id>`            | PUT    | JSON payload | Update post by ID                |
| `/api/posts/<post_id>`            | DELETE |              | Delete post by ID                |
| `/api/comments`                   | GET    |              | Get all comments                 |
| `/api/comments/<comment_id>`      | GET    |              | Get comment by ID                |
| `/api/comments`                   | POST   | JSON payload | Create a new comment             |
| `/api/comments/<comment_id>`      | PUT    | JSON payload | Update comment by ID             |
| `/api/comments/<comment_id>`      | DELETE |              | Delete comment by ID             |

## Retrospective

### How did the project's design evolve over time?

The project's design evolved from simple CRUD operations to a more sophisticated REST API with multiple models and relationships. Initially, we focused on user management and gradually expanded to include categories, posts, and comments.

### Did you choose to use an ORM or raw SQL? Why?

We chose to use SQLAlchemy as an ORM for database operations. This decision allowed us to work with Python objects directly, making database interactions more intuitive and less error-prone. SQLAlchemy also supports migrations and simplifies complex queries.

### What future improvements are in store, if any?

- Implement user authentication and authorization.
- Add more robust error handling and input validation.
- Improve performance by optimizing database queries and adding caching mechanisms.
- Enhance data visualization capabilities to provide insights into user behavior.