# JPG Extraction Tool

---

### A Python tool for extracting processed JPG images from the diabetic retinopathy screening service for data requests

```
  Last Updated : 29/06/2022
  Team   :  R&D INSIGHT 
  Owner  :  David Gee
  Dev    :  Samuel Bodza
```

---

### Documentation
*For full documentation see the **Documentation** folder*

TLDR:
- Python tool that locates images, given unique file name.
- Able to copy images into folder
- Able to return a statistically calculated sample to validate ML
- Able to parse EXIF data

---

### Instructions for Use

**Usage**
```
the tool will automatically run at midnight every day

1. Copy valid csv(s) into input folder
   1. ex. ../input/<csv_name>.csv
2. Pick data up following morning

if something has not worked:
    - Check to see in the CSV is still in the input, will move to output when finished
    - Check the logs to see if there was any errors

```

**CSV naming scheme**
```
by default
    this tool returns:
        - csv of path names
        - copy of the images
        - parsed exif data
        - random samaple of the images 
        
the CSV can be any valid filename and by default will pull a sample 
and parse exif data but if the CSV name contains the terms shown 
below it will change the functionality of the tool.

GETNAMES
    this returns:
        - csv of path names
        
GETIMAGES
    this returns:
        - csv of path names
        - copy of the images
        
NOSAMPLE
    this returns:
        - csv of path names
        - copy of the images
        - parsed exif data
       
NOEXIF
    this returns:
        - csv of path names
        - copy of the images
        - a random sample of the images
       
```
**CSV formatting**
```
CSVs should have:
	- no headers
	- one column
	- filenames must all be in the same form, in one of the below formats:
		- filestorage://[SERVER]/[PATH]/Img_cee0d57f-b66c-4913-beda-25705b710fee?Full=[EXT];Thumbnail=[EXT]
		- Img_cee0d57f-b66c-4913-beda-25705b710fee_Full.jpg
		- Img_cee0d57f-b66c-4913-beda-25705b710fee
		- cee0d57f-b66c-4913-beda-25705b710fee
```

---

### Example

for an example of an input of *test.csv*

this will create a directory called test__[date] in output

in the test__[date] directory there will be 3 more folders:
```
./output/test_<date>/
    |- csv/
        |- test.csv
        |- paths.csv 
    |- images/
        |- Img1.jpg
        |- Img2.jpg
        |- ...   
    |- logs/
        |- test.logs
        |- exif/
            |- exif_out.txt
            |- exif_out2.txt
            |- exif_to_check.txt
        |- failed_exif/
            |- Img11.jpg
            |- Img19.jpg
            |- ...
        |- sample_internal/
            |- Img17.jpg
            |- Img23.jpg
            |- ...
        |- sample_external/
            |- Img17.jpg
            |- Img23.jpg
            |- ...

```
---

### Future Work
- [ ] add JPG DICOM functionality
- [ ] add Heidelberg DICOM functionality
- [ ] add TOPCON DICOM functionality

---





