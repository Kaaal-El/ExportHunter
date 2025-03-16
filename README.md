# ExportHunter  

ExportHunter is a tool that extracts exported activities from an APK and allows users to initiate `am start` commands with specified intent values. It also generates code to build an APK that triggers the exported activity with predefined intent and bundle parameters.  

This tool is ideal for testing and automating interactions with exported components.  

## Run
```
python3 ExportHunter.py
```

## Features  

1. **Extract Exported Activities** – Detects and lists all exported activities, including those requiring **permissions**.  
2. **Java Code Analysis** – Highlights intent-related methods in the selected activity’s Java code, identifying potential extra values.  
3. **Modify Intent Extras & Bundles** –  
   - Supports data types such as `--es`, `--ez`, `--ei`, etc.  
   - Use the **Configure** button to add extra values inside a bundle.  
4. **Launch via ADB** – Execute the selected activity directly on a connected device.  
5. **Generate & Launch APK Code** –  
   - Generates APK code for launching the exported activity.  
   - Automatically initiates the call to the exported activity upon launch.  
6. **No Root Required** – Works seamlessly on non-rooted Android devices.  
7. **Demo APK Included** – A sample `Demo.apk` is provided for user familiarization.  

## Usage  

1. **Browse an APK** – Load an APK to retrieve its exported activities.  
2. **Select an Activity** – Double-click an activity to view its Java code.  
3. **Modify Intent Data** – Add Action (-a), Data (-d), Extras and/or Bundles.  
4. **Launch via ADB** – Execute the selected activity on a device.  
5. **Generate & Deploy APK** – Automatically create and launch an APK for testing.  


## Demo
- Launch Using ADB (Secret 1)

https://github.com/user-attachments/assets/3b09179e-1cb3-48fb-8a5f-425b3253fa12

- Launch Using APK (Secret 2)

https://github.com/user-attachments/assets/8a5110a8-e5f4-43de-9f59-892f13e140ee



## Dependencies  

Ensure the following tools are installed and available in your system `PATH`:  

- **ADB**
- **scrcpy**  
- **apktool**  
- **Java** – `openJDK@21` or later  
- **Android SDK 34** or later (Recommended: Android Studio installed)  

### Compatibility  

- Requires an OS with a `/tmp` folder.  
