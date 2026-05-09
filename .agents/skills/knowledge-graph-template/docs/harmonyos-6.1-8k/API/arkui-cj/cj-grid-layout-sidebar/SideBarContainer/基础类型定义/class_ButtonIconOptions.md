### class ButtonIconOptions

```cangjie
public class ButtonIconOptions {
    public var shown: ?ResourceStr
    public var hidden: ?ResourceStr
    public var switching: ?ResourceStr
    public init(shown!: ?ResourceStr, hidden!: ?ResourceStr, switching!: ?ResourceStr = None)
}
```

**功能：** 表示图标类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var shown

```cangjie
public var shown: ?ResourceStr
```

**功能：** 侧边栏显示时控制按钮的图标。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var hidden

```cangjie
public var hidden: ?ResourceStr
```

**功能：** 侧边栏隐藏时控制按钮的图标。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var switching

```cangjie
public var switching: ?ResourceStr
```

**功能：** 侧边栏显示和隐藏状态切换时控制按钮的图标。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?ResourceStr, ?ResourceStr, ?ResourceStr)

```cangjie
public init(shown!: ?ResourceStr, hidden!: ?ResourceStr, switching!: ?ResourceStr = None)
```

**功能：** 构造 ButtonIconOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shown|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 设置侧边栏显示时控制按钮的图标。|
|hidden|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 设置侧边栏隐藏时控制按钮的图标。|
|switching|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 设置侧边栏显示和隐藏状态切换时控制按钮的图标。<br>初始值：""|