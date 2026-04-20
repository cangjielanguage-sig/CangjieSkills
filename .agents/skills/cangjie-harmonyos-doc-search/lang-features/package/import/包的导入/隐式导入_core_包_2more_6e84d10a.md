## 隐式导入 core 包

诸如 `String`、`Range` 等类型能直接使用，并不是因为这些类型是内置类型，而是因为编译器会自动为源码隐式的导入 `core` 包中所有的 `public` 修饰的声明。

## 使用 `import as` 对导入的名字重命名

不同包的名字空间是分隔的，因此在不同的包之间可能存在同名的顶层声明。在导入不同包的同名顶层声明时，支持使用 `import packageName.name as newName` 的方式进行重命名来避免冲突。没有名字冲突的情况下仍然可以通过 `import as` 来重命名导入的内容。`import as` 具有如下规则：

- 使用 `import as` 对导入的声明进行重命名后，当前包只能使用重命名后的新名字，原名无法使用。
- 如果重命名后的名字与当前包顶层作用域的其他名字存在冲突，且这些名字对应的声明均为函数类型，则参与函数重载，否则报重定义的错误。
- 支持 `import pkg as newPkgName` 的形式对包名进行重命名，以解决不同模块中同名包的命名冲突问题。
    <!-- compile.error -import3-->
    <!-- cfg="-p p1 --output-type=staticlib" -->

    ```cangjie
    // a.cj
    package p1
    public func f1() {}
    ```

    <!-- compile.error -import3-->
    <!-- cfg="-p p2 --output-type=staticlib" -->

    ```cangjie
    // d.cj
    package p2
    public func f3() {}
    ```

    <!-- compile.error -import3-->
    <!-- cfg="-p p1 --output-type=staticlib" -->

    ```cangjie
    // b.cj
    package p1
    public func f2() {}
    ```

    <!-- compile.error -import3-->
    <!-- cfg="-p pkgc --output-type=staticlib" -->

    ```cangjie
    // c.cj
    package pkgc
    public func f1() {}
    ```

    <!-- compile.error -import3-->
    <!-- cfg="libp1.a libpkgc.a libp1.a" -->

    ```cangjie
    // main.cj
    import p1 as A
    import p1 as B
    import p2.f3 as f  // OK
    import pkgc.f1 as a
    import pkgc.f1 as b // OK

    func f(a: Int32) {}

    main() {
        A.f1()  // OK, package name conflict is resolved by renaming package name.
        B.f2()  // OK, package name conflict is resolved by renaming package name.
        p1.f1() // Error, the original package name cannot be used.
        a()     // OK.
        b()     // OK.
        pkgc.f1()    // Error, the original name cannot be used.
    }
    ```

- 如果没有对导入的存在冲突的名字进行重命名，在 `import` 语句处不报错；在使用处，会因为无法导入唯一的名字而报错。这种情况可以通过 `import as` 定义别名或者 `import fullPackageName` 导入包作为命名空间。

    ```cangjie
    // a.cj
    package p1
    public class C {}

    // b.cj
    package p2
    public class C {}

    // main1.cj
    package pkga
    import p1.C
    import p2.C

    main() {
        let _ = C() // Error
    }

    // main2.cj
    package pkgb
    import p1.C as C1
    import p2.C as C2

    main() {
        let _ = C1() // OK
        let _ = C2() // OK
    }

    // main3.cj
    package pkgc
    import p1
    import p2

    main() {
        let _ = p1.C() // OK
        let _ = p2.C() // OK
    }
    ```