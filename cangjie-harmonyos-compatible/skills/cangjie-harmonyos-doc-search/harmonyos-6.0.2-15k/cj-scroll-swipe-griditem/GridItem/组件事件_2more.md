## 组件事件

### func onSelect((Bool) -> Unit)

```cangjie
public func onSelect(callback: (Bool) -> Unit): This
```

**功能：** GridItem元素被鼠标框选的状态改变时触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|GridItem元素被鼠标框选的状态改变时触发回调。 <br/> 参数一：进入鼠标框选范围即被选中返回true，&nbsp;移出鼠标框选范围即未被选中返回false。|

## 基础类型定义

### class GridItemOptions

```cangjie
public class GridItemOptions {
    public var style: GridItemStyle
    public init(style!: GridItemStyle = GridItemStyle.NONE)
}
```

**功能：** GridItem样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var style

```cangjie
public var style: GridItemStyle
```

**功能：** 设置GridItem样式。

**类型：** [GridItemStyle](cj-common-types.md#enum-griditemstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(GridItemStyle)

```cangjie
public init(style!: GridItemStyle = GridItemStyle.NONE)
```

**功能：** 创建一个GridItemOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[GridItemStyle](cj-common-types.md#enum-griditemstyle)|否|GridItemStyle.NONE| **命名参数。** 设置GridItem样式。<br/>初始值：GridItemStyle.NONE。<br/>设置为GridItemStyle.NONE时无样式。<br/>设置为GridItemStyle.PLAIN时，显示Hover、Press态样式。|