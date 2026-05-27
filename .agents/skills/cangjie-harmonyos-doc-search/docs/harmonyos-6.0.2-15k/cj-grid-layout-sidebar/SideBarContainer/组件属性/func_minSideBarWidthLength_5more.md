### func minSideBarWidth(Length)

```cangjie
public func minSideBarWidth(value: Length): This
```

**功能：** 设置侧边栏最小宽度。

> **说明：**
>
> - 设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过使用侧边栏容器本身宽度。
> - minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|侧边栏最小宽度。<br>初始值：240.vp。|

### func showControlButton(Bool)

```cangjie
public func showControlButton(isShow: Bool): This
```

**功能：** 设置是否显示控制按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isShow|Bool|是|-|是否显示控制按钮。<br>true：显示控制按钮。<br>false：不显示控制按钮。<br>初始值：true。|

### func showSideBar(Bool)

```cangjie
public func showSideBar(isShow: Bool): This
```

**功能：** 设置是否显示侧边栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isShow|Bool|是|-|是否显示侧边栏。<br>true：显示侧边栏。<br>false：不显示侧边栏。<br>初始值：true。|

### func sideBarPosition(SideBarPosition)

```cangjie
public func sideBarPosition(value: SideBarPosition): This
```

**功能：** 设置侧边栏显示位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SideBarPosition](./cj-common-types.md#enum-sidebarposition)|是|-|侧边栏显示位置。<br>初始值：SideBarPosition.Start。|

### func sideBarWidth(Length)

```cangjie
public func sideBarWidth(value: Length): This
```

**功能：** 设置侧边栏的宽度。

> **说明：**
>
> 设置为小于0的值时按默认值显示。受最小宽度和最大宽度限制，不在限制区域内取最近的点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|侧边栏的宽度。<br>初始值：240.vp。<br>单位：vp。|