### func backButtonIcon(AppResource)

```cangjie
public func backButtonIcon(value: AppResource): This
```

**功能：** 设置标题栏返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|返回键图片资源。|

### func backButtonIcon(PixelMap)

```cangjie
public func backButtonIcon(value: PixelMap): This
```

**功能：** 设置标题栏返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|返回键图片资源。|

### func menus(Array\<NavigationMenuItem\>)

```cangjie
public func menus(values: Array<NavigationMenuItem>): This
```

**功能：** 设置页面右上角菜单。不设置时不显示菜单项。使用Array\<NavigationMenuItem\> 写法时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|Array\<[NavigationMenuItem](./cj-navigation-switching-navigation.md#class-navigationmenuitem)\>|是|-|页面右上角菜单。|

### func menus(() -> Unit)

```cangjie
public func menus(value: () -> Unit): This
```

**功能：** 设置页面右上角菜单。不设置时不显示菜单项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|() -> Unit|是|-|页面右上角菜单。|

### func ignoreLayoutSafeArea(Array\<LayoutSafeAreaType>, Array\<LayoutSafeAreaEdge>)

```cangjie
public func ignoreLayoutSafeArea(types!: Array<LayoutSafeAreaType> = [LayoutSafeAreaType.SYSTEM], edges!: Array<LayoutSafeAreaEdge> = [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]): This
```

**功能：** 控制组件的布局，使其扩展到非安全区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|types|Array\<[LayoutSafeAreaType](./cj-common-types.md#enum-layoutsafeareatype)>|否|[LayoutSafeAreaType.SYSTEM]|配置扩展安全区域的类型。|
|edges|Array\<[LayoutSafeAreaEdge](./cj-common-types.md#enum-layoutsafeareaedge)>|否|[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]|配置扩展安全区域的方向。|

> **说明：**
>
> 组件设置ignoreLayoutSafeArea之后生效的条件为：
>
> - 设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。
> - 若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。