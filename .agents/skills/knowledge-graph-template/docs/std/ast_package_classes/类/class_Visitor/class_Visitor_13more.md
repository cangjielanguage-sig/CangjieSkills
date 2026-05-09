## class Visitor

```cangjie
public abstract class Visitor
```

功能：一个抽象类，其内部默认定义了访问不同类型 AST 节点访问（`visit`）函数。

> **说明：**
>
> - `visit` 函数搭配 `traverse` 一起使用，可实现对节点的访问和修改, 所有 `visit` 函数都有默认为空的实现，可以按需实现需要的 `visit` 方法。
> - 该类需要被继承使用，并允许子类重新定义访问函数。

### func breakTraverse()

```cangjie
public func breakTraverse(): Unit
```

功能：用于重写 `visit` 函数中，通过调用该函数来终止继续遍历子节点的行为。

### func needBreakTraverse()

```cangjie
protected func needBreakTraverse(): Bool
```

功能：用于判断是否需要停止遍历。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### func visit(Annotation)

```cangjie
protected open func visit(_: Annotation): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [Annotation](ast_package_classes.md#class-annotation) - [Annotation](ast_package_classes.md#class-annotation) 类型的被遍历节点。

### func visit(Argument)

```cangjie
protected open func visit(_: Argument): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [Argument](ast_package_classes.md#class-argument) - [Argument](ast_package_classes.md#class-argument) 类型的被遍历节点。

### func visit(ArrayLiteral)

```cangjie
protected open func visit(_: ArrayLiteral): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [ArrayLiteral](ast_package_classes.md#class-arrayliteral) - [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 类型的被遍历节点。

### func visit(AsExpr)

```cangjie
protected open func visit(_: AsExpr): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [AsExpr](ast_package_classes.md#class-asexpr) - [AsExpr](ast_package_classes.md#class-asexpr) 类型的被遍历节点。

### func visit(AssignExpr)

```cangjie
protected open func visit(_: AssignExpr): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [AssignExpr](ast_package_classes.md#class-assignexpr) - [AssignExpr](ast_package_classes.md#class-assignexpr) 类型的被遍历节点。

### func visit(BinaryExpr)

```cangjie
protected open func visit(_: BinaryExpr): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [BinaryExpr](ast_package_classes.md#class-binaryexpr) - [BinaryExpr](ast_package_classes.md#class-binaryexpr) 类型的被遍历节点。

### func visit(Block)

```cangjie
protected open func visit(_: Block): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [Block](ast_package_classes.md#class-block) - [Block](ast_package_classes.md#class-block) 类型的被遍历节点。

### func visit(Body)

```cangjie
protected open func visit(_: Body): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [Body](ast_package_classes.md#class-body) - [Body](ast_package_classes.md#class-body) 类型的被遍历节点。

### func visit(CallExpr)

```cangjie
protected open func visit(_: CallExpr): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [CallExpr](ast_package_classes.md#class-callexpr) - [CallExpr](ast_package_classes.md#class-callexpr) 类型的被遍历节点。

### func visit(ClassDecl)

```cangjie
protected open func visit(_: ClassDecl): Unit
```

功能：定义访问节点时的操作，需要重写。

参数：

- _: [ClassDecl](ast_package_classes.md#class-classdecl) - [ClassDecl](ast_package_classes.md#class-classdecl) 类型的被遍历节点。