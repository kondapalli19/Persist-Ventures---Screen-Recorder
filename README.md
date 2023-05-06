# Persist-Ventures - Screen Recorder
The program uses Python's Tkinter module to provide a graphical user interface with buttons that make it efficient. It records screen activity and uploads it to the cloud.

## _How it works ?_

- Copy the code
- Make sure all the modules are imported and installed
- Generate the access token of Cloud in which you want to upload ( in this program I used [Google drive Api] access token).
- Change the parents in Json with the directory where you want to upload the file.

## Features

- This tool can be used to record the screen of the device
- Using this tool one can also upload the recorded file to cloud.
- Buttons are provided with GUI to make things easier.






## Tech

It uses python modules :

- [cv2] - Pre-built CPU-only OpenCV packages for Python
- [Numpy] - The fundamental package for scientific computing with Python
- [pyautogui] - cross-platform GUI automation Python module for human beings
- [tkinter] - Python interface to the Tcl/Tk GUI toolkit.
- [json] - exposes an API familiar to users of the standard library marshal and pickle modules
- [requests] - Requests is a simple, yet elegant, HTTP library
- [threading] - higher-level threading interfaces on top of the lower level _thread module
- [PIL] - adds image processing capabilities to your Python interpreter







[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
    
   [PIL]: <https://pillow.readthedocs.io/en/stable/>
   [requests]: <https://pypi.org/project/requests/>
   [Numpy]: <https://numpy.org/>
   [cv2]: <https://pypi.org/project/opencv-python/>
   [json]: <https://docs.python.org/3/library/json.html>
   [tkinter]: <https://docs.python.org/3/library/tkinter.html>
   [pyautogui]: <https://pypi.org/project/PyAutoGUI/>
   [threading]: <https://docs.python.org/3/library/threading.html>
   [Google drive Api]: <https://cloud.google.com/appengine/docs/admin-api/trying-the-api>
