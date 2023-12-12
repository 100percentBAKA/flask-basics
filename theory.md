# Key Notes

## UserMixin

Import: ` from flask_login import UserMixin`

In Flask, `UserMixin` is a class provided by the Flask-Login extension. It is designed to simplify the implementation of a user model for user authentication. By inheriting from `UserMixin`, your user model gains default implementations of several properties and methods required by Flask-Login.

The key functionalities provided by `UserMixin` include:

- **User ID Management:**

  - `UserMixin` adds a `get_id()` method to your user model, allowing Flask-Login to retrieve a unique identifier for the current user.

- **Session Management:**

  - Methods like `is_authenticated`, `is_active`, and `is_anonymous` are provided by `UserMixin` to help manage user sessions and determine the state of a user.

- **Password Management:**
  - While `UserMixin` does not directly handle password hashing, it provides a `get_auth_token` method, which can be used in conjunction with Flask's `Secret` key to create a secure token for password reset or other purposes.

By using `UserMixin`, you can create a user model that integrates seamlessly with Flask-Login, making it easier to implement user authentication and manage user sessions in your Flask application.

## func

Import: `from sqlalchemy.sql import func`

The sqlalchemy.sql.func module provides a collection of SQL functions that can be used in SQLAlchemy queries. It includes a variety of database-agnostic SQL functions that can be employed when building queries or defining columns in SQLAlchemy models.

- **Aggregation Functions:**

  - Functions like func.sum, func.avg, func. count, etc., are used for performing aggregation operations on columns.

  ```python
  from sqlalchemy.sql import func

  average_value = session.query(func.avg(MyModel.column_name)).scalar()
  ```

- **Date and Time Functions:**

  - Functions like func.now, func.current_date, and func.extract are used for working with date and time values.

  ```python
  from sqlalchemy.sql import func

  current_datetime = session.query(func.now()).scalar()
  ```

- **Mathematical Functions:**

  - Functions like func.sqrt, func.exp, func.log, etc., are used for mathematical operations.

  ```python
      from sqlalchemy.sql import func

      sqrt_value = session.query(func.sqrt(MyModel.column_name)).scalar()
  ```

- **String Functions:**

  - Functions like func.concat, func.length, func.lower, etc., are used for string manipulation.

  ```python
      from sqlalchemy.sql import func

      concatenated_value = session.query(func.concat(MyModel.column1, MyModel.column2)).scalar()
  ```
