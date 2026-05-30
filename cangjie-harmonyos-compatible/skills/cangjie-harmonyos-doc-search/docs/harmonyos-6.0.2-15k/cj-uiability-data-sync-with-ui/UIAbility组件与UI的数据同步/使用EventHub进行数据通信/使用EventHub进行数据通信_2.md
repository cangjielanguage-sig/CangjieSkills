```cangjie
    import kit.AbilityKit.UIAbility

    class MainAbility <: UIAbility {
        // ...
        public override func onDestroy(): Unit {
            this.context.eventhub.get0("event0").off()
            this.context.eventhub.get1<String>("event1").off()
            this.context.eventhub.get2<String, String>("event2").off()
        }
    }
    ```