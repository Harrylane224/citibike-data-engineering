'''
This script is designed to structure the EDA insights into a markdown format. This structured format will be retrieving
figures and tables from the EDA notebooks and saving them into a markdown file. The reason for this design is to build
a dynamic and reusable markdown file that can be easily updated with new insights from the EDA notebooks.
'''

import os
# Ensure the outputs directory exists
os.makedirs("outputs", exist_ok=True)

# Function to write a markdown header
def write_markdown_header(file_path, header, header_level):
    with open(file_path, "a") as file:
        prefix = "#" * header_level
        file.write(f"{prefix} {header}\n\n")

# Function to write a markdown section
def write_markdown_section(file_path, section_title, content):
    with open(file_path, "a") as file:
        file.write(f"## {section_title}\n")
        file.write(content + "\n\n")

# Function to write a markdown table
def write_markdown_table(file_path,table_name):
    # Read the table content from the specified file
    with open(table_name, "r") as table_file:
        table_content = table_file.read()
    # Write the table content to the markdown file
    with open(file_path, "a") as summary_file:
        summary_file.write(table_content + "\n\n")

# Write the markdown file for eda_insights.md
def write_eda_insights_markdown():
    file_path = os.path.join("..", "eda", "eda_insights.md")
    # Check to see if the file exists
    if not os.path.exists(file_path):
        print(f"Cannot locate the eda_insights.md file: {file_path}")
        return

    output_dir = os.path.join("..", "eda", "notebooks", "outputs")
    # Check to see if output_dir exists
    if not os.path.exists(output_dir):
        print(f"Cannot locate the output directory: {output_dir}")
        return

    # Clear the contents of the file if it exists
    with open("outputs/eda_insights.md", "w", encoding="utf-8") as f:
        f.write("")  # This clears the file


write_eda_insights_markdown()
