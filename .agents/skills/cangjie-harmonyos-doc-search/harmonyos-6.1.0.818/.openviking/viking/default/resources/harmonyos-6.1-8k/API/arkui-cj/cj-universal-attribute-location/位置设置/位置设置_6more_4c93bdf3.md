# 位置设置

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

设置组件的位置、锚点和偏移量。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func position(?Length, ?Length)

```cangjie
func position(x!: ?Length, y!: ?Length): T
```

**功能：** 设置组件的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件的x坐标|
|y|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件的y坐标|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func markAnchor(?Length, ?Length)

```cangjie
func markAnchor(x!: ?Length, y!: ?Length): T
```

**功能：** 设置锚点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 锚点的x坐标|
|y|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 锚点的y坐标|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func offset(?Length, ?Length)

```cangjie
func offset(x!: ?Length, y!: ?Length): T
```

**功能：** 设置偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** x轴偏移量|
|y|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** y轴偏移量|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func alignRules(?AlignRuleOption)

```cangjie
func alignRules(value: ?AlignRuleOption): T
```

**功能：** 设置组件的对齐规则。

> **说明：**
>
> 仅当父容器为RelativeContainer时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[AlignRuleOption](./cj-common-types.md#class-alignruleoption)|是|-|对齐规则选项<br>初始值：AlignRuleOption()。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|