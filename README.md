# 📜 SquickLang Specification

SquickLang is a mini programming language inspired by Python, but with Esperanto-style keywords and custom syntax.

---

## 🔤 Keywords and Tokens

| Token        | Python Equivalent  | Category               |
|--------------|--------------------|------------------------|
| `variablo`   | variable           | Variable declaration   |
| `se`         | if                 | Conditional            |
| `gis`        | while              | Loop                   |
| `por`        | for                | Loop                   |
| `alie`       | else               | Conditional            |
| `alie se`    | elif               | Conditional            |
| `kaj`        | and                | Logical operator       |
| `au`         | or                 | Logical operator       |
| `haltu`      | break              | Loop control           |
| `daurigi`    | continue           | Loop control           |
| `difini`     | def                | Function definition    |
| `forigi`     | delete             | Deletion               |
| `provu`      | try                | Exception handling     |
| `krom`       | except             | Exception handling     |
| `malvero`    | false              | Boolean literal        |
| `vere`       | true               | Boolean literal        |
| `finfine`    | finally            | Exception handling     |
| `klaso`      | class              | Class definition       |
| `tutmonda`   | global             | Scope modifier         |
| `en`         | in                 | Membership operator    |
| `estas`      | is                 | Identity operator      |
| `funkcio`    | lambda             | Anonymous function     |
| `nenio`      | none               | Null literal           |
| `ne`         | not                | Logical negation       |
| `reveni`     | return             | Return statement       |
| `Saluton`    | (start of program) | Program entry point    |
| `adiau`      | (end of program)   | Program termination    |

---

## ➕ Arithmetic Operators

| Token        | Python Equivalent | Operation         |
|--------------|-------------------|-------------------|
| `aldoni`     | `+`               | Addition          |
| `subtrahi`   | `-`               | Subtraction       |
| `multigi`    | `*`               | Multiplication    |
| `dividi`     | `/`               | Division          |
| `modulo`     | `%`               | Modulo            |
| `intensigi`  | `**`              | Exponentiation    |

---

## 🧮 Comparison and Assignment Operators

| Token              | Python Equivalent | Operation              |
|--------------------|-------------------|------------------------|
| `asigini`          | `=`               | Assignment             |
| `egala`            | `==`              | Equality               |
| `ne egala`         | `!=`              | Inequality             |
| `granda`           | `>`               | Greater than           |
| `malgranda`        | `<`               | Less than              |
| `Granda egala?`    | `>=`              | Greater than or equal  |
| `malgranda egala`  | `<=`              | Less than or equal     |

---

## 🧱 Structural Symbols

| Symbol   | Meaning              | Category               |
|----------|----------------------|------------------------|
| `(`      | left_parenthesis     | Grouping               |
| `)`      | right_parenthesis    | Grouping               |
| `{`      | left_brace           | Block start            |
| `}`      | right_brace          | Block end              |
| `[`      | left_bracket         | Indexing/list start    |
| `]`      | right_bracket        | Indexing/list end      |
| `,`      | comma                | Separator              |
| `:`      | colon                | Block or dict separator|
| `;`      | semicolon            | Statement separator    |
| `:3`     | comment_symbol       | Comment                |

---

## 🔢 Data Types

| Token     | Python Equivalent | Type        |
|-----------|-------------------|-------------|
| `entjero` | int               | Integer     |
| `flosi`   | float             | Float       |
| `snuro`   | str               | String      |

---

## ✅ Code Example

```squick
Saluton

difini salutu(nomo: snuro):
    print("Saluton, " + nomo)

por variablo en ["Mia", "Eta", "Amiko"]:
    salutu(variablo)

adiau
```

---

