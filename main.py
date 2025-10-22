from input_parce import parser, lexer
from cfgPdaconvert import cfg_PdaConvert


print("Enter your grammar (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":  ## empty line
        break
    lines.append(line)


data = "\n".join(lines).strip()

stringInput = input("Enter the string")
print(stringInput)

result = parser.parse(data, lexer=lexer)
print(result)
print(next(iter(result)))

print(cfg_PdaConvert(result,next(iter(result)),stringInput))