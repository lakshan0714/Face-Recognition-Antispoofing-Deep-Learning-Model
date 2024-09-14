import os
import pandas as pd
import shutil

csv_file=r'D:\my projects\ML PROJECTS\antispeefing\real-fake selfie detection.v2i.tensorflow\_annotations.csv'
folder_path=r'D:\my projects\ML PROJECTS\antispeefing\real-fake selfie detection.v2i.tensorflow\train'
real_path=r'D:\my projects\ML PROJECTS\antispeefing\Images\Real'
fake_path=r'D:\my projects\ML PROJECTS\antispeefing\real-fake selfie detection.v2i.tensorflow\Fake'


df=pd.read_csv(csv_file)



#print(df)

for index,row in df.iterrows():
    print(index)
    img_= row['filename']
    label=row['class']
    img_path=os.path.join(folder_path,img_)

    if label=='face_spoof':
        des_path=fake_path
    
    elif label=='face_real':
        des_path=real_path
    
    else:
        continue


    if(os.path.exists(img_path)):
       shutil.copy(img_path,des_path)
       print('done')

    


   
