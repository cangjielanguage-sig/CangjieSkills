### class NavPathInfo

```cangjie
public class NavPathInfo {
    public var name: ?String
    public var param: ?String
    public var onPop: ?Callback<PopInfo, Unit> = None
    public init(name!: ?String, param!: ?String, onPop!: ?Callback<PopInfo, Unit> = None)
}
```

**功能：** 表示NavDestination的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var name

```cangjie
public var name: ?String
```

**功能：** 导航目标页面的名称。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var onPop

```cangjie
public var onPop: ?Callback<PopInfo, Unit> = None
```

**功能：** 导航目标页面触发pop时的回调函数。

**类型：** ?[Callback](./cj-common-types.md#type-callbackt-v)\<[PopInfo](#class-popinfo), Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var param

```cangjie
public var param: ?String
```

**功能：** 导航目标页面的详细参数。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?String, ?String, ?Callback\<PopInfo, Unit>)

```cangjie
public init(name!: ?String, param!: ?String, onPop!: ?Callback<PopInfo, Unit> = None)
```

**功能：** NavPathInfo的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|?String|是|-|**命名参数。** NavDestination的名称。初始值：""。|
|param|?String|是|-|**命名参数。** NavDestination的详细参数。初始值：""。|
|onPop|?[Callback](./cj-common-types.md#type-callbackt-v)\<[PopInfo](#class-popinfo), Unit>|否|None|**命名参数。**  NavDestination页面触发pop时的回调函数。|