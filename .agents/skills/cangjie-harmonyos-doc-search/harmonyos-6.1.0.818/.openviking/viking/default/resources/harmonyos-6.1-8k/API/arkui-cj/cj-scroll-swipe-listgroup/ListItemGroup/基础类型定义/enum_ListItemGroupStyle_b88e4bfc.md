### enum ListItemGroupStyle

```cangjie
public enum ListItemGroupStyle <: Equatable<ListItemGroupStyle> {
    | None
    | Card
    | ...
}
```

**功能：** 设置List组件卡片样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：** Equatable\<[ListItemGroupStyle](#enum-listitemgroupstyle)>

#### Card

```cangjie
Card
```

**功能：** 显示默认卡片样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### None

```cangjie
None
```

**功能：** 无样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(ListItemGroupStyle)

```cangjie
public operator func !=(other: ListItemGroupStyle): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListItemGroupStyle](#enum-listitemgroupstyle)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(ListItemGroupStyle)

```cangjie
public operator func ==(other: ListItemGroupStyle): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListItemGroupStyle](#enum-listitemgroupstyle)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|