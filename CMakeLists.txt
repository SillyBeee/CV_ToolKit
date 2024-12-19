cmake_minimum_required(VERSION 3.5)

project(cv_toolkit)

# 找到 Qt 和 OpenCV
find_package(Qt5 REQUIRED COMPONENTS Core Widgets)
find_package(OpenCV REQUIRED)

set(CMAKE_AUTOMOC ON) # 启用自动生成 moc 文件
set(CMAKE_AUTOUIC ON) # 启用自动处理 UI 文件
set(CMAKE_AUTORCC ON) # 启用自动处理资源文件

add_executable(${PROJECT_NAME} cv_toolkit.cpp)

# 链接库
target_link_libraries(${PROJECT_NAME} Qt5::Core Qt5::Widgets ${OpenCV_LIBS})
