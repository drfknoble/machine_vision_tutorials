cmake_minimum_required(VERSION 3.5)

project(project)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(OpenCV_DIR "C:/opencv/build")
find_package(OpenCV PATHS "c:/opencv/build")

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430d.dll
	)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430.dll
	)
endif()

# Build

add_executable(gray_dilate "gray_dilate.cpp" "utils.cpp" "utils.hpp")
target_link_libraries (gray_dilate ${OpenCV_LIBS})
add_custom_command(TARGET gray_dilate POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:gray_dilate>/data)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET gray_dilate POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${file} $<TARGET_FILE_DIR:gray_dilate>)
endforeach(file)

# Install

install(TARGETS gray_dilate DESTINATION ${PROJECT_SOURCE_DIR}/bin)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)

foreach(file ${OPENCV_DLLS})
	install(FILES ${file} DESTINATION ${PROJECT_SOURCE_DIR}/bin/)
endforeach(file)