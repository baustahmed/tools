import os

def rename_files(folder_path):
    # Get list of files in the folder
    files = os.listdir(folder_path)
    
    # Sort the files alphabetically
    files.sort()
    
    # Counter for serial numbering
    counter = 1
    
    # Iterate through files and rename them
    for file_name in files:
        # Split the file name and extension
        base_name, extension = os.path.splitext(file_name)
        
        # Create new file name with serial number
        new_name = f"name-{counter}{extension}"
        
        # Construct full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment the counter
        counter += 1

# Replace 'folder_path' with the path to your folder containing files
folder_path = 'folder_path'
rename_files(folder_path)