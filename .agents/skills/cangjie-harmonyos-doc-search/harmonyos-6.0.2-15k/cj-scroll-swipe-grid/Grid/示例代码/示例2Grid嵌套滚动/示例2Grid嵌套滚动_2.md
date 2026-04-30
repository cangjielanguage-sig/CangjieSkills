Row() {
                Text("Top").width(30).height(30).borderRadius(50)
            }.padding(5).borderRadius(50).backgroundColor(0xffffff).shadow(radius: 10, color: Color(0x909399),
                offsetX: 1, offsetY: 1).margin(right: 22, bottom: 15).onClick(
                {
                    event =>
                    this.scroller.scrollTo(xOffset: 0, yOffset: 0)
                    this.gridScroller.scrollTo(xOffset: 0, yOffset: 0)
                }
            )
        }.align(Alignment.BottomEnd)
    }
}
```

![griditem](figures/grid2.gif)