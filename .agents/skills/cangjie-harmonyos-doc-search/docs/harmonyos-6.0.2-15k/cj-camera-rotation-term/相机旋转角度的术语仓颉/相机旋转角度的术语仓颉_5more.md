# 相机旋转角度的术语（仓颉）

在适配相机旋转角度中涉及设备方向、镜头角度、屏幕显示角度等多个术语，开发者可以了解相关概念，帮助理解框架的运作机制。

## 设备自然方向

**设备自然方向**指设备默认的使用方向，以手机为例，如图所示，手机的自然方向为竖屏且充电口向下。

![Camera Natural Direction](./figures/camera-natural-direction.png)

## 屏幕显示方向

**屏幕显示方向**指当前用户视角下，设备正确的显示方向。

![Camera Screen Display Direction](./figures/camera-screen-display-direction.png)

## 屏幕旋转角度

显示设备的屏幕顺时针旋转角度，简称为**屏幕旋转角度**，即设备从自然方向到当前方向的顺时针夹角。

如图所示，图示夹角即为屏幕旋转角度，可通过[Display.rotation](../../../API_Reference/source_zh_cn/arkui-cj/cj-apis-display.md#prop-rotation)获取。

![Camera Screen Rotation Angle](./figures/camera-screen-rotation-angle.png)

## 相机镜头安装角度

**相机镜头安装角度**指相机采集图像方向到设备自然方向在顺时针方向的夹角。

以手机为例，手机后置相机传感器是横屏安装的，当手机在竖屏方向使用后置相机镜头拍摄时，相机采集到的原始图像方向如图所示。

此时图像需要顺时针旋转90度，才能与设备自然方向保持一致，所以**后置相机的镜头角度为90度**。

![Camera Lens Angle 90](./figures/camera-lens-angle-90.png)

而手机前置镜头，是朝向使用者的，当手机在竖屏方向使用前置相机镜头拍摄时，出图方向与后置出图方向互为镜像，如下图所示，**前置相机的镜头角度为270度**。

![Camera Lens Angle 270](./figures/camera-lens-angle-270.png)