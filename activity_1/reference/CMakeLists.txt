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

# utilities

# build

add_custom_command(TARGET main POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/data $<TARGET_FILE_DIR:main>/data)

# install

install(TARGETS main DESTINATION ${PROJECT_SOURCE_DIR}/bin)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/data DESTINATION ${PROJECT_SOURCE_DIR}/bin)
