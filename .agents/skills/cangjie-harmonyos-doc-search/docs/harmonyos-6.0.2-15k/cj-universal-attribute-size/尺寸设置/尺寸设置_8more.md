# 尺寸设置

设置组件的宽高、边距。

## func width(Length)

```cangjie
public func width(value: Length): This
```

**功能：** 设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会画出父组件的范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|   value   | [Length](cj-common-types.md#interface-length) | 是  | \-  | 组件宽度。<br/> 单位：vp。|

## func width\<T>(Option\<T>)

```cangjie
public func width<T>(value: Option<T>): This
```

**功能：** 设置组件自身的宽度，参数值为None时使用元素自身内容需要的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|   value   | Option\<T> | 是  | \-  | 组件宽度。<br/>T为Int64、Float64、Length、AppResource类型。|

## func height(Length)

```cangjie
public func height(value: Length): This
```

**功能：** 设置组件自身的高度，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会画出父组件的范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|   value   | [Length](cj-common-types.md#interface-length) | 是  | -  | 组件高度。<br/> 单位：vp。|

## func height\<T>(Option\<T>)

```cangjie
public func height<T>(value: Option<T>): This
```

**功能：** 设置组件自身的高度，参数值为None时使用元素自身内容需要的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|   value   | Option\<T> | 是  | \-  | 组件高度。<br/>T为Int64、Float64、Length、AppResource类型。|

## func size(Length, Length)

```cangjie
public func size(width!: Length, height!: Length): This
```

**功能：** 设置组件的高宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称|类型|必填|默认值|说明|
|:---|:---|:--- |:---|:---|
| width       | [Length](./cj-common-types.md#interface-length)      | 是  | \-  | **命名参数。**  组件宽度。<br/> 单位：vp。|
| height      | [Length](./cj-common-types.md#interface-length)      | 是  | \-  | **命名参数。**  组件高度。<br/> 单位：vp。|

## func padding(Length)

```cangjie
public func padding(value: Length): This
```

**功能：** 设置内边距属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value     | [Length](./cj-common-types.md#interface-length)  | 是  | - | 组件的内边距，四个方向内边距同时生效。<br/> 单位：vp。|

## func padding(Length, Length, Length, Length)

```cangjie
public func padding(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp): This
```

**功能：** 设置内边距属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top       | [Length](./cj-common-types.md#interface-length)  | 否  |0.vp| **命名参数。**  上内边距，组件内元素距组件顶部的尺寸。</br>初始值： 0.vp。|
| right     | [Length](./cj-common-types.md#interface-length)  | 否  |0.vp| **命名参数。**  右内边距，组件内元素距组件右边界的尺寸。</br>初始值： 0.vp。|
| bottom    | [Length](./cj-common-types.md#interface-length)  | 否  |0.vp| **命名参数。**  下内边距，组件内元素距组件底部的尺寸。</br>初始值： 0.vp。|
| left      | [Length](./cj-common-types.md#interface-length)  | 否  |0.vp| **命名参数。**  左内边距，组件内元素距组件左边界的尺寸。</br>初始值： 0.vp。|

> **说明：**
>
> padding设置百分比时，上下左右内边距均以父容器的width作为基础值。