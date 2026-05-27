## class ForEach

```cangjie
public class ForEach <: ComponentRender {
    public init(subcomponent: () -> Unit)
}
```

**功能：** ForEach组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ComponentRender](#interface-componentrender)

### init(() -> Unit)

```cangjie
public init(subcomponent: () -> Unit)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subcomponent|()->Unit|是|-|子组件。|

### static func create\<T>(Int64, CustomView, ArrayLike\<T>, ItemGenFuncType\<T>, KeyGenFuncType\<T>)

```cangjie
public static func create<T>(viewID: Int64, parentView: CustomView, dataSource: ArrayLike<T>,
    itemGeneratorFunc!: ItemGenFuncType<T>, keyGeneratorFunc!: KeyGenFuncType<T> = { realData: T, idx: Int64 =>
        match(realData) {
            case realDataStr: ToString => realDataStr.toString()
            case _ => idx.toString()
        }
    }): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|viewID|Int64|是|-|组件id。|
|parentView|[CustomView](#class-customview)|是|-|父组件。|
|dataSource|[ArrayLike](#interface-arraylike)\<T>|是|-|数据源。|
|itemGeneratorFunc|ItemGenFuncType\<T>|是|-| **命名参数。** 组件生成函数。|
|keyGeneratorFunc|KeyGenFuncType\<T>|否|{ realData: T, idx: Int64 => match(realData) {<br>case realDataStr: ToString => realDataStr.toString()<br>case \_ => idx.toString()<br>} }| **命名参数。** 键值生成函数。|

> **说明：**
>
> - ItemGenFuncType\<T>是(T, Int64) -> Unit的别名。
> - KeyGenFuncType\<T>是(T, Int64) -> Unit的别名。

### static func create()

```cangjie
public static func create()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func genChild()

```cangjie
public func genChild(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func initial()

```cangjie
public func initial(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func pop()

```cangjie
public func pop(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func update()

```cangjie
public func update(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12