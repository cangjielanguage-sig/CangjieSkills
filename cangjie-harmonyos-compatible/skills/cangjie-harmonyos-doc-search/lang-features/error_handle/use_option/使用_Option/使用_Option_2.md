```cangjie
    main() {
        let a = Some(1)
        let b: ?Int64 = None
        let r1 = a.getOrThrow()
        println(r1)
        try {
            let r2 = b.getOrThrow()
        } catch (e: NoneValueException) {
            println("b is None")
        }
    }
    ```

   上述代码的执行结果为：

    ```text
    1
    b is None
    ```