from datetime import datetime

# Define the start date of your experience
start_date = datetime(2022, 6, 1)
current_date = datetime.now()

# Calculate the experience in years
experience_in_years = (current_date - start_date).days / 365

# Round to one decimal place
experience_formatted = round(experience_in_years, 1)

# Path to the README.md file
readme_file = "README.md"

# Markers in the README where the experience should be inserted
start_marker = "<!--experience-start-->"
end_marker = "<!--experience-end-->"

# Open the README.md file and read its content
with open(readme_file, "r") as file:
    content = file.read()

# Check if the markers are present in the content
if start_marker in content and end_marker in content:
    # Split the content and insert the experience value between the markers
    updated_content = (
        content.split(start_marker)[0]
        + f"{start_marker} {experience_formatted} years {end_marker}"
        + content.split(end_marker)[1]
    )
else:
    print("Marker not found in README.md. Please add <!--experience-start--> and <!--experience-end--> to the file.")
    exit(1)

# Write the updated content back to the README.md file
with open(readme_file, "w") as file:
    file.write(updated_content)
