### class PopInfo

```cangjie
public class PopInfo {
    public var info: NavPathInfo
    public var result: String
    public init(
        info: NavPathInfo,
        result: String
    )
}
```

**功能：** 表示下一个页面返回的回调信息载体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### let info

```cangjie
public let info: NavPathInfo
```

**功能：** 表示页面触发返回时的当前页面信息，系统自动获取填入，无需开发者传入。

**类型：** [NavPathInfo](#class-navpathinfo)

**读写能力：** 可读写

**起始版本：** 20

#### let result

```cangjie
public let result: String
```

**功能：** 设置页面触发返回时的结果，开发者自定义对象。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

#### init(NavPathInfo, String)

```cangjie
public init(
    info: NavPathInfo,
    result: String
)
```

**功能：** 创建PopInfo。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-| 页面触发返回时的当前页面信息，系统自动获取填入，无需开发者传入。|
|result|String|是|-|页面触发返回时的结果，开发者自定义对象。|