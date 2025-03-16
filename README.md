# ExportHunter
This project allows users to fetch exported activities from an APK and initiate am start commands with provided intent values. Additionally, it can generate code for building an APK that triggers the exported activity with specified intent and bundle values. 

Ideal for testing and automating interactions with exported components.

# Working
1. **Browse an APK** – A list of exported activities will be displayed.  
2. **Select an Activity** – Double-click on an activity to load its corresponding Java code. Intent-related methods will be highlighted.  
3. **Add Extras & Bundles** (if needed):  
   - Use appropriate data types such as `--es`, `--ez`, `--ei`, etc.  
   - Click the **Configure** button in the bundle entry to add extras within the bundle.  
4. **Launch via ADB** – Execute the selected activity on a connected device.  
5. **Generate & Launch APK Code** (for working with bundles):  
   - The tool will generate the required APK code.  
   - The APK will automatically initiate the call to the exported activity upon launch.  
6. **Demo APK Included** – A sample `Demo.apk` is provided to help users familiarize themselves with the tool.  


<img width="1131" alt="1" src="https://github.com/user-attachments/assets/242134c2-5432-4389-942a-204cf63e5a81" />

# Things to Know
- Extract exported Activities includes activities that requires **permission**
- Java Code of selected Activity will Highlighted code that might be using Extras from intent
- Generated APK calls Exported activity at start of its MainActivity


# Dependencies

To have the tool working please install the following tools.
- scrcpy
- apktool
- Java -> openJdk@21 or later
- Android SDK 34 or later (Preferably have Android Studio installed) 


All the tools should be in PATH

Compatible with OS having /tmp folder.



