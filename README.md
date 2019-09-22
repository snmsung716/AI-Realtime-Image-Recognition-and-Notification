# AI-Realtime-Image-Recognition-and-Notification

<img src="./git/0.png">

## 

### 1. Detection of Specific Object on Raspberry Pi
- Based on your model to detect a specific object in which you want to get the result, the database is sent to Firebase.

### 2. Notification on Your Smartphone or Device or Website
- If Firebase has the database on the specific location which has been selected, Firebase triggers Onesignal and then your smartphone, device or website have a notification of information.

### 3. Command by Your Smartphone or Device or Website
- The command which you send to Firebase is taken by the robot immediately.


<img src="./git/1.png" width="514" height="324">    <img src="./git/3.png" width="312" height="324">




## Requirements

- Kivy==1.11.1
- Kivy-Garden==0.1.4
- firebase==3.0.1
- requests==2.22.0
- Cython==0.29.13

I strongly recommend to use Anaconda environment. This repo may be able to be used in Python 3.7 environment.


## Installation of dependencies

```pip3 install Kivy```
```pip3 install Kivy-Garden```
```cd kivyIOS```
```python3 main.py```