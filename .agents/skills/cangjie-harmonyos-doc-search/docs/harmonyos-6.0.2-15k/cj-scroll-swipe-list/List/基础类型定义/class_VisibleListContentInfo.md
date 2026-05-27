### class VisibleListContentInfo

```cangjie
public class VisibleListContentInfo {
    public var index: Int32
    public var itemGroupArea: ListItemGroupArea
    public var itemIndexInGroup: Int32
    public VisibleListContentInfo(
        index!: Int32,
        itemGroupArea!: ListItemGroupArea = ListItemGroupArea.UNDEFINED,
        itemIndexInGroup!: Int32 = -1
    )
}
```

**功能：** 用于表示List可见内容区子组件的详细信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var index

```cangjie
public var index: Int32
```

**功能：** 表示ListItem或ListItemGroup在List中的索引值。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var itemGroupArea

```cangjie
public var itemGroupArea: ListItemGroupArea
```

**功能：** 表示处于ListItemGroup的哪一个区域。

**类型：** [ListItemGroupArea](cj-common-types.md#enum-listitemgrouparea)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var itemIndexInGroup

```cangjie
public var itemIndexInGroup: Int32
```

**功能：** 表示ListItem在ListItemGroup中的索引值。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### VisibleListContentInfo(Int32, ListItemGroupArea, Int32)

```cangjie
public VisibleListContentInfo(
    index!: Int32,
    itemGroupArea!: ListItemGroupArea = ListItemGroupArea.UNDEFINED,
    itemIndexInGroup!: Int32 = -1
)
```

**功能：** 创建一个VisibleListContentInfo类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-| **命名参数。** List显示区域内ListItem或ListItemGroup的索引值。|
|itemGroupArea|[ListItemGroupArea](cj-common-types.md#enum-ListItemGroupArea)|否|ListItemGroupArea.UNDEFINED| **命名参数。** 如果当前可视页面的上边或下边在某个ListItemGroup之中，将会显示它所处的位置。|
|itemIndexInGroup|Int32|否|- 1| **命名参数。** 如果当前可视页面的上边或下边在某个Group之中，将会显示Start或End的ListItem在Group中的索引。|