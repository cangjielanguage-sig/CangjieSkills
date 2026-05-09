# AlphabetIndexer

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

可以与容器组件联动，用于按逻辑结构快速定位容器显示区域的组件。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(Array\<String>, ?UInt32)

```cangjie
public init(arrayValue!: Array<String>, selected!: ?UInt32)
```

**功能：** 创建一个AlphabetIndexer组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arrayValue|Array\<String>|是|-|**命名参数。** 字符串数组，每个字符串代表一个索引项。|
|selected|?UInt32|是|-|**命名参数。** 初始选中项索引值，若超出索引值范围，则取默认值0。初始值: 0|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> - [width](./cj-universal-attribute-size.md#func-widthoptionlength)属性设置"auto"时表示自适应宽度，宽度会随索引项最大宽度变化。
> - [padding](./cj-universal-attribute-size.md#func-paddinglength)属性默认为4.vp。

通用事件：全部支持。