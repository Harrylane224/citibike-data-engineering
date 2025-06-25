'''
This script is designed to structure the EDA insights into a markdown format. This structured format will be retrieving
figures and tables from the EDA notebooks and saving them into a markdown file. The reason for this design is to build
a dynamic and reusable markdown file that can be easily updated with new insights from the EDA notebooks.
'''

import os
# Ensure the outputs directory exists
output_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "eda", "outputs"))
os.makedirs(output_dir, exist_ok=True)

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
    file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "eda", "eda_insights.md"))
    # Check to see if the file exists
    if not os.path.exists(file_path):
        print(f"Cannot locate the eda_insights.md file: {file_path}")
        pass
    # Check to see if output_dir exists
    if not os.path.exists(output_dir):
        print(f"Cannot locate the output directory: {output_dir}")
        pass

    # Clear the contents of the file if it exists
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")  # This clears the file

    # Write the header
    write_markdown_header(file_path, "Citibike - EDA Insights Report", 1)
    # Write the introduction section
    write_markdown_section(file_path, "Introduction", "This report summarises the insights gathered from the exploratory data analysis (EDA) conducted on the Citibike and newark airport weather dataset.")

    # Write the data overview section
    write_markdown_section(file_path, "Data Overview", "Provides an overview of each dataset, displaying of the column names, column descriptions, data types and three distinct values.")
    # Write the citibike data overview table
    write_markdown_header(file_path, "Citibike Data Overview", 3)
    write_markdown_table(file_path, os.path.join(output_dir, "citibike_shape.md"))
    # Write the newark airport weather data overview table
    write_markdown_header(file_path, "Newark Airport Weather Data Overview", 3)
    write_markdown_table(file_path, os.path.join(output_dir, "newark_airport_shape.md"))

    # Write the results from possible foreign key relationships section
    write_markdown_section(file_path, "Possible Foreign Key Relationships", "This section explores the potential foreign key relationships between the datasets, identifying how they can be linked to enhance the analysis.")
    # Write the foreign key relationships table
    write_markdown_header(file_path, "Foreign Key Relationships", 3)
    write_markdown_table(file_path, os.path.join(output_dir, "possible_fk_relationships.md"))

    # Write the results from the duplicate detection section
    write_markdown_section(file_path, "Duplicate Detection", "This section identifies and discusses the presence of duplicate records in the datasets, which can impact the integrity of the analysis.")
    # Write the duplicate detection table
    write_markdown_header(file_path, "Duplicate Detection Results", 3)
    write_markdown_table(file_path, os.path.join(output_dir, "duplicate_counts_table.md"))

    # Write the results from the missing data section
    write_markdown_section(file_path, "Missing Data", "This section examines the presence of missing values in the datasets, which can affect the quality of the analysis and the insights derived from it.")
    # Write the missing values table
    write_markdown_header(file_path, "Missing Data Summary", 3)
    write_markdown_table(file_path, os.path.join(output_dir, "missing_data_summary.md"))


write_eda_insights_markdown()
