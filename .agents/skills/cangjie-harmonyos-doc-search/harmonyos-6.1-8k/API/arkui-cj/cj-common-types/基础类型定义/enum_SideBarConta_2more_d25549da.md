## enum SideBarContainerType

```cangjie
public enum SideBarContainerType <: Equatable<SideBarContainerType> {
    | Embed
    | Overlay
    | Auto
    | ...
}
```

**功能：** 容器内侧边栏样式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SideBarContainerType](#enum-sidebarcontainertype)>

### Embed

```cangjie
Embed
```

**功能：** 侧边栏嵌入到组件内，和内容区并列显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Overlay

```cangjie
Overlay
```

**功能：** 侧边栏浮在内容区上面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** Web的深色模式为跟随系统。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SideBarContainerType)

```cangjie
public operator func ==(other: SideBarContainerType): Bool
```

**功能：** 判断两个SideBarContainerType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SideBarContainerType](#enum-sidebarcontainertype)|是|-|要比较的另一个SideBarContainerType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SideBarContainerType)

```cangjie
public operator func !=(other: SideBarContainerType): Bool
```

**功能：** 判断两个SideBarContainerType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SideBarContainerType](#enum-sidebarcontainertype)|是|-|要比较的另一个SideBarContainerType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SideBarPosition

```cangjie
public enum SideBarPosition <: Equatable<SideBarPosition> {
    | Start
    | End
    | ...
}
```

**功能：** 设置侧边栏显示位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SideBarPosition](#enum-sidebarposition)>

### Start

```cangjie
Start
```

**功能：** 侧边栏位于容器左侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 侧边栏位于容器右侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SideBarPosition)

```cangjie
public operator func ==(other: SideBarPosition): Bool
```

**功能：** 判断两个SideBarPosition枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SideBarPosition](#enum-sidebarposition)|是|-|要比较的另一个SideBarPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SideBarPosition)

```cangjie
public operator func !=(other: SideBarPosition): Bool
```

**功能：** 判断两个SideBarPosition枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SideBarPosition](#enum-sidebarposition)|是|-|要比较的另一个SideBarPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|