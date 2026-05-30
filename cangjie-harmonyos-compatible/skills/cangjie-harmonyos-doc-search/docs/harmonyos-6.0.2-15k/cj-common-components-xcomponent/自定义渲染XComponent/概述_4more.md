## 概述

XComponent组件作为一种渲染组件，可用于EGL/OpenGLES和媒体数据写入，通过使用XComponent持有的“NativeWindow”来渲染画面，通常用于满足开发者较为复杂的自定义渲染需求，例如相机预览流的显示和游戏画面的渲染。可通过指定type字段来实现不同的渲染方式，当前支持[XComponentType.SURFACE](../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#enum-xcomponenttype)类型。对于SURFACE类型，开发者将定制的绘制内容单独展示到屏幕上。

目前XComponent组件支持XComponentController场景，在仓颉侧获取SurfaceId，生命周期回调，以及触摸、鼠标、按键等事件回调均在仓颉侧触发。

## 自绘制原理说明

XComponent持有一个surface，开发者能通过调用NativeWindow等接口，申请并提交Buffer至图形队列，以此方式将自绘制内容传送至该surface。XComponent负责将此surface整合进UI界面，其中展示的内容正是开发者传送的自绘制内容。surface的默认位置与大小与XComponent组件一致，开发者可利用[setXComponentSurfaceRect](../../API_Reference/source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md#func-setxcomponentsurfacerectsurfacerect)接口自定义调整surface的位置和大小。

> **说明：**
>
> 当开发者传输的绘制内容包含透明元素时，surface区域的显示效果会与下方内容进行合成展示。例如，若传输的内容完全透明，且XComponent的背景色被设置为黑色，同时Surface保持默认的大小与位置，则最终显示的将是一片黑色区域。

## XComponentController 场景

通过在仓颉侧获取SurfaceId，布局信息、生命周期回调、触摸、鼠标、按键等事件回调等均在仓颉侧触发，按需传递到Native侧进行处理。主要开发场景如下：

- 基于仓颉侧获取的SurfaceId，在Native侧调用接口创建出NativeWindow实例。
- 利用NativeWindow和EGL接口开发自定义绘制内容以及申请和提交Buffer到图形队列。
- 仓颉侧获取生命周期、事件等信息传递到Native侧处理。

XComponentController 生命周期请参见 [XComponent](../../API_Reference/source_zh_cn/arkui-cj/cj-rendering-drawing-xcomponent.md)。

## Native XComponent

Native部分需要调用到 Native XComponent 接口，详情请参见 [Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)。