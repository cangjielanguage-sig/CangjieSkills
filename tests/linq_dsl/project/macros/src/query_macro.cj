macro package macros

import std.ast.*
import std.collection.*

func subTokens(tokens: Tokens, startIdx: Int64, endIdx: Int64): Tokens {
    var result = ArrayList<Token>()
    var i = startIdx
    while (i < endIdx) {
        result.add(tokens[i])
        i += 1
    }
    return Tokens(result)
}

func isQueryKeyword(value: String): Bool {
    return value == "from" || value == "in" || value == "where" ||
           value == "select" || value == "orderby" || value == "count" ||
           value == "asc" || value == "desc"
}

public macro query(attrTokens: Tokens, inputTokens: Tokens): Tokens {
    // Determine mode from attribute
    let isCount = (attrTokens.size > 0 && attrTokens[0].value == "count")

    let tokens = inputTokens
    let n = tokens.size

    // Step 1: Find all top-level keyword positions
    var kwPositions = ArrayList<Int64>()
    var kwNames = ArrayList<String>()
    var depth: Int64 = 0
    var i: Int64 = 0
    while (i < n) {
        let tok = tokens[i]
        let v = tok.value
        if (v == "(" || v == "[" || v == "{") {
            depth += 1
        } else if (v == ")" || v == "]" || v == "}") {
            depth -= 1
        }
        if (depth == 0 && isQueryKeyword(v)) {
            kwPositions.add(i)
            kwNames.add(v)
        }
        i += 1
    }

    // Step 2: Parse "from <var> in <expr>"
    if (kwPositions.size < 2) {
        diagReport(DiagReportLevel.ERROR, inputTokens,
            "Expected 'from <var> in <expr>'", "Missing required clauses")
        return inputTokens
    }
    if (kwNames[0] != "from" || kwNames[1] != "in") {
        diagReport(DiagReportLevel.ERROR, inputTokens,
            "Expected 'from <var> in <expr>'", "Invalid syntax")
        return inputTokens
    }

    let fromPos = kwPositions[0]
    let inPos = kwPositions[1]

    if (inPos - fromPos != 2) {
        diagReport(DiagReportLevel.ERROR, inputTokens,
            "Expected single variable name after 'from'", "")
        return inputTokens
    }
    let iterVar = tokens[fromPos + 1]

    // Step 3: Extract collection expression
    var kwIdx: Int64 = 2
    var collEnd = n
    if (kwIdx < kwPositions.size) {
        collEnd = kwPositions[kwIdx]
    }
    let collExpr = subTokens(tokens, inPos + 1, collEnd)

    // Step 4: Extract where clauses
    var whereExprs = ArrayList<Tokens>()
    while (kwIdx < kwPositions.size && kwNames[kwIdx] == "where") {
        let whereStart = kwPositions[kwIdx] + 1
        kwIdx += 1
        var whereEnd = n
        if (kwIdx < kwPositions.size) {
            whereEnd = kwPositions[kwIdx]
        }
        whereExprs.add(subTokens(tokens, whereStart, whereEnd))
    }

    if (isCount) {
        return generateCount(iterVar, collExpr, whereExprs)
    }

    // Step 5: Extract select expression
    if (kwIdx >= kwPositions.size || kwNames[kwIdx] != "select") {
        diagReport(DiagReportLevel.ERROR, inputTokens,
            "Expected 'select <expr>'", "Missing select clause")
        return inputTokens
    }
    let selectStart = kwPositions[kwIdx] + 1
    kwIdx += 1
    var selectEnd = n
    if (kwIdx < kwPositions.size) {
        selectEnd = kwPositions[kwIdx]
    }
    let selectExpr = subTokens(tokens, selectStart, selectEnd)

    // Step 6: Check for orderby
    var orderDir = ""
    if (kwIdx < kwPositions.size && kwNames[kwIdx] == "orderby") {
        kwIdx += 1
        if (kwIdx < kwPositions.size) {
            let dir = kwNames[kwIdx]
            if (dir == "desc") {
                orderDir = "desc"
            } else if (dir == "asc") {
                orderDir = "asc"
            }
        }
        if (orderDir == "") {
            orderDir = "asc"
        }
    }

    return generateSelect(attrTokens, iterVar, collExpr, whereExprs, selectExpr, orderDir)
}

func generateCount(iterVar: Token, collExpr: Tokens, whereExprs: ArrayList<Tokens>): Tokens {
    var loopBody: Tokens
    if (whereExprs.size > 0) {
        var cond = whereExprs[0]
        var i: Int64 = 1
        while (i < whereExprs.size) {
            let next = whereExprs[i]
            cond = quote($(cond) && $(next))
            i += 1
        }
        loopBody = quote(
            if ($(cond)) {
                _query_count += 1
            }
        )
    } else {
        loopBody = quote(_query_count += 1)
    }

    var code = quote({ =>
        var _query_count: Int64 = 0
        for ($(iterVar) in $(collExpr)) {
            $(loopBody)
        }
        _query_count
    })
    // Append () to immediately invoke the lambda: { => ... }()
    code = code + quote(\(\))
    return code
}

func generateSelect(resultType: Tokens, iterVar: Token, collExpr: Tokens,
                    whereExprs: ArrayList<Tokens>, selectExpr: Tokens,
                    orderDir: String): Tokens {
    var loopBody: Tokens
    if (whereExprs.size > 0) {
        var cond = whereExprs[0]
        var i: Int64 = 1
        while (i < whereExprs.size) {
            let next = whereExprs[i]
            cond = quote($(cond) && $(next))
            i += 1
        }
        loopBody = quote(
            if ($(cond)) {
                _query_result.add($(selectExpr))
            }
        )
    } else {
        loopBody = quote(_query_result.add($(selectExpr)))
    }

    var sortCode: Tokens
    if (orderDir == "asc") {
        sortCode = quote(sort(_query_result))
    } else if (orderDir == "desc") {
        sortCode = quote(
            sort(_query_result)
            _query_result.reverse()
        )
    } else {
        sortCode = Tokens()
    }

    var code = quote({ =>
        var _query_result = ArrayList<$(resultType)>()
        for ($(iterVar) in $(collExpr)) {
            $(loopBody)
        }
        $(sortCode)
        _query_result.toArray()
    })
    // Append () to immediately invoke the lambda: { => ... }()
    code = code + quote(\(\))
    return code
}
