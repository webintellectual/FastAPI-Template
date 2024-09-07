import os
import json

def prompt_user(question, default="", comment=""):
    """Helper function to prompt the user and return their input"""
    result = input(f"{question} [{default}, {comment}]: ")
    return result.strip() or default

def main():
    # Load the context from cookiecutter.json
    context_file = "cookiecutter.json"
    with open(context_file, 'r') as f:
        context = json.load(f)

    # Example: Accessing and using existing context variables
    project_name = context.get("project_name", "My FastAPI Project flag")
    project_slug = context.get("project_slug", project_name.lower().replace(' ', '-').replace('_', '-'))

    print(f"Project Name: {project_name}")
    print(f"Project Slug: {project_slug}")

    # Additional prompting for database details
    use_database_url = context.get("use_database_url", "no").lower() == "yes"
    if not use_database_url:
        db_username = prompt_user("Database username", "user", "Enter your database username")
        db_password = prompt_user("Database password", "password", "Enter your database password")
        db_host = prompt_user("Database host", "localhost", "Enter your database host")
        db_port = prompt_user("Database port", "5432", "Enter your database port")
        db_name = prompt_user("Database name", project_slug, "Enter your database name")

        # Add these new variables to the context
        context.update({
            "db_username": db_username,
            "db_password": db_password,
            "db_host": db_host,
            "db_port": db_port,
            "db_name": db_name
        })

    # Save the updated context back to the cookiecutter.json file (optional)
    with open(context_file, 'w') as f:
        json.dump(context, f, indent=4)

if __name__ == "__main__":
    main()