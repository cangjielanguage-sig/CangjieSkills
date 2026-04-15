## class SizeOptions

```cangjie
public class SizeOptions {
    public var width: Length = 0
    public var height: Length = 0
    public init(width!: Length = 0, height!: Length = 0)
}
```

**功能：** 宽高尺寸类型，用于描述组件布局时的宽高尺寸大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var height

```cangjie
public var height: Length = 0
```

**功能：** 高度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var width

```cangjie
public var width: Length = 0
```

**功能：** 宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Length, Length)

```cangjie
public init(width!: Length = 0, height!: Length = 0)
```

**功能：** SizeOptions的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|否|0| **命名参数。** 宽度。初始值: 0|
|height|[Length](./cj-common-types.md#interface-length)|否|0| **命名参数。** 高度。初始值: 0|