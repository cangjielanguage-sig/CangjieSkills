### class PopInfo

```cangjie
public class PopInfo {
    public let info: NavPathInfo
    public let result: String
}
```

**功能：** 表示弹出页面的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### let info

```cangjie
public let info: NavPathInfo
```

**功能：** 导航路径信息。

**类型：** [NavPathInfo](#class-navpathinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### let result

```cangjie
public let result: String
```

**功能：** 弹出操作的结果。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### enum BarStyle

```cangjie
public enum BarStyle <: Equatable<BarStyle> {
    | Standard
    | Stack
    | ...
}
```

**功能：** 标题栏或工具栏的布局样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BarStyle](#enum-barstyle)>

#### Stack

```cangjie
Stack
```

**功能：** 在此模式下，标题栏或工具栏在内容区域上层叠加布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Standard

```cangjie
Standard
```

**功能：** 在此模式下，标题栏或工具栏在内容区域上方布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(BarStyle)

```cangjie
public operator func !=(other: BarStyle): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarStyle](#enum-barstyle)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(BarStyle)

```cangjie
public operator func ==(other: BarStyle): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarStyle](#enum-barstyle)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|