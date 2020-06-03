cmake_minimum_required(VERSION 3.5.1)

project(project)

set(QT_DIR "C:/Qt/5.14.2/msvc2017_64")
set(Qt5_DIR "C:/Qt/5.14.2/msvc2017_64/lib/cmake/Qt5")

find_package(Qt5 COMPONENTS Core Gui Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_library(gui gui.cpp)
target_link_libraries(gui Qt5::Core Qt5::Gui Qt5::Widgets)

add_executable(project WIN32 main.cpp)
target_link_libraries (project gui)

# Utilities

set(CMAKE_DIR "C:/Program Files/CMake")
find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)
find_program(WINDEPLOYQT_EXECUTABLE NAMES windeployqt HINTS ${QT_DIR} ENV QT_DIR PATH_SUFFIXES bin)

# Build

set_property(TARGET project PROPERTY CXX_STANDARD 17)

add_custom_command(TARGET project POST_BUILD COMMAND ${WINDEPLOYQT_EXECUTABLE} $<TARGET_FILE:project>)

# Install

install(TARGETS project DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(CODE "execute_process(COMMAND ${WINDEPLOYQT_EXECUTABLE} \"${PROJECT_SOURCE_DIR}/bin/project.exe\")")
