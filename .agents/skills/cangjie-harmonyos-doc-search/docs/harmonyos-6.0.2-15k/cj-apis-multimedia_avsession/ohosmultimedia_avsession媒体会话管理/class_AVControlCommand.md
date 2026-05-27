## class AVControlCommand

```cangjie
public class AVControlCommand {
    public AVControlCommand(
        public var command: AVControlCommandType
    )
}
```

**功能：** 会话接受的命令的对象描述。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### prop parameter

```cangjie
public mut prop parameter: ?AVControlCommandParameterType
```

**功能：** 命令对应参数。

**类型：** ?[AVControlCommandParameterType](#enum-avcontrolcommandparametertype)

**读写能力：** 可读写

**起始版本：** 19

### var command

```cangjie
public var command: AVControlCommandType
```

**功能：** 命令。

**类型：** [AVControlCommandType](#enum-avcontrolcommandtype)

**读写能力：** 可读写

**起始版本：** 19

### AVControlCommand(AVControlCommandType)

```cangjie
public AVControlCommand(
    public var command: AVControlCommandType
)
```

**功能：** [AVControlCommand](#class-avcontrolcommand)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|command|[AVControlCommandType](#enum-avcontrolcommandtype)|是|-|命令。|