# Activity 1

## Introduction

To develop our understanding of the Open Computer Vision (OpenCV) library, let's write a program that uses the code and functions introduced in Tutorials 1 - 4.

## Aims

The aims of this activity are to:

1. Practise writing programs in C++
1. Pratise building software using CMake
1. Familiarise ourselves with OpenCV's fuctions

## Objectives

The objectives of this activity are to:

1. Write a program that uses the C++ standard and OpenCV libraries to load an image, display it, and write a copy to a directory
1. Write a CMakeLists.txt file
1. Build an executable using CMake

## Requirements

To complete this activity, you need the following tools:

1. [CMake 3.17.2](https://cmake.org/)
1. [Visual Studio Code](https://code.visualstudio.com/) and either: 
    1) GCC via [Mingw-w64](http://mingw-w64.org/doku.php)
    
    or
    
    2) [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

    or

1. [Visual Studio Community 2019](https://visualstudio.microsoft.com/vs/)
1. [OpenCV 4.3.0](https://opencv.org/)

I recommend installing Visual Studio Community 2019 and the Desktop development with C++ workload. If you've installed Visual Studio IDE, you can use its C++ in Visual Studio Code.

## List of Files

This project is organised as follows:

1. [CMakeLists.txt](CMakeLists.txt)
1. [main.cpp](main.cpp)
1. [main.hpp](main.hpp)
1. [README.md](README.md)
1. [data/input_image.png](data/input_image.png)

The file CMakeLists.txt is a text file. We will use it to type commands that CMake will use to build our project. The files main.cpp and main.hpp are C++ source and header files. We will use them to write code that the compiler will use to build our executable. The sub-directory data contains the image input_image.png. We will use it in our program.

## Steps

Here, we will work throught the steps needed to load an image, display it, and write a copy to a directory. 

## Step 1

Open [main.hpp](main.hpp). Complete the following:

1. Create a header guard
1. Include the standard library's iostream and filesystem header files
1. Include OpenCV's header file

## Step 2

Open [main.cpp](main.cpp). Complete the following:

1. Include main.hpp
1. Define the ```main()``` function
1. Write a try-catch statement
1. In the try statement:
    1. Use the standard library's `path` class to get the executable's parent path. Assign the results to a variable named "executable_path"
    1. Use the standard library's `cout` output stream to display the contents of `executable_path`
    1. Append "data/input_image.png" to `executable_path`. Assign the results to a variable named "input_file"
    1. Use the standard library's `cout` output stream to display the contents of `input_file`
    1. Write an `if` statement that checks whether a file with a name equal to `input_file`'s contents exists. If false, return 1.
    1. Use OpenCV's `imread()` function to read a file with a name equal to `input_file`'s content. Assign the results to a variable named "image"
    1. Write an `if` statement that checks whether `image` is empty. If true, return 2
    1. Use OpenCV's `imshow()` function to display `image` in a window named "image"
    1. Write a `while` loop that loops continuously until the user presses the <kbd>Esc</kbd> key
    1. Use OpenCV's `destroyWindow()` function to close the `image` window
    1. Append "data/output_image.png" to `executable_path`. Assign the results to a variable named "output_file"
    1. Use the standard library's `cout` output stream to display the contents of `output_file`
    1. Use OpenCV's `imwrite()` function to write `image` to a file with a name equal to `output_file`'s contents
    1. Return 0
1. In the catch statement:
    1. Display information about an exception

## Step 3

Open [CMakeLists.txt](CMakeLists.txt). Complete the following:

1. Define a minimum required CMake version
1. Name the project "main"
1. Set the C++ standard to be C++17
1. Find the OpenCV package
1. Include OpenCV's include directories to the project
1. Include OpenCV's libraries directories to the project
1. Add an executable to the project
1. Write a custom command to copy the project's data sub-directory to the build directory
1. Write a command to install the project into a sub-directory named "bin"
1. Write a command to install the project's data sub-directory into the bin sub-directory

## Step 4

### Visual Studio Code

Open the Command Palette via either <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> or <kbd>F1</kbd> and enter the following command:

    CMake:Configure

Wait for the command to complete.

Open the Command Palette and enter the following command:

    CMake:Build

Wait for the command to complete.

Open the Command Palette and enter the following command:

    CMake:Run Without Debugging

Wait for the command to complete.

Open the Command Palette and enter the following command:

    CMake:Install

Wait for the command to complete.

## Output

Upon successful completion of Steps 1 - 4, the following image will be displayed:

![output](data/input_image.png)

A copy of this image is saved as output_image.png in the data sub-directory.

## Conclusion

In this activity, we've written a program that uses the code and functions introduced in Tutorials 1 - 4.

I hope you've found it helpful.