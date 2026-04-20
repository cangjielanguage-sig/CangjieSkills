### class BreakPoints

```cangjie
public class BreakPoints {
    public var value: ?Array<Length>
    public var reference: ?BreakpointsReference
    public init(value!: ?Array<Length> = None,
        reference!: ?BreakpointsReference = None
    )
}
```

**功能：** 构建栅格容器组件的断点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var reference

```cangjie
public var reference: ?BreakpointsReference
```

**功能：** 断点切换参照物。

**类型：** ?[BreakpointsReference](#enum-breakpointsreference)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var value

```cangjie
public var value: ?Array<Length>
```

**功能：** 断点位置的单调递增数组设置。

**类型：** ?Array\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Array\<Length>, ?BreakpointsReference)

```cangjie
public init(value!: ?Array<Length> = None,
    reference!: ?BreakpointsReference = None
)
```

**功能：** 构造一个BreakPoints对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Array\<[Length](./cj-common-types.md#interface-length)>|否|None| **命名参数。** 断点位置的单调递增数组设置<br>初始值：[320.vp, 600.vp, 840.vp]|
|reference|?[BreakpointsReference](#enum-breakpointsreference)|否|None| **命名参数。** 断点切换参照物。<br>初始值：BreakpointsReference.WindowSize|