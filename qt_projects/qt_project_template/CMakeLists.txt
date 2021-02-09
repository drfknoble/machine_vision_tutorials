cmake_minimum_required(VERSION 3.5.1)

project(project)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# QtCreator supports the following variables for Android, which are identical to qmake Android variables.
# Check http://doc.qt.io/qt-5/deployment-android.html for more information.
# They need to be set before the find_package(Qt5 ...) call.

#if(ANDROID)
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
#    if (ANDROID_ABI STREQUAL "armeabi-v7a")
#        set(ANDROID_EXTRA_LIBS
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libcrypto.so
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libssl.so)
#    endif()
#endif()

find_package(Qt5 COMPONENTS Widgets REQUIRED)
find_package(OpenCV REQUIRED PATHS "C:/opencv/build")

set(OpenCV_DIR "C:/opencv/build")
set(QT_DIR "C:/Qt/5.15.0/msvc2019_64")
set(Qt5_DIR "C:/Qt/5.15.0/msvc2019_64/lib/cmake/Qt5")

add_library(gui gui.cpp gui.hpp vision.cpp vision.hpp)
target_link_libraries(gui Qt5::Core Qt5::Gui Qt5::Widgets ${OpenCV_LIBS})

add_executable(project WIN32 main.cpp main.hpp)
target_link_libraries (project gui)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(OPENCV_DLLS
                ${OpenCV_DIR}/x64/vc15/bin/opencv_world440d.dll
	)
elseif(CMAKE_BUILD_TYPE STREQUAL "RelWithDebInfo")
	set(OPENCV_DLLS
                ${OpenCV_DIR}/x64/vc15/bin/opencv_world440.dll
	)
endif()

# Utilities

set(CMAKE_DIR "C:/Program Files/CMake")
find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)
find_program(WINDEPLOYQT_EXECUTABLE NAMES windeployqt HINTS ${QT_DIR} ENV QT_DIR PATH_SUFFIXES bin)

# Build

set_property(TARGET project PROPERTY CXX_STANDARD 17)

add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:project>/data)
add_custom_command(TARGET project POST_BUILD COMMAND ${WINDEPLOYQT_EXECUTABLE} $<TARGET_FILE:project>)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} ARGS -E copy ${file} $<TARGET_FILE_DIR:project>)
endforeach(file)

# Install

install(TARGETS project DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(CODE "execute_process(COMMAND ${WINDEPLOYQT_EXECUTABLE} \"${PROJECT_SOURCE_DIR}/bin/project.exe\")")

foreach(file ${OPENCV_DLLS})
	install(FILES ${file} DESTINATION ${PROJECT_SOURCE_DIR}/bin/)
endforeach(file)
