## class LocationCommand

```cangjie
public class LocationCommand {
    public var scenario: LocationRequestScenario
    public var command: String
    public init(scenario: LocationRequestScenario, command: String)
}
```

**功能：** 扩展命令参数。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### var command

```cangjie
public var command: String
```

**功能：** 扩展命令字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var scenario

```cangjie
public var scenario: LocationRequestScenario
```

**功能：** 表示定位场景。

**类型：** [LocationRequestScenario](#enum-locationrequestscenario)

**读写能力：** 可读写

**起始版本：** 19

### init(LocationRequestScenario, String)

```cangjie
public init(scenario: LocationRequestScenario, command: String)
```

**功能：** 构造LocationCommand对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scenario|[LocationRequestScenario](#enum-locationrequestscenario)|是|-|表示定位场景。|
|command|String|是|-|扩展命令字符串。|