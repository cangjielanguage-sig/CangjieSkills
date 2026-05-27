# Flex布局

> **说明：**
>
> 仅当父组件是 [Flex](./cj-row-column-stack-flex.md)、[Column](./cj-row-column-stack-column.md)、[Row](./cj-row-column-stack-row.md)、[GridRow](./cj-grid-layout-gridrow.md)（仅针对[alignSelf](./cj-universal-attribute-flexlayout.md#func-alignselfitemalign)）时生效。

## func flexBasis(Length)

```cangjie
public func flexBasis(value: Length): This
```

**功能：** 设置组件的基准尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---------| :--------- | :------- | :-------- | :--------------------------------------------------|
|value| [Length](./cj-common-types.md#interface-length) | 是 | - | 组件在父容器主轴方向上的基准尺寸。|

## func flexGrow(Float64)

```cangjie
public func flexGrow(value: Float64): This
```

**功能：** 设置组件在父容器的剩余空间所占比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---------| :--------- | :------- | :-------- | :--------------------------------------------------|
|value| Float64 | 是 | - | 父容器在主轴方向上的剩余空间分配给此属性所在组件的比例。<br>取值范围(0,+∞)，初始值：0.0。|

## func flexGrow(Int64)

```cangjie
public func flexGrow(value: Int64): This
```

**功能：** 设置组件在父容器的剩余空间所占比例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :--------- | :------- | :-------- | :--------------------------------------------------|
| value  | Int64 | 是 | - | 父容器在主轴方向上的剩余空间分配给此属性所在组件的比例。<br>取值范围(0,+∞)，初始值：0。|

## func flexShrink(Float64)

```cangjie
public func flexShrink(value: Float64): This
```

**功能：** 设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :--------- | :------- | :-------- | :--------------------------------------------------|
| value  | Float64 | 是 | - |父容器压缩尺寸分配给此属性所在组件的比例。<br> 父容器为[Column](./cj-row-column-stack-column.md)、[Row](./cj-row-column-stack-row.md)时，取值范围(0,+∞)，初始值为0.0。 <br>父容器为[Flex](./cj-row-column-stack-flex.md)时，初始值：1.0。<br>[constraintSize](./cj-universal-attribute-size.md#func-constraintsizelength-length-length-length)限制组件的尺寸范围，[Column](./cj-row-column-stack-column.md)和[Row](./cj-row-column-stack-row.md)即使设置了[constraintSize](./cj-universal-attribute-size.md#func-constraintsizelength-length-length-length)，在未设置主轴尺寸（[width](./cj-universal-attribute-size.md#func-widthlength)/[height](./cj-universal-attribute-size.md#func-heightlength)/[size](./cj-universal-attribute-size.md#func-sizelength-length)时仍遵守默认布局行为，在主轴上自适应子组件尺寸，此时flexShrink不生效。|

## func flexShrink(Int64)

```cangjie
public func flexShrink(value: Int64): This
```

**功能：** 设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :--------- | :------- | :-------- | :--------------------------------------------------|
| value  | Int64 | 是 | - | 父容器压缩尺寸分配给此属性所在组件的比例。<br> 父容器为Column、Row时，初始值为0。 <br>父容器为Flex时，初始值为1。|