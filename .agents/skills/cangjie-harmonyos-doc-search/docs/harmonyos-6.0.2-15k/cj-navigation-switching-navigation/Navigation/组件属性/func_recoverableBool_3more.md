### func recoverable(Bool)

```cangjie
public func recoverable(recoverable: Bool): This
```

**功能：** 配置Navigation是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建改Navigation。并恢复至异常退出时的页面栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| recoverable  | Bool | 是 | - | Navigation是否可恢复，默认为不可恢复。<br>初始值：false。<br>true：页面栈可恢复。<br>false：页面栈不可恢复。|

> **说明：**
>
> - 使用改接口需要先设置Navigation的id属性，否则改接口无效。
> - 改接口需要配合NaviDestination的recoverable接口使用。
> - 恢复过程中不可序列化的信息，例如不可序列化的参数与用户设置的onPop等，会被丢弃，无法恢复。

### func enableDragBar(Bool)

```cangjie
public func enableDragBar(isEnabled: Bool): This
```

**功能：** 控制分栏场景下是否显示拖拽条。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isEnabled  | Bool | 是 | -| 是否开启拖拽条，默认为无拖拽条样式。<br>初始值：false。<br>true：有拖拽条样式。<br>false：无拖拽条样式。|

### func enableModeChangeAnimation(Bool)

```cangjie
public func enableModeChangeAnimation(isEnabled: Bool): This
```

**功能：** 控制是否开启单双栏切换时的动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| isEnabled  | Bool | 是  | - |是否开启单双栏切换时的动效。<br>初始值：true。<br>true：开启单双栏切换时的动效。<br>false：关闭单双栏切换时的动效。|