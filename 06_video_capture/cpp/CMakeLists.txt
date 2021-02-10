cmake_minimum_required(VERSION 3.5)

project(project)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(OpenCV_DIR "c:/opencv/build")
find_package(OpenCV PATHS "c:/opencv/build")

include_directories(${PROJECT_SOURCE_DIR}
                    ${OpenCV_INLCUDE_DIRS})
link_directories(${OpenCV_LIBRARY_DIRS})

if(${CMAKE_BUILD_TYPE} MATCHES Debug)
	set(OPENCV_DLLS
		"${OpenCV_DIR}/x64/vc15/bin/opencv_world430d.dll"
	)
else()
	set(OPENCV_DLLS
		"${OpenCV_DIR}/x64/vc15/bin/opencv_world430.dll"
	)
endif()

# build

add_executable(main "video.cpp" "video.hpp")
target_link_libraries(main ${OpenCV_LIBS})

foreach(file ${OPENCV_DLLS})
	add_custom_command(TARGET main POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different "${file}" $<TARGET_FILE_DIR:main>)
endforeach(file)

# install

install(TARGETS main DESTINATION "${PROJECT_SOURCE_DIR}/bin")

foreach(file ${OPENCV_DLLS})
	install(FILES "${file}" DESTINATION "${PROJECT_SOURCE_DIR}/bin")
endforeach(file)
