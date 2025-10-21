from input_parce import parser, lexer

print("Enter your grammar (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":  ## empty line
        break
    lines.append(line)

data = "\n".join(lines).strip()

result = parser.parse(data, lexer=lexer)
print(result)