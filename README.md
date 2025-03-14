# ExportHunter
This project allows users to fetch exported activities from an APK and initiate am start commands with provided intent values. Additionally, it can generate code for building an APK that triggers the exported activity with specified intent and bundle values. 

Ideal for testing and automating interactions with exported components.

<img width="534" alt="image" src="https://github.com/user-attachments/assets/6d060c8e-7e2a-4a8e-bd34-c89fd343320d" />

# Features
- Extract exported Activities (includes activities that requires permission)
- View Java Code of selected Activity with Highlighted code that might be using Extras from intent
- Configure Extras to pass includig Bundles
- Launch Over ADB which uses `am start`
- Generate APK code for configured Extras + Bundles
- Build + Deploy + Launch Generated APK

# Working
- Demo.apk provided to get used to the Tool
- --es/--ez/--ei etc. should be used for the type of the Extras
   
<img width="1131" alt="1" src="https://github.com/user-attachments/assets/242134c2-5432-4389-942a-204cf63e5a81" />

# Dependencies

To have the tool working please install the following tools.
- scrcpy
- apktool
- Java -> openJdk@21 or later
- Android SDK 34 or later (Preferably have Android Studio installed) 


All the tools should be in PATH

Compatible with OS having /tmp folder.



