### class FlexSpaceOptions

```cangjie
public class FlexSpaceOptions {
    public var mainSpace: Length
    public var crossSpace: Length
    public FlexSpaceOptions(mainSpace!: Length = 0.px, crossSpace!: Length = 0.px)
}
```

**功能：** 所有子组件在Flex容器主轴或交叉轴的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var crossSpace

```cangjie
public var crossSpace: Length
```

**功能：** Flex容器交叉轴上的space。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var mainSpace

```cangjie
public var mainSpace: Length
```

**功能：** Flex容器主轴上的space。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### FlexSpaceOptions(Length, Length)

```cangjie
public FlexSpaceOptions(mainSpace!: Length = 0.px, crossSpace!: Length = 0.px)
```

**功能：** 创建一个FlexSpaceOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mainSpace|[Length](cj-common-types.md#interface-length)|否|0.px| **命名参数。** Flex容器主轴上的space。|
|crossSpace|[Length](cj-common-types.md#interface-length)|否|0.px| **命名参数。** Flex容器交叉轴上的space。|