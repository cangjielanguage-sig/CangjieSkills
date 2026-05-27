Row {
                    Flex(FlexParams(justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center)) {
                        Text("borderImageFill:${this.FillValue} ")
                        Toggle(ToggleType.SwitchType, isOn: this.FillValue).selectedColor(0x39a2db).switchPointColor(
                            0xe5ffffff).onChange(
                            {
                                isOn: Bool =>
                                this.FillValue = !this.FillValue
                                nativeLog("Component status: ${isOn}")
                            }
                        )
                    }
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

![border_image](./figures/border_image3.png)