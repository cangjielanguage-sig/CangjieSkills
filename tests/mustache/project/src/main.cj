package mustache

main(): Int64 {
    // Demo: render a Mustache template
    let template = MustacheTemplate.fromString("Hello, {{name}}! {{#items}}<li>{{.}}</li> {{/items}}{{^items}}No items.{{/items}}")
    let ctx = MustacheContext()
    ctx.put("name", MustacheStr("World"))
    let items = MustacheList()
    items.add(MustacheStr("Apple"))
    items.add(MustacheStr("Banana"))
    items.add(MustacheStr("Cherry"))
    ctx.put("items", items)
    println("Rendered:")
    println(template.render(ctx))
    return 0
}
