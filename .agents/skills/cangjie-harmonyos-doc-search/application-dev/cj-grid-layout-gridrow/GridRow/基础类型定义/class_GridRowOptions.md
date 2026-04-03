### class GridRowOptions

```cangjie
public class GridRowOptions {
    public var xs: ?Int32
    public var sm: ?Int32
    public var md: ?Int32
    public var lg: ?Int32
    public var xl: ?Int32
    public var xxl: ?Int32
    public init(
        xs!: ?Int32 = None,
        sm!: ?Int32 = None,
        md!: ?Int32 = None,
        lg!: ?Int32 = None,
        xl!: ?Int32 = None,
        xxl!: ?Int32 = None
    )
    public init(value: ?Int32)
}
```

**功能：** 栅格在不同宽度设备类型下，栅格列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var lg

```cangjie
public var lg: ?Int32
```

**功能：** **命名参数。** 在栅格大小为lg的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var md

```cangjie
public var md: ?Int32
```

**功能：** **命名参数。** 在栅格大小为md的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var sm

```cangjie
public var sm: ?Int32
```

**功能：** **命名参数。** 在栅格大小为sm的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xl

```cangjie
public var xl: ?Int32
```

**功能：** **命名参数。** 在栅格大小为xl的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xs

```cangjie
public var xs: ?Int32
```

**功能：** **命名参数。** 在栅格大小为xs的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var xxl

```cangjie
public var xxl: ?Int32
```

**功能：** **命名参数。** 在栅格大小为xxl的设备上，栅格子组件占据的列数或偏移的列数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?Int32, ?Int32, ?Int32, ?Int32, ?Int32)

```cangjie
public init(
    xs!: ?Int32 = None,
    sm!: ?Int32 = None,
    md!: ?Int32 = None,
    lg!: ?Int32 = None,
    xl!: ?Int32 = None,
    xxl!: ?Int32 = None
)
```

**功能：** 构造一个GridRowOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xs|?Int32|否|None| **命名参数。** 在栅格大小为xs的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：2|
|sm|?Int32|否|None| **命名参数。** 在栅格大小为sm的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：4|
|md|?Int32|否|None| **命名参数。** 在栅格大小为md的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：8|
|lg|?Int32|否|None| **命名参数。** 在栅格大小为lg的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：12|
|xl|?Int32|否|None| **命名参数。** 在栅格大小为xl的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：12|
|xxl|?Int32|否|None| **命名参数。** 在栅格大小为xxl的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：12|

#### init(?Int32)

```cangjie
public init(value: ?Int32)
```

**功能：** 构造一个GridRowOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-| 在任意栅格大小的设备上，栅格子组件占据的列数或偏移的列数。<br>初始值：12|