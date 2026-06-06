Row {
                                        }.width(12.vp).height(12.vp).margin(right: 15.vp).border(width: 2.vp,
                                            color: 0xcccccc).borderWidth(EdgeWidths(top: 2.vp, right: 2.vp)).rotate(45)
                                    }.borderRadius(15.vp).shadow(radius: 100, color: 0xededed).width(90.percent).
                                        alignItems(VerticalAlign.Center).padding(left: 15.vp, top: 15.vp, bottom: 15.vp).
                                        backgroundColor(Color.WHITE)
                                }.width(100.percent).margin(top: 12.vp)
                            },
                            keyGeneratorFunc: {item: String, index: Int64 => item.toString()}
                        )
                    }.width(100.percent).height(80.percent)
                }.width(100.percent).height(100.percent).backgroundColor(0xffffff).transition(
                    TransitionEffect.OPACITY.combine(TransitionEffect.translate(TranslateOptions(x: 100.percent))).
                    combine(TransitionEffect.scale(ScaleOptions(x: 0.95, y: 0.95))))
            }
        }
    }
}
```

![bindpopup](./figures/bindpopup1.gif)