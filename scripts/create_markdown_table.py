'''
Purpose: The purpose of this script is to create a markdown tables from the outputs from notebooks.
Output: These markdown tables will be saved into the eda/outputs directory.
# Parameters:
# - df: the DataFrame that will be convereted into a markdown table.
# - table_name: the table name when it has been created and saved.
'''
import os

def create_markdown_table(df, table_name):
    # Set the absolute path to eda/outputs relative to the notebook
    output_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "outputs"))
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{table_name}.md")

    if os.path.exists(file_path):
        os.remove(file_path)

    # Initialize markdown table string
    markdown_table = ""

    # Header row
    header = "| " + " | ".join(df.columns) + " |"
    markdown_table += header + "\n"

    # Separator row
    separator = "| " + " | ".join(["---"] * len(df.columns)) + " |"
    markdown_table += separator + "\n"

    # Data rows
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(value) for value in row) + " |"
        markdown_table += row_str + "\n"

    # Save to file
    file_path = os.path.join(output_dir, f"{table_name}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_table)

    return f"Markdown table '{table_name}' created successfully in 'outputs/'."
