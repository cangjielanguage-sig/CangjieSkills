## enum CompositeOperation

```cangjie
public enum CompositeOperation {
    | SourceOver
    | SourceAtop
    | SourceIn
    | SourceOut
    | DestinationOver
    | DestinationAtop
    | DestinationIn
    | DestinationOut
    | Lighter
    | Copy
    | Xor
}
```

**功能：** 设置合成操作的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### copy

```cangjie
copy
```

**功能：** 显示新绘制内容而忽略现有绘制内容。

**起始版本：** 12

### destination-atop

```cangjie
destination-atop
```

**功能：** 在新绘制内容顶部显示现有绘制内容。

**起始版本：** 12

### destination-in

```cangjie
destination-in
```

**功能：** 在新绘制内容中显示现有绘制内容。

**起始版本：** 12

### destination-out

```cangjie
destination-out
```

**功能：** 在新绘制内容外显示现有绘制内容。

**起始版本：** 12

### destination-over

```cangjie
destination-over
```

**功能：** 在新绘制内容上方显示现有绘制内容。

**起始版本：** 12

### lighter

```cangjie
lighter
```

**功能：** 显示新绘制内容和现有绘制内容。

**起始版本：** 12

### source-atop

```cangjie
source-atop
```

**功能：** 在现有绘制内容顶部显示新绘制内容。

**起始版本：** 12

### source-in

```cangjie
source-in
```

**功能：** 在现有绘制内容中显示新绘制内容。

**起始版本：** 12

### source-out

```cangjie
source-out
```

**功能：** 在现有绘制内容之外显示新绘制内容。

**起始版本：** 12

### source-over

```cangjie
source-over
```

**功能：** 在现有绘制内容上显示新绘制内容，属于默认值。

**起始版本：** 12

### xor

```cangjie
xor
```

**功能：** 使用异或操作对新绘制内容与现有绘制内容进行融合。

**起始版本：** 12