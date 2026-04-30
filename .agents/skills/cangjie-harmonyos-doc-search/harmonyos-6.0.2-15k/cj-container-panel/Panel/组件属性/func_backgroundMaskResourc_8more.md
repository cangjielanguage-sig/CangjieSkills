### func backgroundMask(ResourceColor)

```cangjie
public func backgroundMask(value: ResourceColor): This
```

**功能：** 指定Panel的背景蒙层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|指定的背景蒙层。<br/>初始值：0x08182431。|

### func dragBar(Bool)

```cangjie
public func dragBar(hasDragBar: Bool): This
```

**功能：** 设置是否存在dragbar。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasDragBar|Bool|是|-|是否存在dragbar，true表示存在，false表示不存在。<br/>初始值：true。|

### func fullHeight(Length)

```cangjie
public func fullHeight(value: Length): This
```

**功能：** 指定PanelMode.Full状态下的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|指定PanelMode.Full状态下的高度。<br/>初始值：当前组件主轴大小减去8vp空白区。<br/>**说明：** <br/>不支持设置百分比。|

### func halfHeight(Length)

```cangjie
public func halfHeight(value: Length): This
```

**功能：** 指定PanelMode.Half状态下的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|指定PanelMode.Half状态下的高度。<br/>初始值：当前组件主轴大小的一半。<br/>**说明：** <br/>不支持设置百分比。|

### func miniHeight(Length)

```cangjie
public func miniHeight(value: Length): This
```

**功能：** 指定PanelMode.Mini状态下的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|指定PanelMode.Mini状态下的高度。<br/>初始值：48.vp<br/>**说明：** <br/>不支持设置百分比。|

### func mode(PanelMode)

```cangjie
public func mode(mode: PanelMode): This
```

**功能：** 设置可滑动面板的初始状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[PanelMode](#enum-panelmode)|是|-|设置可滑动面板的初始状态。<br/>Minibar类型初始值：PanelMode.Mini；其余类型初始值：PanelMode.Half。|

### func panelType(PanelType)

```cangjie
public func panelType(ty: PanelType): This
```

**功能：** 设置可滑动面板的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ty|[PanelType](#enum-paneltype)|是|-|设置可滑动面板的类型。<br/>初始值：PanelType.Foldable。|

### func show(Bool)

```cangjie
public func show(value: Bool): This
```

**功能：** 当滑动面板弹出时，是否显示面板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|当滑动面板弹出时调用，true显示面板，false不显示面板。<br/>初始值：true。<br/>**说明：** <br/>该属性的优先级高于参数show。|