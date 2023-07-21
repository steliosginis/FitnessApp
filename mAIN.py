#function that creat html page for each task 
#open main html page 
import os

def create_html_file(html_content, file_name):
    try:
        absolute_path = os.path.abspath(file_name)

        with open(file_name, "w") as file:
            file.write(html_content)

        print(f"HTML file '{file_name}' has been created successfully.")
        return absolute_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My HTML File</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a dynamically created HTML file using Python.</p>
    </body>
    </html>
    """

    file_name = "fitnessappmain.html"

    html_file_path = create_html_file(html_content, file_name)

    if html_file_path:
        print(f"Path of the created HTML file: {html_file_path}")
    else:
        print("HTML file creation failed.")