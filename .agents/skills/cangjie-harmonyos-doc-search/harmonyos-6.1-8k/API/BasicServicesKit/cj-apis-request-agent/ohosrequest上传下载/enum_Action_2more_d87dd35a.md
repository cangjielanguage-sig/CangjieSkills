## enum Action

```cangjie
public enum Action <: Equatable<Action> & ToString {
    | Download
    | Upload
    | ...
}
```

**功能：** 定义操作选项。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- Equatable\<Action>
- ToString

### Download

```cangjie
Download
```

**功能：** 表示下载任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Upload

```cangjie
Upload
```

**功能：** 表示上传任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func !=(Action)

```cangjie
public operator func !=(other: Action): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                   | 必填 | 默认值 | 说明           |
| :----- | :--------------------- | :--- | :----- | :------------- |
| other  | [Action](#enum-action) | 是   | -      | 另一个枚举值。 |

**返回值：**

| 类型 | 说明                                      |
| :--- | :---------------------------------------- |
| Bool | 两个枚举值不相等返回true，否则返回false。 |

### func ==(Action)

```cangjie
public operator func ==(other: Action): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                   | 必填 | 默认值 | 说明           |
| :----- | :--------------------- | :--- | :----- | :------------- |
| other  | [Action](#enum-action) | 是   | -      | 另一个枚举值。 |

**返回值：**

| 类型 | 说明                                    |
| :--- | :-------------------------------------- |
| Bool | 两个枚举值相等返回true，否则返回false。 |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                       |
| :----- | :------------------------- |
| String | 获取当前枚举的字符串表示。 |

## enum BroadcastEvent

```cangjie
public enum BroadcastEvent <: ToString {
    | Complete
    | ...
}
```

**功能：** 定义自定义系统事件。用户可以使用公共事件接口获取该事件。上传下载SA具有'ohos.permission.SEND_TASK_COMPLETE_EVENT' 该权限，用户可以配置事件的metadata 指向的二级配置文件来拦截其他事件发送者。

使用CommonEventData 类型传输公共事件相关数据。成员的内容填写和[CommonEventData介绍](./cj-apis-common_event_manager.md) 介绍的有所区别，其中CommonEventData.code 表示任务的状态，目前为0x40 COMPLETE或0x41 FAILED; CommonEventData.data 表示任务的taskId。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- ToString

### Complete

```cangjie
Complete
```

**功能：** 表示自定义系统事件完成。在任务结束后会触发该事件，根据任务的成功或失败，事件的code返回0x40或者0x41。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型   | 说明                   |
| :----- | :--------------------- |
| String | 当前枚举的字符串表示。 |