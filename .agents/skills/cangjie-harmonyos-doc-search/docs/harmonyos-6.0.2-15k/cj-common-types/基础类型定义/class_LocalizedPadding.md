## class LocalizedPadding

```cangjie
public class LocalizedPadding {
    public let top: Length
    public let end: Length
    public let bottom: Length
    public let start: Length
    public LocalizedPadding(
        top!: Length = 17.0.vp,
        end!: Length = 8.0.vp,
        bottom!: Length = 18.0.vp,
        start!: Length = 8.0.vp
    )
}
```

**功能：** 内边距类型，用于描述组件不同方向的内边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let bottom

```cangjie
public let bottom: Length
```

**功能：** 下内边距，组件内元素距组件底部的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let end

```cangjie
public let end: Length
```

**功能：** 右内边距，组件内元素距组件右边界的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let start

```cangjie
public let start: Length
```

**功能：** 左内边距，组件内元素距组件左边界的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let top

```cangjie
public let top: Length
```

**功能：** 上内边距，组件内元素距组件顶部的尺寸。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### LocalizedPadding(Length, Length, Length, Length)

```cangjie
public LocalizedPadding(
    top!: Length = 17.0.vp,
    end!: Length = 8.0.vp,
    bottom!: Length = 18.0.vp,
    start!: Length = 8.0.vp
)
```

**功能：** 构造一个LocalizedPadding对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[Length](cj-common-types.md#interface-length)|否|17.0.vp| **命名参数。** 上内边距，组件内元素距组件顶部的尺寸。|
|end|[Length](cj-common-types.md#interface-length)|否|8.0.vp| **命名参数。** 右内边距，组件内元素距组件右边界的尺寸。从右至左显示语言模式下为左内边距，组件内元素距组件左边界的尺寸。|
|bottom|[Length](cj-common-types.md#interface-length)|否|18.0.vp| **命名参数。** 下内边距，组件内元素距组件底部的尺寸。|
|start|[Length](cj-common-types.md#interface-length)|否|8.0.vp| **命名参数。** 左内边距，组件内元素距组件左边界的尺寸。从右至左显示语言模式下为右内边距，组件内元素距组件右边界的尺寸。|