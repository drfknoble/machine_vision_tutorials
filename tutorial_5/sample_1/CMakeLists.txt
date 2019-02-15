cmake_minimum_required(VERSION 3.1.0)

project(project)

find_package(OpenCV REQUIRED)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(project main.cpp)
target_link_libraries (project ${OpenCV_LIBS})

set(CMAKE_DIR "C:/Program Files/CMake")

set(OPENCV_DIR "C:/opencv/build/x64/vc15/bin")

set(OPENCV_DLLS
	${OPENCV_DIR}/opencv_world400d.dll
	${OPENCV_DIR}/opencv_world400.dll
)

find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)

# Build

# add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:project>/data)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET project POST_BUILD COMMAND ${CMAKE_EXECUTABLE} ARGS -E copy ${file} $<TARGET_FILE_DIR:project>)
endforeach(file)

# Install

install(TARGETS project DESTINATION ${PROJECT_SOURCE_DIR}/bin)
# install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)

foreach(file ${OPENCV_DLLS})
	install(FILES ${file} DESTINATION ${PROJECT_SOURCE_DIR}/bin/)
endforeach(file)