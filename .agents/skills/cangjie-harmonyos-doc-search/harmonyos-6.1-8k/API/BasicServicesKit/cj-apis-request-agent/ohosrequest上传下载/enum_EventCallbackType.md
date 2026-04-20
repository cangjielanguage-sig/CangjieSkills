## enum EventCallbackType

```cangjie
public enum EventCallbackType <: Equatable<EventCallbackType> & Hashable & ToString {
    | Progress
    | Completed
    | Failed
    | Pause
    | Resume
    | Remove
    | Response
    | ...
}
```

**功能：** 订阅事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**父类型：**

- Equatable\<EventCallbackType>
- Hashable
- ToString

### Completed

```cangjie
Completed
```

**功能：** 表示任务完成的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Failed

```cangjie
Failed
```

**功能：** 表示任务失败的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Pause

```cangjie
Pause
```

**功能：** 表示任务暂停的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Progress

```cangjie
Progress
```

**功能：** 表示任务进度的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Remove

```cangjie
Remove
```

**功能：** 表示任务移除的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Response

```cangjie
Response
```

**功能：** 表示任务接收到响应的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### Resume

```cangjie
Resume
```

**功能：** 表示任务恢复的事件类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### func !=(EventCallbackType)

```cangjie
public operator func !=(other: EventCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                                         | 必填 | 默认值 | 说明     |
| :----- | :------------------------------------------- | :--- | :----- | :------- |
| other  | [EventCallbackType](#enum-eventcallbacktype) | 是   | -      | 另一个订阅事件类型。 |

**返回值：**

| 类型 | 说明                                      |
| :--- | :---------------------------------------- |
| Bool | 两个枚举值不相等返回true，否则返回false。 |

### func ==(EventCallbackType)

```cangjie
public operator func ==(other: EventCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                                         | 必填 | 默认值 | 说明     |
| :----- | :------------------------------------------- | :--- | :----- | :------- |
| other  | [EventCallbackType](#enum-eventcallbacktype) | 是   | -      | 另一个订阅事件类型。 |

**返回值：**

| 类型 | 说明                                    |
| :--- | :-------------------------------------- |
| Bool | 两个枚举值相等返回true，否则返回false。 |

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件的哈希值。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**返回值：**

| 类型  | 说明                   |
| :---- | :--------------------- |
| Int64 | 当前枚举的哈希值表示。 |

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