### class DatePickerDialogOptions

```cangjie
public class DatePickerDialogOptions {
    public var start: ?DateTime
    public var end: ?DateTime
    public var selected: ?DateTime
    public var lunar: Bool = false
    public var showTime: Bool = false
    public var useMilitaryTime: Bool = false
    public var lunarSwitch: Bool = false
    public var disappearTextStyle: ?PickerTextStyle
    public var textStyle: ?PickerTextStyle
    public var selectedTextStyle: ?PickerTextStyle
    public var acceptButtonStyle: ?PickerDialogButtonStyle
    public var cancelButtonStyle: ?PickerDialogButtonStyle
    public var alignment: ?DialogAlignment
    public var offset: ?Offset = Offset(0.vp, 0.vp)
    public var maskRect: ?Rectangle
    public var onCancel: ?() -> Unit
    public var onDateAccept: ?(DateTime) -> Unit
    public var onDateChange: ?(DateTime) -> Unit
    public var backgroundColor: ResourceColor = Color.TRANSPARENT
    public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
    public var onDidAppear: ?() -> Unit
    public var onDidDisappear: ?() -> Unit
    public var onWillAppear: ?() -> Unit
    public var onWillDisappear: ?() -> Unit
    public var shadow: ?ShadowOptions
    public var dateTimeOptions: ?DateTimeOptions
    public init(
        start!: DateTime = DateTime.of(year: 1970, month: Month.of(1), dayOfMonth: 1),
        end!: DateTime = DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31),
        selected!: DateTime = DateTime.now(),
        lunar!: Bool = false,
        showTime!: Bool = false,
        useMilitaryTime!: Bool = false,
        lunarSwitch!: Bool = false,
        disappearTextStyle!: ?PickerTextStyle = None,
        textStyle!: ?PickerTextStyle = None,
        selectedTextStyle!: ?PickerTextStyle = None,
        acceptButtonStyle!: ?PickerDialogButtonStyle = None,
        cancelButtonStyle!: ?PickerDialogButtonStyle = None,
        alignment!: ?DialogAlignment = None,
        offset!: ?Offset = None,
        maskRect!: ?Rectangle = None,
        onCancel!: ?()->Unit = None,
        onDateAccept!: ?(DateTime)->Unit = None,
        onDateChange!: ?(DateTime)->Unit= None,
        backgroundColor!: ResourceColor = Color.TRANSPARENT,
        backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        onDidAppear!: ?()->Unit = None,
        onDidDisappear!: ?()->Unit = None,
        onWillAppear!: ?()->Unit = None,
        onWillDisappear!: ?()->Unit = None,
        shadow!: ?ShadowOptions = None,
        dateTimeOptions!: ?DateTimeOptions = None
        )
}
```

**功能：** 设置日期滑动选择器弹窗类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19