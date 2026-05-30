## func margin(Length)

```cangjie
public func margin(value: Length): This
```

**功能：** 设置外边距属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value| [Length](./cj-common-types.md#interface-length) | 是  | - | 组件的外边距，四个方向内边距同时生效。<br/> 单位：vp|

## func margin(Length, Length, Length, Length)

```cangjie
public func margin(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp): This
```

**功能：** 设置外边距属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top       | [Length](./cj-common-types.md#interface-length)  | 否  | 0.vp | **命名参数。**  上内边距，组件顶部距组件外元素的尺寸。|
| right     | [Length](./cj-common-types.md#interface-length)  | 否  | 0.vp | **命名参数。**  右内边距，组件右边界距组件外元素的尺寸。|
| bottom    | [Length](./cj-common-types.md#interface-length)  | 否  | 0.vp | **命名参数。**  下内边距，组件底部距组件外元素的尺寸。|
| left      | [Length](./cj-common-types.md#interface-length)  | 否  | 0.vp | **命名参数。**  左内边距，组件左边界距组件外元素的尺寸。|

## func layoutWeight(Int32)

```cangjie
public func layoutWeight(value: Int32): This
```

**功能：** 设置组件的布局权重，使用该属性的组件在父容器（[Row](./cj-common-types.md#row)/[Column](./cj-common-types.md#column)/[Flex](./cj-row-column-stack-flex.md#flex)）的主轴方向按照权重分配尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value     | Int32  | 是  | - | 父容器尺寸确定时，设置了layoutWeight属性的子元素与兄弟元素占主轴尺寸按照权重进行分配，忽略元素本身尺寸设置，表示自适应占满剩余空间。</br>**说明：** 仅在[Row](./cj-common-types.md#row)/[Column](./cj-common-types.md#column)/[Flex](./cj-row-column-stack-flex.md#flex)布局中生效。可选值为大于等于0的数字，或者可以转换为数字的字符串。如果容器中有子元素设置了layoutWeight属性，且设置的属性值大于0，则所有子元素不会再基于flexShrink和flexGrow布局。|