if __name__ == "__main__":
    import os
    import shutil
    import datetime
    
    file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xls', '.ppt', '.epub'],
    "Music": ['.mp3', '.wav', '.aac', '.flac'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov', '.wmv']
    }
    
    folder_path = input("Enter the path to the file: ")
    
    if not os.path.exists(folder_path):
        print("File does not exits")
    else:
        log_path = os.path.join(folder_path,"organizer_log.txt")
        
        with open(log_path,"a") as log_file:
            log_file.write(f"\n--- Run started at {datetime.datetime.now()} ---\n")
        
            for item in os.listdir(folder_path):
                if item.startswith("organizer_log"):
                    continue
                item_path = os.path.join(folder_path,item)
                if os.path.isfile(item_path):
                    _,ext = os.path.splitext(item_path)
                    ext = ext.lower()
                
                
                    category_found = False
                
                    for category,extensions in file_types.items():
                        if ext in extensions:
                            category_path = os.path.join(folder_path,category)
                            os.makedirs(category_path,exist_ok=True)
                            shutil.move(item_path,os.path.join(category_path,item))
                            print(f"Moved {item} -> {category}")
                            log_file.write(f"Moved {item} -> {category}\n")
                            category_found = True
                            break
                    if not category_found:
                        print(f"Skipped {item} -> No matching category found")
                        log_file.write(f"Skipped {item} -> No matching category found\n")
        
            log_file.write(f"\n--- Run ended at {datetime.datetime.now()} ---\n")
