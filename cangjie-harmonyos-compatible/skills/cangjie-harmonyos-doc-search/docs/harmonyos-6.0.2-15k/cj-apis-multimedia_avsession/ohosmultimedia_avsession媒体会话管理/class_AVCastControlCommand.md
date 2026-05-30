## class AVCastControlCommand

```cangjie
public class AVCastControlCommand {
    public AVCastControlCommand(
        public var command: AVCastControlCommandType
    )
}
```

**功能：** 投播控制器接受的命令的对象描述。

**系统能力：**  SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### prop parameter

```cangjie
public mut prop parameter: ?AVCastControlCommandParameterType
```

**功能：** 命令对应参数。

**类型：** ?[AVCastControlCommandParameterType](#enum-avcastcontrolcommandparametertype)

**读写能力：** 可读写

**起始版本：** 19

### var command

```cangjie
public var command: AVCastControlCommandType
```

**功能：** 命令。

**类型：** [AVCastControlCommandType](#enum-avcastcontrolcommandtype)

**读写能力：** 可读写

**起始版本：** 19

### AVCastControlCommand(AVCastControlCommandType)

```cangjie
public AVCastControlCommand(
    public var command: AVCastControlCommandType
)
```

**功能：** AVCastControlCommand构造函数。

**系统能力：**  SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|command|[AVCastControlCommandType](#enum-avcastcontrolcommandtype)|是|-|命令。|