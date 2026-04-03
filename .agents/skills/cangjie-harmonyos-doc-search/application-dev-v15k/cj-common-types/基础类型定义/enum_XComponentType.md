## enum XComponentType

```cangjie
public enum XComponentType {
    | SURFACE
    | COMPONENT
    | TEXTURE
    | NODE
}
```

**功能：** 定义XComponent的具体配置参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### COMPONENT

```cangjie
COMPONENT
```

**功能：** XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NODE

```cangjie
NODE
```

**功能：** 用于Native UI节点的占位容器，开发者通过Native API 开发的页面组件可展示在此容器区域内。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SURFACE

```cangjie
SURFACE
```

**功能：** 用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。背景色设置为黑色时会走显示子系统（DSS）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TEXTURE

```cangjie
TEXTURE
```

**功能：** 用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容会和XComponent组件的内容合成后展示到屏幕上。1、保持帧同步，保持在同一帧将图形处理器（GPU）纹理和ArkUI其他的绘制指令统一发给渲染服务(RenderService)。2、动效和原生组件统一。3、走图形处理器（GPU）合成，相比surface可能走显示子系统（DSS）功耗更高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19