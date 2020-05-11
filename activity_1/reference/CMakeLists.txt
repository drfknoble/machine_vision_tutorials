cmake_minimum_required(VERSION 3.5)

project(main)

set(CMAKE_CXX_STANDARD 17)

set(OpenCV_DIR "C:/opencv/build")
find_package(OpenCV)

include_directories(${PROJECT_SOURCE_DIR}
                    ${OpenCV_INLCUDE_DIRS})
link_directories(${OpenCV_LIBRARY_DIRS})

add_executable(main main.cpp)
target_link_libraries(main ${OpenCV_LIBS})

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430d.dll
	)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
	set(OPENCV_DLLS
		${OpenCV_DIR}/x64/vc15/bin/opencv_world430.dll
	)
endif()

# utilities

# build

add_custom_command(TARGET main POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:main>/data)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET main POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${file} $<TARGET_FILE_DIR:main>)
endforeach(file)

# install

install(TARGETS main DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET main POST_BUILD COMMAND ${CMAKE_COMMAND} ARGS -E copy ${file} ${PROJECT_SOURCE_DIR}/bin)
endforeach(file)
