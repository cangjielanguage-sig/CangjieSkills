### enmu LocalizedBarrierDirection

```cangjie
public enum LocalizedBarrierDirection {
    | START
    | END
    | TOP
    | BOTTOM
}
```

**功能：** 定义支持镜像模式的屏障线的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### START

```cangjie
START
```

**功能：** 屏障在其所有[referencedId](#class-localizedbarrierstyle)的最左/右侧，LTR模式时为最左侧，RTL模式时为最右侧。

**起始版本：** 19

#### END

```cangjie
END
```

**功能：** 屏障在其所有[referencedId](#class-localizedbarrierstyle)的最左/右侧, LTR模式时为最右侧，RTL模式时为最左侧。

**起始版本：** 19

#### TOP

```cangjie
TOP
```

**功能：** 屏障在其所有[referencedId](#class-localizedbarrierstyle)的最上方。

**起始版本：** 19

#### BOTTOM

```cangjie
BOTTOM
```

**功能：** 屏障在其所有[referencedId](#class-localizedbarrierstyle)的最下方。

**起始版本：** 19