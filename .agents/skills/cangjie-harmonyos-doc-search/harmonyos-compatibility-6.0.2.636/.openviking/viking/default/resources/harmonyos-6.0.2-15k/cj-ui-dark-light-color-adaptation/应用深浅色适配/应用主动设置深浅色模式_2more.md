## 应用主动设置深浅色模式

应用默认配置为跟随系统切换深浅色模式，如不希望应用跟随系统深浅色模式变化，可主动设置应用的深浅色风格。设置后，应用的深浅色模式固定，不会随系统改变。

```cangjie
public override func onCreate(): Unit {
    Hilog.info(0x0000, 'testTag', 'Ability onCreate');
    this.context.getApplicationContext().setColorMode(ConfigurationColorMode.COLOR_MODE_LIGHT)
}
```

## 系统默认判断规则

1. 如果应用调用上述setColorMode接口主动设置了深浅色，则以接口效果优先。

2. 应用没有调用setColorMode接口时：

    - 如果应用工程dark目录下有深色资源，则系统组件在深色模式下会自动切换成为深色。

    - 如果应用工程dark目录下没有任何深色资源，则系统组件在深色模式下仍会保持浅色体验。

        ![darkDir](./figures/darkDir.png)

如果应用全部都是由系统组件/系统颜色开发，且想要跟随系统切换深浅色模式时，请参考以下示例修改代码来保证应用体验。

```cangjie
public override func onCreate(): Unit {
    this.context.getApplicationContext().setColorMode(ConfigurationColorMode.COLOR_MODE_NOT_SET)
}
```