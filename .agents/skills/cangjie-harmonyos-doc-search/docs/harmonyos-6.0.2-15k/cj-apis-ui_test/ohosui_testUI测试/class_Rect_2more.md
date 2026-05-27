## class Rect

```cangjie
public class Rect {
    public Rect(
        public let left: IntNative,
        public let top: IntNative,
        public let right: IntNative,
        public let bottom: IntNative
    )
}
```

**功能：** 控件的边框信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### let bottom

```cangjie
public let bottom: IntNative
```

**功能：** 控件边框的右下角的Y坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### let left

```cangjie
public let left: IntNative
```

**功能：** 控件边框的左上角的X坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### let right

```cangjie
public let right: IntNative
```

**功能：** 控件边框的右下角的X坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### let top

```cangjie
public let top: IntNative
```

**功能：** 控件边框的左上角的Y坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### Rect(IntNative, IntNative, IntNative, IntNative)

```cangjie
public Rect(
    public let left: IntNative,
    public let top: IntNative,
    public let right: IntNative,
    public let bottom: IntNative
)
```

**功能：** 创建[Rect](#class-rect)实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|IntNative|是|-|控件边框的左上角的X坐标。|
|top|IntNative|是|-|控件边框的左上角的Y坐标。|
|right|IntNative|是|-|控件边框的右下角的X坐标。|
|bottom|IntNative|是|-|控件边框的右下角的Y坐标。|

## class TestRunner

**功能：** 提供了框架测试的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### static func registerCreator(String, () -> TestRunner)

```cangjie
public static func registerCreator(name: String, creator: () -> TestRunner): Unit
```

**功能：** 注册构建[TestRunner](#class-testrunner)对象的函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| name | String | 是 | \- | 构建函数标识。 |
| creator | () -> [TestRunner](#class-testrunner) | 是 | \- | 构建[TestRunner](#class-testrunner)对象的函数。 |

### func onRun()

```cangjie
public open func onRun(): Unit
```

**功能：** 为运行测试用例准备单元测试环境。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func onPrepare()

```cangjie
public open func onPrepare(): Unit
```

**功能：** 运行测试用例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12