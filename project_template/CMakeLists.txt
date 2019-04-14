cmake_minimum_required(VERSION 3.5.1)

project(project)

set(CMAKE_DIR "C:/Program Files/CMake")
set(QT_DIR "C:/Qt/5.12.2/msvc2017_64")

set(OpenCV_DIR "C:/opencv/build")
set(Qt5_DIR "C:/Qt/5.12.2/msvc2017_64/lib/cmake/Qt5")

find_package(OpenCV REQUIRED)
find_package(Qt5 COMPONENTS Core Gui Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_library(gui gui.cpp vision.cpp)
target_link_libraries(gui Qt5::Core Qt5::Gui Qt5::Widgets ${OpenCV_LIBS})

add_executable(project WIN32 main.cpp)
target_link_libraries (project gui)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world410d.dll
	)
elseif(CMAKE_BUILD_TYPE STREQUAL "RelWithDebInfo")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world410.dll
	)
endif()

# Build

find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)
add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:project>/data)
find_program(WINDEPLOYQT_EXECUTABLE NAMES windeployqt HINTS ${QT_DIR} ENV QT_DIR PATH_SUFFIXES bin)
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