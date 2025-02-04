# Readme

This project is structured in two parts. 
- Firstly is the **data/** directory. This contains runs/ a subdirectory with user data from the user evaluation. 
Each run (structured Participant 1 VF, Participant 2 VF, Participant 1 NVF...) contains a **left/** and **right/** folder (for each eye). 
**raw/**, **processed/** and **reports/** contain the raw test output, graphs, and final report respectively.

- The second part is **src/** which contains **L4-Project**, **scripts/** and **tests/**. They contain the main Unity project, complimentry external scripts 
for data processing and the user test respectively. Within **L4-Project** contains **Assets/ProjectAssets** which is where assets (scripts, models, etc)
that were coded and made for this project (however, many of the SDKs have used assets outwith this folder, that are used for this project, hence there being in **Assets/**).
    - **L4-Project/assets/ProjectAssets** includes **scripts/**, **models/**, **scenes/** and **materials/**:
        - **scripts/**: contains the scripts used for the functionality of testing, logging and interaction.
        - **models/**: contains the models used, such as stimuli, central point and the plane were stimuli are displayed.
        - **scenes/**: contains the main menu and both testing environments. 
        - **materials/**: the material or shaders used on assets to give them colour, shading and texture.

**NOTE: In order to use many of the head-mounted display and VR capabilities of Unity, a number of SDKs were used. As far as we are aware all scripts include a copyright disclaimer 
at the top. The SDKs we used (outlined in the dissertation) were: OpenVR (Unity/Steam VR management plugin), SteamVR (interaction manager), SRanipal (Eyetracking).**



## Build instructions
### Requirements

List of the pre-requisite software required to run project:
* Unity (2019.4.35f1)
* SteamVR (2.7.3)
* HTC Vive Pro Eye Headset
* HTC Vive controller
* SteamVR 2.0 base Stations (one may work, but HMD is optimised for two)
* SRanipal (1.3.6.8)
* Windows 10 with admin rights

### Build steps
Running should be done through the Unity Editor. It is important that the entire repository is cloned due to the file setup. While the program will 
create **runs/** and its subsequent subdirectories, test data and scripts are collected through their respective directories. 

To add the project to your Unity Editor, select 'open' then 'open project from disk', then select **src/L4-Project**.
Before running, the user should ensure they have the necessary pre-requisites. They will run, when the user opens the project through the Unity Editor.
Both require admin rights to run, once steamVR has opened - you may press the start (or play) button at the top of the Unity window.
When first entering one of the test environments (either through the UI or manually by clicking the scene in assets) SRAnipal, will require confirmation to run
as it requires admin approval. **It's important to do this before building or testing** as SteamVR may need to setup supplemetory scripts and action dictionaries.

To build:
- select 'file'
- select 'Build Settings'
- Ensure all scenes are selected
- Select 'PC, Mac & Linux Standalone' as the platform option
- Select 'Windows' with 'X86_64' architecture
- Select 'build', which will generate an application executable


To Test:
- Ensure you have followed the steps in the first paragraph
- Ensure you are in the main Menu (projectassets/scenes/main)
- Click play
- The user should have both controllers infront of them, and they may use the trigger to interact with the UI menu
- Once in one of the test environments (or scenes) they may start the test with the tracking pad button. The test will begin five seconds after
- They can register a stimulus by clicking the trigger. 
- Currently testing takes 6-7 minutes approximetly. After, the scripts will process raw data and generate a pdf. An output path is printed in Unitys console
- To change the test file, users should locate the 'gameObject' and change the file path to another test in **tests/**
- All directory management is done automatically through the program. raw, processed and the final reporting data is generated automatically.