import os
import pandas as pd
import shutil

# Define paths
csv_file = r'D:\my projects\ML PROJECTS\antispeefing\archive (1)\real_30.csv'
folder_path = r'D:\my projects\ML PROJECTS\antispeefing\archive (1)\samples'
real_path = r'D:\my projects\ML PROJECTS\antispeefing\Images\Real'
fake_path = r'D:\my projects\ML PROJECTS\antispeefing\real-fake selfie detection.v2i.tensorflow\Fake'

# Read the CSV file
df = pd.read_csv(csv_file)

# Initialize a counter for renaming images
counter = 1

# Loop through each row in the dataframe
for index, row in df.iterrows():
    print(index)
    img_ = row['selfie_link']
    # label = row['class']
    img_path = os.path.join(folder_path, img_)

    # Uncomment the label-based path selection if needed
    # if label == 'face_spoof':
    #     des_path = fake_path
    # elif label == 'face_real':
    des_path = real_path
    # else:
    #     continue

    if os.path.exists(img_path):
        # Define new image name based on the counter
        new_img_name = f"{counter}.jpg"
        new_img_path = os.path.join(des_path, new_img_name)
        
        # Copy and rename the image
        shutil.copy(img_path, new_img_path)
        
        print(f"Image {img_} copied and renamed to {new_img_name}")
        
        # Increment the counter
        counter += 1

print('All images processed.')
