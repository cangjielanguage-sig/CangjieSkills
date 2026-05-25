## class Margin

```cangjie
public class Margin {
    public init(top!: ?Length = None, right!: ?Length = None, bottom!: ?Length = None, left!: ?Length = None)
}
```

**功能：** 外边距类型，用于描述组件不同方向的外边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length, ?Length)

```cangjie
public init(top!: ?Length = None, right!: ?Length = None, bottom!: ?Length = None, left!: ?Length = None)
```

**功能：** 初始化外边距类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 上外边距，组件顶部距组件外元素的尺寸。初始值为0.vp。|
|right|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 右外边距，组件右边界距组件外元素的尺寸。初始值为0.vp。|
|bottom|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 下外边距，组件底部距组件外元素的尺寸。初始值为0.vp。|
|left|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 左外边距，组件左边界距组件外元素的尺寸。初始值为0.vp。|