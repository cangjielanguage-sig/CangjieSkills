## class Position

```cangjie
public class Position {
    public var x: ?Length
    public var y: ?Length
    public init(x!: ?Length = None, y!: ?Length = None)
}
```

**功能：** 位置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Length
```

**功能：** 定义x轴坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Length
```

**功能：** 定义y轴坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length)

```cangjie
public init(x!: ?Length = None, y!: ?Length = None)
```

**功能：** 构造一个Position类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** x轴坐标，单位为vp。|
|y|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** y轴坐标，单位为vp。|

## class MotionPathOptions

```cangjie
public class MotionPathOptions {
    public var path: ?String
    public var from: ?Float64
    public var to: ?Float64
    public var rotatable: ?Bool
    public init(path!: ?String, from!: ?Float64 = None, to!: ?Float64 = None, rotatable!: ?Bool = None)
}
```

**功能：** 设置动画路径选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var path

```cangjie
public var path: ?String
```

**功能：** 设置动画路径。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var from

```cangjie
public var from: ?Float64
```

**功能：** 设置动画路径的起始位置。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var to

```cangjie
public var to: ?Float64
```

**功能：** 设置动画路径的结束位置。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var rotatable

```cangjie
public var rotatable: ?Bool
```

**功能：** 设置动画路径是否可旋转。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?String, ?Float64, ?Float64, ?Bool)

```cangjie
public init(path!: ?String, from!: ?Float64 = None, to!: ?Float64 = None, rotatable!: ?Bool = None)
```

**功能：** 构造一个MotionPathOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|?String|是|-|**命名参数。** 设置动画路径的起始位置。|
|from|?Float64|否|None|**命名参数。** 设置动画路径的起始位置。初始值为0.0。|
|to|?Float64|否|None|**命名参数。** 设置动画路径的结束位置。初始值为1.0。|
|rotatable|?Bool|否|None|**命名参数。** 设置动画路径是否可旋转。初始值为false。|