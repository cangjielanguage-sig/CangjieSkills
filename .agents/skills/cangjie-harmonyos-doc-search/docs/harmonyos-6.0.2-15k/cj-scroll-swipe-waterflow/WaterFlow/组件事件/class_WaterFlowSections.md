### class WaterFlowSections

```cangjie
public class WaterFlowSections {
    public init()
}
```

**功能：** 瀑布流分组信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init()

```cangjie
public init()
```

**功能：** 创建一个瀑布流分组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func length()

```cangjie
public func length(): UInt32
```

**功能：** 瀑布流中分组数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|瀑布流中分组数量。|

#### func push(SectionOptions)

```cangjie
public func push(section: SectionOptions): Bool
```

**功能：** 将指定分组添加到瀑布流末尾。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|section|[SectionOptions](#class-sectionoptions)|是|-|添加到瀑布流末尾的分组|

**返回值：**

|类型|说明|
|:----|:----|
|boolean|分组添加成功返回true，添加失败（新分组的itemsCount不是正整数）返回false。|

#### func splice(Int32, UInt32, Array\<SectionOptions>)

```cangjie
public func splice(start: Int32, deleteCount: UInt32, sections: Array<SectionOptions>): Bool
```

**功能：** 移除或者替换已存在的分组和/或添加新分组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-|从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。<br/>**说明：**<br/>1. 如果索引是负数，则从末尾开始计算，使用start + WaterFlowSections.length()。<br/>2. 如果 start < -WaterFlowSections.length()，则使用0。<br/>3. 如果 start >= WaterFlowSections.length()，则在最后添加新分组。|
|deleteCount|UInt32|是|-|表示要从start开始删除的分组数量。<br/>**说明：**<br/>1. 如果省略了deleteCount，或者其值大于或等于由start指定的位置到WaterFlowSections末尾的分组数量，那么从start到WaterFlowSections末尾的所有分组将被删除。<br/>2. 如果deleteCount是0或者负数，则不会删除任何分组。|
|sections|Array\<[SectionOptions](#class-sectionoptions)>|是|-|表示要从start开始加入的分组。如果不指定，splice()将只从瀑布流中删除分组。|

**返回值：**

|类型|说明|
|:----|:----|
|boolean|分组是否修改成功，要加入的分组中有任意分组的itemsCount不是正整数时返回false。|

#### func update(UInt32, SectionOptions)

```cangjie
public func update(sectionIndex: UInt32, section: SectionOptions): Bool
```

**功能：** 修改指定索引分组的配置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sectionIndex|UInt32|是|-|从0开始计算的索引，会转换为整数，表示要修改的分组的位置。<br/>**说明：**<br/> 1. 如果索引是负数，则从末尾开始计算，使用sectionIndex + WaterFlowSections.length()。<br/>2. 如果sectionIndex < -WaterFlowSections.length()，则使用0。<br/>3. 如果sectionIndex >= WaterFlowSections.length()，则在最后添加新分组。|
|section|[SectionOptions](#class-sectionoptions)|是|-|新的分组信息。|

**返回值：**

|类型|说明|
|:----|:----|
|boolean|分组是否更新成功，新分组的itemsCount不是正整数时返回false。|

#### func value()

```cangjie
public func value(): Array<SectionOptions>
```

**功能：** 获取瀑布流中所有分组配置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[SectionOptions](#class-sectionoptions)>|瀑布流中所有分组配置信息。|