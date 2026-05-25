## class ElementName

```cangjie
public class ElementName {
    public init(deviceId: String, bundleName: String, abilityName: String, moduleName: String)
    public init(deviceId: String, bundleName: String, abilityName: String)
}
```

**功能：** ElementName信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### prop abilityName

```cangjie
public prop abilityName: String
```

**功能：** Ability名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop bundleName

```cangjie
public prop bundleName: String
```

**功能：** 应用Bundle名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop deviceId

```cangjie
public prop deviceId: String
```

**功能：** 设备ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop moduleName

```cangjie
public prop moduleName: String
```

**功能：** Ability所属的HAP的模块名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String, String, String, String)

```cangjie
public init(deviceId: String, bundleName: String, abilityName: String, moduleName: String)
```

**功能：** 通过指定设备ID，应用Bundle名称，Ability名称，模块名称构造ElementName。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|设备ID。|
|bundleName|String|是|-|应用Bundle名称。|
|abilityName|String|是|-|Ability名称。|
|moduleName|String|是|-|Ability所属的HAP的模块名称。|

### init(String, String, String)

```cangjie
public init(deviceId: String, bundleName: String, abilityName: String)
```

**功能：** 通过指定设备ID，应用Bundle名称，Ability名称构造ElementName。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|设备ID。|
|bundleName|String|是|-|应用Bundle名称。|
|abilityName|String|是|-|Ability名称。|