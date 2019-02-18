cmake_minimum_required(VERSION 3.1.0)

project(project)

find_package(OpenCV REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)
find_package(Qt5Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_library(gui gui.cpp vision.cpp)
target_link_libraries(gui Qt5::Core Qt5::Gui Qt5::Widgets ${OpenCV_LIBS})

add_executable(project WIN32 main.cpp)
target_link_libraries (project gui)

set(CMAKE_DIR "C:/Program Files/CMake")
set(QT_DIR "C:/Qt/5.11.2/msvc2017_64")

set(OPENCV_DIR "C:/opencv/build/x64/vc15/bin")
set(OPENCV_DLLS
	${OPENCV_DIR}/opencv_world401d.dll
	${OPENCV_DIR}/opencv_world401.dll
)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} ARGS -E copy ${file} $<TARGET_FILE_DIR:project>)
endforeach(file)
find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)
add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:project>/data)

find_program(WINDEPLOYQT_EXECUTABLE NAMES windeployqt HINTS ${QT_DIR} ENV QT_DIR PATH_SUFFIXES bin)
add_custom_command(TARGET project POST_BUILD COMMAND ${WINDEPLOYQT_EXECUTABLE} $<TARGET_FILE:project>)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} ARGS -E copy ${file} ${PROJECT_SOURCE_DIR}/bin)
endforeach(file)
install(TARGETS project DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(CODE "execute_process(COMMAND ${WINDEPLOYQT_EXECUTABLE} \"${PROJECT_SOURCE_DIR}/bin/project.exe\")")
