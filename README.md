# CV 工具箱

CV 工具箱是一个图形用户界面 (GUI) 应用程序，用于对图像应用各种计算机视觉处理技术。它是使用 Qt 和 OpenCV 构建的。

## 功能简介

- **高斯模糊**: 对图像应用高斯模糊，可调节内核大小和 sigma 值。
- **中值模糊**: 对图像应用中值模糊，可调节内核大小。
- **去噪**: 对图像应用快速非局部均值去噪，可调节强度。
- **颜色选择器**: 悬停在图像上以选择并显示 RGB 或 HSV 模式下的颜色。
- **去除水印**: 使用修复技术去除图像中的水印。
- **阈值处理**: 对图像应用二值化阈值处理，可调节阈值和最大值。
- **伽马校正**: 对图像应用伽马校正，可调节伽马值。

## 安装

1. 克隆仓库:
    ```sh
    git clone https://github.com/yourusername/CV_Toolbox.git
    cd CV_Toolbox
    ```

2. 安装依赖:
    - Qt
    - OpenCV

3. 构建项目:
    ```sh
    qmake
    make
    ```

## 使用方法

1. 运行应用程序:
    ```sh
    ./CV_Toolbox
    ```

2. 点击“加载图像”按钮加载图像。

3. 从下拉菜单中选择一个处理功能。

4. 根据需要调整参数。

5. 点击“应用”按钮将所选处理功能应用到图像。

6. 使用“切换到 HSV”按钮在使用颜色选择器功能时在 RGB 和 HSV 颜色显示模式之间切换。

