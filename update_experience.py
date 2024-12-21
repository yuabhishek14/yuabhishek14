from datetime import datetime

start_date =  datetime(2022, 6, 1)
current_date = datetime.now()

experience_in_years = (current_date - start_date).days / 365

experience_formatted = round(experience_in_years, 1)

readme_file =  "Readme.md"

start_marker = "<!--experience-start-->"
end_marker = "<!--experience-end-->"

with open (readme_file, "r") as files:
    content =  file.read()


if start_marker in content and end_marker in content:

    updated_content =  content.split(start_marker)[0] + f"{start_marker} {experience_formatted} years {end_marker}" + content.split(end_marker)[1]
else:
    print("Marker not found in README.md. Please add <!--experience-start--> and <!--experience-end--> to the files.")
    exit(1)

with open(readme_file, "w") as file:
    file.write(updated_content)    
