# Simple Blog CMS

This project is a simple command-line based Content Management System (CMS) for a blog. It's a great example to understand the basics of file handling, JSON manipulation, and user authentication in Python.

## How it Works

The application has two main user roles: **Admin** and **Guest**.

  * **Admin:** The admin can log in and has the ability to create new blog posts and view a list of all existing posts.
  * **Guest:** A guest can view a welcome message.

The application uses JSON files to store data:

  * `posts.json`: Stores all the blog posts.
  * `user_list.json`: Stores the user credentials.

## Running the Project

1.  Make sure you have Python installed on your system.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you have saved the project files.
4.  Run the `home.py` file using the following command:

<!-- end list -->

```bash
python home.py
```

This will start the application and prompt you to log in as a user or continue as a guest.

## Code Files

Here is a breakdown of the important files in this project:

  * **`home.py`**: This is the main file to run the application. It handles the initial user interaction, asking them to either log in or continue as a guest.
  * **`admin.py`**: This file contains the logic for the admin user. It allows the admin to create new posts and see a list of all posts.
  * **`guest.py`**: A simple module that displays a welcome message for guest users.
  * **`posts.json`**: This file acts as a database to store the blog posts.
  * **`user_list.json`**: This file stores the usernames and passwords for authentication.

## Things to Explore

  * **Enhance Guest functionality:** Can you modify the `guest.py` and `home.py` files to allow guests to also view the blog posts?
  * **Error Handling:** What happens if the `posts.json` or `user_list.json` files are not found? Add some error handling to the code to gracefully handle such situations.
  * **More Admin Features:** What other features would be useful for an admin? Maybe an option to delete or edit a post? Try implementing it in `admin.py`.
  * **Password Security:** The passwords in `user_list.json` are stored in plain text. This is not secure. Research how you can store passwords more securely (e.g., using hashing).
