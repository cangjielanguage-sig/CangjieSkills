### class FadingEdgeOptions

```cangjie
public class FadingEdgeOptions {
    public var fadingEdgeLength: ?Length
    public init(fadingEdgeLength!: ?Length = None)
}
```

**功能：** 提供自定义淡出边缘的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fadingEdgeLength

```cangjie
public var fadingEdgeLength: ?Length
```

**功能：** 自定义淡出边缘中的长度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length)

```cangjie
public init(fadingEdgeLength!: ?Length = None)
```

**功能：** 构造一个自定义淡出边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fadingEdgeLength|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 自定义淡出边缘中的长度。初始值：32.vp。|

### class ScrollEdgeOptions

```cangjie
public class ScrollEdgeOptions {
    public var velocity: ?Float32
    public init(velocity!: ?Float32 = None)
}
```

**功能：** 提供滚动边缘选项参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var velocity

```cangjie
public var velocity: ?Float32
```

**功能：** 滚动边缘选项中的速度。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Float32)

```cangjie
public init(velocity!: ?Float32 = None)
```

**功能：** 构造滚动边缘选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|velocity|?Float32|否|None|**命名参数。** 滚动边缘选项中的速度。初始值：0.0。|

### class ScrollToIndexOptions

```cangjie
public class ScrollToIndexOptions {
    public var extraOffset: ?Length
    public init(extraOffset!: ?Length = None)
}
```

**功能：** 提供滚动到索引选项参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var extraOffset

```cangjie
public var extraOffset: ?Length
```

**功能：** 滚动到索引选项中的额外偏移量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length)

```cangjie
public init(extraOffset!: ?Length = None)
```

**功能：** 构造滚动到索引选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|extraOffset|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 滚动到索引选项中的额外偏移量。初始值：0.vp。|