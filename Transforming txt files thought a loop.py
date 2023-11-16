import os
from datetime import datetime


citroen_directory = f'''c:\Directory'''

#############################################################################
## Create a loop trought all files into "citroen_directory" folder

for filename in os.listdir(citroen_directory):
    print(f'Directorio: {citroen_directory}')
    file_path = os.path.join(citroen_directory, filename)
# If the finded element is a file then process it
    if os.path.isfile(file_path):
        print(f'processing file {filename}')

        # Open each file and read the lines.
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extract the date from the first line.
        date_parts = lines[0].split('-')[:3]  # This will get the first three parts.
        date_str = '-'.join(date_parts)  # Join them back together with hyphens.
        print(f'Creation date: {date_str}')
        date_obj = datetime.strptime(date_str, "%d-%b-%y")

        # Format the datetime object into the desired string format
        formatted_date = date_obj.strftime("%d/%m/%Y")
        print(f'New date with nice format: {formatted_date}')

        # Modify the first line by removing the date.
        if lines:
            lines[0] = '-'.join(lines[0].split('-')[3:])

        # Create a new file name by adding the date string to the original name.
        new_file_name = f"WU283760 {date_str}.txt"
        new_file_path = os.path.join(citroen_directory,'temp', new_file_name)

        print(f'Old filepath: {file_path}')
        # Rename the file by moving it to the new path.
        os.rename(file_path, new_file_path)
        print(f"File has been renamed to {new_file_path}")

        # Add 'Fecha Informe' column to each line after the header.
        new_lines = [lines[0]]  # This will start with the header line.
        for line in lines[1:]:
            new_lines.append(f"{formatted_date};{line}")

        # Write the modified lines back to the new file.
        with open(new_file_path, 'w') as file:
            file.writelines(new_lines)

        print(f"Added 'Fecha Informe' column to {new_file_path}")

        # Write the modified lines with the new "Fecha Informe" column to the new file.
        with open(new_file_path, 'w') as file:
            # Add the new column name "Fecha Informe" to the header.
            header = lines[0].strip().split(';')
            header.insert(0, "Fecha Informe")
            file.write(';'.join(header) + '\n')

            # Insert the date_str into each line except the header.
            for line in lines[1:]:
                new_line = f"{formatted_date};" + line
                file.write(new_line)
        #####################################################################################33

