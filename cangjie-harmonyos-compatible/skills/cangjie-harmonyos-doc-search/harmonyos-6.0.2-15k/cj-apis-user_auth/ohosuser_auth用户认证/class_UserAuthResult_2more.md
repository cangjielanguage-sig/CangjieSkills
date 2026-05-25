## class UserAuthResult

```cangjie
public class UserAuthResult {}
```

**功能：** 用户认证结果。当认证结果为成功时，返回认证类型和认证通过的令牌信息。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### let authType

```cangjie
public let authType: ?UserAuthType
```

**功能：** 当认证结果为成功时，返回认证类型。

**类型：** ?[UserAuthType](#enum-userauthtype)

**读写能力：** 只读

**起始版本：** 19

### let enrolledState

```cangjie
public let enrolledState: ?EnrolledState
```

**功能：** 当认证结果为成功时，返回注册凭据的状态。

**类型：** ?[EnrolledState](#class-enrolledstate)

**读写能力：** 只读

**起始版本：** 19

### let result

```cangjie
public let result: Int32
```

**功能：** 用户认证结果。若成功返回SUCCESS，若失败返回相应错误码，参见[UserAuthResultCode](#class-userauthresultcode)。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let token

```cangjie
public let token: ?Array<Byte>
```

**功能：** 当认证结果为成功时，返回认证通过的令牌信息。

**类型：** ?Array\<Byte>

**读写能力：** 只读

**起始版本：** 19

## class WidgetParam

```cangjie
public class WidgetParam {
    public WidgetParam(
        public let title: String,
        public let navigationButtonText: ?String
    )
}
```

**功能：** 用户认证界面配置相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### let navigationButtonText

```cangjie
public let navigationButtonText: ?String
```

**功能：** 导航按键的说明文本，最大长度为60字符。仅在单指纹、单人脸场景下支持。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let title

```cangjie
public let title: String
```

**功能：** 用户认证界面的标题，最大长度为500字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### WidgetParam(String, ?String)

```cangjie
public WidgetParam(
    public let title: String,
    public let navigationButtonText: ?String
)
```

**功能：** 创建[WidgetParam](#class-widgetparam)实例。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|用户认证界面的标题，最大长度为500字符。|
|navigationButtonText|?String|是|-|导航按键的说明文本，最大长度为60字符。仅在单指纹、单人脸场景下支持。|