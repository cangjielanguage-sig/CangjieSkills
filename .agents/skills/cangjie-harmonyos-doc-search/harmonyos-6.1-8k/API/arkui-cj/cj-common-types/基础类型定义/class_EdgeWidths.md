## class EdgeWidths

```cangjie
public class EdgeWidths {
    public var top: ?Length
    public var right: ?Length
    public var bottom: ?Length
    public var left: ?Length
    public init(top!: ?Length = None, right!: ?Length = None, bottom!: ?Length = None, left!: ?Length = None)
}
```

**功能：** 设置弹窗背板的边框宽度。引入该对象时，至少传入一个参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var top

```cangjie
public var top: ?Length
```

**功能：** 上侧边框宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var right

```cangjie
public var right: ?Length
```

**功能：** 右侧边框宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var bottom

```cangjie
public var bottom: ?Length
```

**功能：** 下侧边框宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var left

```cangjie
public var left: ?Length
```

**功能：** 左侧边框宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length, ?Length)

```cangjie
public init(top!: ?Length = None, right!: ?Length = None, bottom!: ?Length = None, left!: ?Length = None)
```

**功能：** 构造EdgeWidths对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 上侧边框宽度。初始值为0.vp。|
|right|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 右侧边框宽度。初始值为0.vp。|
|bottom|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 下侧边框宽度。初始值为0.vp。|
|left|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 左侧边框宽度。初始值为0.vp。|