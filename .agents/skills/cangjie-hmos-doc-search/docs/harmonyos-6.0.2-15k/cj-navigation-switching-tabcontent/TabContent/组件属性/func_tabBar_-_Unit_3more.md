### func tabBar(() -> Unit)

```cangjie
public func tabBar(callback: () -> Unit): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|自定义UI描述。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

### func tabBar(SubTabBarStyle)

```cangjie
public func tabBar(content: SubTabBarStyle): This
```

**功能：** 设置TabBar上显示内容。底部样式没有下划线效果。icon异常时显示灰色图块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[SubTabBarStyle](#class-subtabbarstyle)|是|-|子页签样式。|

### func tabBar(BottomTabBarStyle)

```cangjie
public func tabBar(content: BottomTabBarStyle): This
```

**功能：** 设置TabBar上显示内容。底部样式没有下划线效果。icon异常时显示灰色图块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[BottomTabBarStyle](#class-bottomtabbarstyle)|是|-|底部页签和侧边页签样式。|