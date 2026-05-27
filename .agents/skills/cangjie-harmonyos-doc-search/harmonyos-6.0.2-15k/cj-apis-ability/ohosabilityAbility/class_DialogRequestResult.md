## class DialogRequestResult

```cangjie
public class DialogRequestResult {}
```

**功能：** Diaglog请求结果对象，在调用requestDialogService时返回此对象表明此次申请的结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### var resultCode

```cangjie
public var resultCode: ResultCode
```

**功能：** 此次请求的结果码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [ResultCode](#enum-resultcode)

**读写能力：** 可读写

**起始版本：** 12

### var want

```cangjie
public var want:?Want
```

**功能：** 请求的want信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?[Want](#class-want)

**读写能力：** 可读写

**起始版本：** 12