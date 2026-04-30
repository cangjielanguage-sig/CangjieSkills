### class BreakPoints

```cangjie
public class BreakPoints {
    public BreakPoints(
        public var  value!: Array<Length> = [320.vp, 520.vp, 840.vp],
        public var  reference!: BreakpointsReference = BreakpointsReference.WindowSize
     )
}
```

**功能：** 构建栅格容器组件的断点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var reference

```cangjie
public var reference: BreakpointsReference = BreakpointsReference.WindowSize
```

**功能：** 断点切换参照物。

**类型：** [BreakpointsReference](#enum-breakpointsreference)

**读写能力：** 可读写

**起始版本：** 12

#### var value

```cangjie
public var value: Array<Length> = [320.vp, 520.vp, 840.vp]
```

**功能：** 断点位置的单调递增数组设置。

**类型：** Array\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 12

#### BreakPoints(Array\<Length>, BreakpointsReference)

```cangjie
public BreakPoints(
    public var value!: Array<Length> = [320.vp, 520.vp, 840.vp],
    public var reference!: BreakpointsReference = BreakpointsReference.WindowSize
 )
```

**功能：** 构造一个BreakPoints对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[Length](./cj-common-types.md#interface-length)>|否|[320.vp,520.vp,840.vp]| **命名参数。** 断点位置的单调递增数组设置。|
|reference|[BreakpointsReference](#enum-breakpointsreference)|否|BreakpointsReference.WindowSize| **命名参数。** 断点切换参照物。|

### struct GridRowColumnOption

```cangjie
public struct GridRowColumnOption {
    public GridRowColumnOption(
        xs!: Int32 = 12,
        sm!: Int32 = 12,
        md!: Int32 = 12,
        lg!: Int32 = 12,
        xl!: Int32 = 12,
        xxl!: Int32 = 12
    )
}
```

**功能：** 栅格在不同宽度设备类型下，栅格列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### GridRowColumnOption(Int32, Int32, Int32, Int32, Int32, Int32)

```cangjie
public GridRowColumnOption(
    xs!: Int32 = 12,
    sm!: Int32 = 12,
    md!: Int32 = 12,
    lg!: Int32 = 12,
    xl!: Int32 = 12,
    xxl!: Int32 = 12
)
```

**功能：** 构造一个GridRowColumnOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xs|Int32|否|12| **命名参数。** 在栅格大小为xs的设备上，栅格子组件占据的列数或偏移的列数。|
|sm|Int32|否|12| **命名参数。** 在栅格大小为sm的设备上，栅格子组件占据的列数或偏移的列数。|
|md|Int32|否|12| **命名参数。** 在栅格大小为md的设备上，栅格子组件占据的列数或偏移的列数。|
|lg|Int32|否|12| **命名参数。** 在栅格大小为lg的设备上，栅格子组件占据的列数或偏移的列数。|
|xl|Int32|否|12| **命名参数。** 在栅格大小为xl的设备上，栅格子组件占据的列数或偏移的列数。|
|xxl|Int32|否|12| **命名参数。** 在栅格大小为xxl的设备上，栅格子组件占据的列数或偏移的列数。|

**说明：**

在GridRow栅格组件中，允许开发者使用breakpoints自定义修改[断点](../../../Dev_Guide/arkui-cj/cj-layout-development-grid-layout.md#栅格系统断点)的取值范围，最多支持xs、sm、md、lg、xl、xxl六个断点，且名称不可修改。假设传入的数组是[n0, n1, n2, n3, n4]，各个断点取值如下：

|断点|取值范围|
|:---|:---|
|xs| **命名参数。** [0,n0)|
|sm| **命名参数。** [n0,n1)|
|md| **命名参数。** [n1,n2)|
|lg| **命名参数。** [n2,n3)|
|xl| **命名参数。** [n3,n4)|
|xxl| **命名参数。** [n4,+∞)|