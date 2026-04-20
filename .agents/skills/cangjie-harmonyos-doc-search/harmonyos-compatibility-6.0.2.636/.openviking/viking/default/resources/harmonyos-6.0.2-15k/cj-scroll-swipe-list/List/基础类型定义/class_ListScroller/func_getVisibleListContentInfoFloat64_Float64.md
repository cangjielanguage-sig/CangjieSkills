#### func getVisibleListContentInfo(Float64, Float64)

```cangjie
public func getVisibleListContentInfo(x: Float64, y: Float64): VisibleListContentInfo
```

**功能：** 根据坐标获取子组件的索引信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x轴坐标，单位为vp。|
|y|Float64|是|-|y轴坐标，单位为vp。|

**返回值：**

|类型|说明|
|:----|:----|
|[VisibleListContentInfo](#class-visiblelistcontentinfo)|入参坐标处的子组件的索引信息。|

> **说明：**
>
> * 入参坐标(x, y)的基准点是List组件的位置。
> * 如果该坐标位置处于ListItem范围内，且该ListItem父组件是List，则返回值对象成员index为该ListItem在List中的索引值，itemGroupArea返回ListItemGroupArea.UNDEFINED，itemIndexInGroup返回-1。
> * 如果该坐标位置处于ListItem范围内，且该ListItem父组件是ListItemGroup，则返回值对象成员index为该ListItemGroup在List中的索引值，itemGroupArea返回ListItemGroupArea.IN_LIST_ITEM_AREA，itemIndexInGroup返回该ListItem在ListItemGroup中的索引值。
> * 如果该坐标位置不处于ListItem范围内，但是处于ListItemGroup的header或者footer范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回-1。如果坐标位置处于header范围，itemGroupArea返回ListItemGroupArea.IN_HEADER_AREA。如果坐标位置处于footer范围，itemGroupArea返回ListItemGroupArea.IN_FOOTER_AREA。
> * 如果该坐标位置既不处于ListItem范围内，也不处于ListItemGroup的header或者footer范围内，但是处于ListItemGroup的范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回-1，itemGroupArea返回ListItemGroupArea.NONE。
> * 如果该坐标位置既不处于ListItem范围内，也不处于ListItemGroup的范围内，则返回值对象成员index为-1，itemGroupArea返回ListItemGroupArea.UNDEFINED，itemIndexInGroup返回-1。