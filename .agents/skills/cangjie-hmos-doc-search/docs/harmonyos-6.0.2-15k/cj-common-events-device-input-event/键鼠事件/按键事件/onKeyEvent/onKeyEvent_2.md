Divider()
            Text(this.columnText).fontColor(Color.RED)
        }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center).onKeyEvent(
            {
                event =>
                if (event.keyType.getValue() == KeyType.Down.getValue()) {
                    this.columnType = 'Down'
                }
                if (event.keyType.getValue() == KeyType.Up.getValue()) {
                    this.columnType = 'Up'
                }
                this.columnText = """
                Column:
                KeyType: ${this.columnType}
                KeyCode: ${event.keyCode.toString()}
                KeyText: ${event.keyText.toString()}
            """
            }
        )
    }
}
```

![KeyEventStop](./figures/KeyEventStop.gif)