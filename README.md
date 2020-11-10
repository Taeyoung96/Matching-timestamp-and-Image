# Matching TimeStamp.txt & Image List

## How to run
You should have your own Image folder and time stamp.txt.  
It should have same amounts.  
For example, when you have 1000 images, time stamp.txt has 1000 lines for each image.

```
> matching_TimeStampAndImage
  > Image folder
    > 00000000.jpg
      00000001.jpg 
      00000002.jpg ...
  > time stamp.txt
  > main.py
```

### Just run the code!
`python main.py --image_path [YOUR IMAGE FOLDER's ABSOLUTE PATH] --time_stamp [YOUR TIME STAMP.txt]`

You need to provide 2 argments(essential) & 3 argments(optional)
**Essential**
- --image_path : Your Image folder's absolute path
- --time_stamp : your time stamp.txt

**Optional**
- --ext : To extract Image extension (ex) .jpg, .png ...)
- --image_list_name : The name of txt file which is the list of images  
< Example of Image List >
> [Image Folder/ Name of Image.jpg]  
> Images/3275482532_6e7cbda005_k.jpg  
> Images/8426183211_4f8efa2e64.jpg  
> Images/379883550_ef848a76c7.jpg...
- --final_list_name : The name of txt file which is the final results  
<Example of Final List>
> [Time stamp Image Folder/ Name of Image.jpg]  
> 2086712044_71867a315e.txt Images/3275482532_6e7cbda005_k.jpg  
> 2802320_d477b071be.txt Images/8426183211_4f8efa2e64.jpg  
> 12191050105_2c6026bcda_k.txt Images/379883550_ef848a76c7.jpg...

## I just upload the Sample Image Folder and label.txt! :smile:
