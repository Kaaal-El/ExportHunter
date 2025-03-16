# ExportHunter  

ExportHunter is a tool that extracts exported activities from an APK and allows users to initiate `am start` commands with specified intent values. It also generates code to build an APK that triggers the exported activity with predefined intent and bundle parameters.  

This tool is ideal for testing and automating interactions with exported components.  

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
3. **Modify Intent Data** – Add extras or bundles if necessary.  
4. **Launch via ADB** – Execute the selected activity on a device.  
5. **Generate & Deploy APK** – Automatically create and launch an APK for testing.  

<img width="1131" alt="1" src="https://github.com/user-attachments/assets/242134c2-5432-4389-942a-204cf63e5a81" />

## Dependencies  

Ensure the following tools are installed and available in your system `PATH`:  

- **ADB**
- **scrcpy**  
- **apktool**  
- **Java** – `openJDK@21` or later  
- **Android SDK 34** or later (Recommended: Android Studio installed)  

### Compatibility  

- Requires an OS with a `/tmp` folder.  
