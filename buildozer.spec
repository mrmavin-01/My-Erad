[app]
# (str) Title of your application
title = ERAD App

# (str) Package name
package.name = eradapp

# (str) Package domain (unique identifier)
package.domain = org.erad.app

# (str) Version of your application
version = 1.0.0

# (list) Application requirements
# Comma separated list of requirements
# The main dependencies are kivy, kivymd, and jnius (for Android interaction)
# Include other dependencies as required
# Example: requirements = kivy, kivymd, jnius
#            Use 'pyjnius' for native Android features like vibration
#            Ensure you have all your dependencies here.
requirements = kivy, kivymd, pyjnius, requests, pillow

# (str) Custom source folder
# You can leave this as is if your app source is in the root directory.
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions for the package
# Example: source.include_patterns = assets/*,libs/*
# You may want to include specific directories like assets.
source.include_patterns = assets/*,profile.png,5690898.png,earnings.png,law.png,cogwheel.png,question.png,communicate.png

# (list) Application entry point, default is main.py
# You should change this to point to the Python script that starts your app (e.g., main.py).
entrypoint = main.py

# (list) List of libraries to link against
# Example: link_libraries = SDL2, GLESv2, OpenGL, etc.
# These libraries are generally required for Kivy on Android.
# The default should work for most use cases.
# link_libraries = 

# (list) Permissions (Android-specific)
# For example, you may need to include access to storage or network permissions.
# Add the following permissions for file access:
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Android API to target (set to match the current SDK)
android.api = 33
android.accept_sdk_license = True 

# (str) Android NDK version
# You can check the current NDK version on the Buildozer site or choose a suitable version.
android.ndk = 23b

# (int) Minimum Android API level (e.g., 21 is Lollipop)
android.minapi = 21

# (str) Android ABI
# You can select which architecture to target, e.g., armeabi-v7a, arm64-v8a, etc.
android.arch = arm64-v8a

# (bool) Build APK for Android
# Whether to build the APK as a release version (True) or debug version (False).
android.debug = 0

# (str) The version of Python you want to use for the app
# Set this to 'python3' to use Python 3.x
# python_version = 3

# (str) List of additional build requirements
# In this case, you'll need to ensure that the `pyjnius` library is included in the build process.
# buildozer will automatically include necessary dependencies.
buildozer.buildozer_add_requirements = pyjnius

# (bool) Whether to use a custom Python installation
# If you have custom dependencies installed, you can activate this feature.
# Use 'True' if you're using a precompiled Python installation.
use_python_for_build = True

# (list) Include any extra dependencies like native code libraries
# Example: include_extra_files = data/*.txt
# Exclude any irrelevant files or unwanted assets
include_extra_files =

# Android SDK setup
# SDK tools location for Android build tools and SDK
# You can specify the location if needed, or it will be downloaded automatically.
# android.sdk_path = /path/to/sdk

# Define additional settings for Android app, such as theme style (Dark Mode for KivyMD)
android.theme = "dark"
