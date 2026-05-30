## class OpenLinkOptions

```cangjie
public class OpenLinkOptions {
    public OpenLinkOptions(
        public let appLinkingOnly!: Bool = false,
        public let parameters!: String = ""
    )
}
```

**功能：** 用于标识是否仅打开AppLinking和传递键值对可选参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let appLinkingOnly

```cangjie
public let appLinkingOnly: Bool = false
```

**功能：** 表示是否必须以AppLinking的方式启动Ability：

- 取值为true时，如果不存在与AppLinking相匹配的Ability，直接返回。

- 取值为false时，如果不存在与AppLinking相匹配的Ability，AppLinking会退化为DeepLink。默认值为false。

aa命令隐式拉起Ability时可以通过设置"--pb appLinkingOnly true/false"以AppLinking的方式进行启动。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let parameters

```cangjie
public let parameters: String = ""
```

**功能：** 表示WantParams参数。具体使用规则请参考[Want](#class-want)中的parameters属性。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### OpenLinkOptions(Bool, String)

```cangjie
public OpenLinkOptions(
    public let appLinkingOnly!: Bool = false,
    public let parameters!: String = ""
)
```

**功能：** OpenLinkOptions主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appLinkingOnly|Bool|否|false| **命名参数。** 表示是否必须以AppLinking的方式启动UIAbility。|
|parameters|String|否|""| **命名参数。** 表示WantParams参数|